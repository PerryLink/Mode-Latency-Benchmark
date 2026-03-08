"""核心逻辑测试"""
import pytest
from model_latency_benchmark.core import (
    PROVIDERS,
    BenchmarkResult,
    build_request_headers,
    build_request_body,
    build_request_url,
)

def test_providers_config():
    """测试 PROVIDERS 配置"""
    assert "deepseek" in PROVIDERS
    assert "baidu" in PROVIDERS
    assert PROVIDERS["deepseek"]["name"] == "DeepSeek"
    assert PROVIDERS["deepseek"]["auth_type"] == "bearer"

def test_benchmark_result_dataclass():
    """测试 BenchmarkResult 数据类"""
    result = BenchmarkResult(
        provider_id="deepseek",
        provider_name="DeepSeek",
        ttft=0.245,
        total_time=1.2,
        tokens=100,
        error=None,
        success=True
    )
    assert result.provider_id == "deepseek"
    assert result.success is True
    assert result.ttft == 0.245

def test_build_request_headers_bearer():
    """测试构建 Bearer 认证头"""
    provider = {"auth_type": "bearer"}
    headers = build_request_headers(provider, "sk-test-key")
    assert headers["Authorization"] == "Bearer sk-test-key"
    assert headers["Content-Type"] == "application/json"

def test_build_request_headers_query_param():
    """测试构建查询参数认证头"""
    provider = {"auth_type": "query_param"}
    headers = build_request_headers(provider, "test-key")
    assert "Authorization" not in headers
    assert headers["Content-Type"] == "application/json"

def test_build_request_body():
    """测试构建请求体"""
    provider = {"auth_type": "bearer", "model": "test-model"}
    body = build_request_body(provider, "Hello")
    assert body["model"] == "test-model"
    assert body["messages"][0]["content"] == "Hello"
    assert body["stream"] is True

def test_build_request_url_bearer():
    """测试构建 URL（Bearer 认证）"""
    provider = {"endpoint": "https://api.example.com", "auth_type": "bearer"}
    url = build_request_url(provider, "sk-test-key")
    assert url == "https://api.example.com"

def test_build_request_url_query_param():
    """测试构建 URL（查询参数认证）"""
    provider = {"endpoint": "https://api.example.com", "auth_type": "query_param"}
    url = build_request_url(provider, "test-key")
    assert url == "https://api.example.com?access_token=test-key"
