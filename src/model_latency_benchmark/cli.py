"""CLI 接口实现"""
import asyncio
import os
import sys
from typing import Optional
import click
from dotenv import load_dotenv
from rich.console import Console

from .core import PROVIDERS, run_all_benchmarks
from .utils import create_racing_display, display_results

@click.command()
@click.option('--prompt', default='请用一句话介绍人工智能', help='测试用的提示词')
@click.option('--providers', help='指定要测试的 providers，逗号分隔（如: deepseek,baidu）')
@click.option('--timeout', default=30, help='请求超时时间（秒）')
@click.option('--debug', is_flag=True, help='显示调试信息')
def main(prompt: str, providers: Optional[str], timeout: int, debug: bool):
    """🏁 国产大模型 API 延迟对比工具

    实时测量并对比多个国产大模型 API 的响应速度。
    """
    console = Console()

    # 加载环境变量
    load_dotenv()

    # 验证 API keys
    api_keys = {}
    selected_providers = {}

    # 如果指定了 providers，只测试指定的
    if providers:
        provider_list = [p.strip() for p in providers.split(',')]
        for provider_id in provider_list:
            if provider_id not in PROVIDERS:
                console.print(f"[red]错误: 未知的 provider '{provider_id}'[/red]")
                console.print(f"可用的 providers: {', '.join(PROVIDERS.keys())}")
                sys.exit(1)
            selected_providers[provider_id] = PROVIDERS[provider_id]
    else:
        selected_providers = PROVIDERS

    # 检查 API keys
    for provider_id, provider in selected_providers.items():
        api_key = os.getenv(provider["env_key"])
        if api_key:
            api_keys[provider_id] = api_key
        elif debug:
            console.print(f"[yellow]警告: 未找到 {provider['name']} 的 API key ({provider['env_key']})[/yellow]")

    if not api_keys:
        console.print("[red]错误: 未找到任何有效的 API key[/red]")
        console.print("\n请在 .env 文件中配置至少一个 API key:")
        for provider in selected_providers.values():
            console.print(f"  {provider['env_key']}=your-key-here")
        console.print("\n或者使用环境变量:")
        console.print(f"  export {list(selected_providers.values())[0]['env_key']}=your-key-here")
        sys.exit(1)

    # 只测试有 API key 的 providers
    test_providers = {k: v for k, v in selected_providers.items() if k in api_keys}

    console.print(f"\n[bold cyan]🏁 Model Latency Benchmark - Racing Mode 🏁[/bold cyan]\n")
    console.print(f"测试提示词: [italic]{prompt}[/italic]")
    console.print(f"参与测试: {', '.join([p['name'] for p in test_providers.values()])}\n")

    # 创建进度显示
    progress_data = {}
    live_display = create_racing_display(test_providers, progress_data)

    def progress_callback(provider_id: str, event_type: str, value):
        """进度回调函数"""
        if event_type == "start":
            progress_data[provider_id] = {"status": "running", "ttft": None, "total": None}
        elif event_type == "ttft":
            progress_data[provider_id]["ttft"] = value
        elif event_type == "complete":
            progress_data[provider_id]["status"] = "complete"
            progress_data[provider_id]["total"] = value
        elif event_type == "error":
            progress_data[provider_id]["status"] = "error"
            progress_data[provider_id]["error"] = value

    # 运行 benchmark
    with live_display:
        results = asyncio.run(
            run_all_benchmarks(
                test_providers,
                api_keys,
                prompt,
                timeout,
                progress_callback
            )
        )

    # 显示结果
    console.print()
    display_results(console, results)

    if debug:
        console.print("\n[dim]调试信息:[/dim]")
        for result in results:
            console.print(f"  {result.provider_name}: {result}")

if __name__ == "__main__":
    main()
