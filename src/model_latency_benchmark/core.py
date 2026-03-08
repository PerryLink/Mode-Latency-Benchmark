"""核心业务逻辑：Provider 配置、数据模型、异步 Benchmark 实现"""
import asyncio
import time
from dataclasses import dataclass
from typing import Optional, Dict, Any, Callable
import httpx

# Provider 配置
PROVIDERS = {
    "deepseek": {
        "name": "DeepSeek",
        "endpoint": "https://api.deepseek.com/v1/chat/completions",
        "env_key": "DEEPSEEK_API_KEY",
        "model": "deepseek-chat",
        "auth_type": "bearer",
        "color": "green",
        "icon": "🟢"
    },
    "baidu": {
        "name": "百度文心",
        "endpoint": "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/completions",
        "env_key": "BAIDU_API_KEY",
        "model": "ernie-4.0-turbo-8k",
        "auth_type": "query_param",
        "color": "blue",
        "icon": "🔵"
    },
    "alibaba": {
        "name": "阿里通义",
        "endpoint": "https://dashscope.aliyuncs.com/api/v1/services/aigc/text-generation/generation",
        "env_key": "ALIBABA_API_KEY",
        "model": "qwen-turbo",
        "auth_type": "bearer",
        "color": "orange",
        "icon": "🟠"
    },
    "bytedance": {
        "name": "字节豆包",
        "endpoint": "https://ark.cn-beijing.volces.com/api/v3/chat/completions",
        "env_key": "BYTEDANCE_API_KEY",
        "model": "doubao-pro-4k",
        "auth_type": "bearer",
        "color": "magenta",
        "icon": "🟣"
    }
}

@dataclass
class BenchmarkResult:
    """Benchmark 结果数据模型"""
    provider_id: str
    provider_name: str
    ttft: Optional[float]  # Time to first token (秒)
    total_time: Optional[float]  # 总响应时间 (秒)
    tokens: int
    error: Optional[str]
    success: bool

def build_request_headers(provider: Dict[str, Any], api_key: str) -> Dict[str, str]:
    """构建请求头"""
    headers = {"Content-Type": "application/json"}
    if provider["auth_type"] == "bearer":
        headers["Authorization"] = f"Bearer {api_key}"
    return headers

def build_request_body(provider: Dict[str, Any], prompt: str) -> Dict[str, Any]:
    """构建请求体"""
    if provider["auth_type"] == "query_param":
        # 百度文心使用不同的格式
        return {
            "messages": [{"role": "user", "content": prompt}],
            "stream": True
        }
    else:
        # OpenAI 兼容格式
        return {
            "model": provider["model"],
            "messages": [{"role": "user", "content": prompt}],
            "stream": True
        }

def build_request_url(provider: Dict[str, Any], api_key: str) -> str:
    """构建请求 URL"""
    url = provider["endpoint"]
    if provider["auth_type"] == "query_param":
        url = f"{url}?access_token={api_key}"
    return url

async def benchmark_provider(
    provider_id: str,
    provider: Dict[str, Any],
    api_key: str,
    prompt: str,
    client: httpx.AsyncClient,
    timeout: int,
    progress_callback: Optional[Callable] = None
) -> BenchmarkResult:
    """单个 provider 的性能测试"""
    start_time = time.time()
    ttft = None
    tokens = 0
    error = None

    try:
        if progress_callback:
            progress_callback(provider_id, "start", None)

        headers = build_request_headers(provider, api_key)
        body = build_request_body(provider, prompt)
        url = build_request_url(provider, api_key)

        async with client.stream(
            "POST",
            url,
            headers=headers,
            json=body,
            timeout=timeout
        ) as response:
            response.raise_for_status()

            async for chunk in response.aiter_bytes():
                if chunk:
                    if ttft is None:
                        ttft = time.time() - start_time
                        if progress_callback:
                            progress_callback(provider_id, "ttft", ttft)
                    tokens += 1

        total_time = time.time() - start_time
        if progress_callback:
            progress_callback(provider_id, "complete", total_time)

        return BenchmarkResult(
            provider_id=provider_id,
            provider_name=provider["name"],
            ttft=ttft,
            total_time=total_time,
            tokens=tokens,
            error=None,
            success=True
        )

    except httpx.TimeoutException:
        error = f"Timeout (>{timeout}s)"
    except httpx.HTTPStatusError as e:
        if e.response.status_code in [401, 403]:
            error = "认证失败，请检查 API key"
        elif e.response.status_code == 429:
            error = "请求限流，请稍后重试"
        else:
            error = f"HTTP {e.response.status_code}"
    except httpx.RequestError as e:
        error = f"网络错误: {type(e).__name__}"
    except Exception as e:
        error = f"未知错误: {type(e).__name__}"

    if progress_callback:
        progress_callback(provider_id, "error", error)

    return BenchmarkResult(
        provider_id=provider_id,
        provider_name=provider["name"],
        ttft=None,
        total_time=None,
        tokens=0,
        error=error,
        success=False
    )

async def run_all_benchmarks(
    providers: Dict[str, Dict[str, Any]],
    api_keys: Dict[str, str],
    prompt: str,
    timeout: int = 30,
    progress_callback: Optional[Callable] = None
) -> list[BenchmarkResult]:
    """并发执行所有 provider 测试"""
    async with httpx.AsyncClient() as client:
        tasks = [
            benchmark_provider(
                provider_id,
                provider,
                api_keys[provider_id],
                prompt,
                client,
                timeout,
                progress_callback
            )
            for provider_id, provider in providers.items()
            if provider_id in api_keys
        ]
        results = await asyncio.gather(*tasks)
        return list(results)
