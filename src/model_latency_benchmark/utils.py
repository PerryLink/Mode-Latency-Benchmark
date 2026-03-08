"""Rich 视觉展示工具：进度条、结果表格、格式化函数"""
from typing import Dict, Any
from rich.console import Console
from rich.table import Table
from rich.live import Live
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TimeElapsedColumn

def create_racing_display(providers: Dict[str, Dict[str, Any]], progress_data: Dict[str, Any]) -> Live:
    """创建赛车式的进度条显示"""
    def generate_display():
        table = Table(show_header=False, box=None, padding=(0, 1))
        table.add_column("Provider", style="bold")
        table.add_column("Progress", ratio=1)
        table.add_column("Time", justify="right")

        for provider_id, provider in providers.items():
            icon = provider["icon"]
            name = provider["name"]
            color = provider["color"]

            if provider_id not in progress_data:
                status = "⏳ 等待中..."
                table.add_row(f"{icon} {name}", status, "")
            else:
                data = progress_data[provider_id]
                status_type = data.get("status", "pending")

                if status_type == "running":
                    ttft = data.get("ttft")
                    if ttft:
                        bar = "█" * 15 + "⚡" + "░" * 14
                        time_str = f"{int(ttft * 1000)}ms"
                    else:
                        bar = "▓" * 10 + "░" * 20
                        time_str = "..."
                    table.add_row(f"{icon} {name}", f"[{color}]{bar}[/{color}]", time_str)
                elif status_type == "complete":
                    total = data.get("total", 0)
                    ttft = data.get("ttft", 0)
                    bar = "█" * 30
                    time_str = f"✓ {int(ttft * 1000)}ms / {total:.2f}s"
                    table.add_row(f"{icon} {name}", f"[{color}]{bar}[/{color}]", f"[green]{time_str}[/green]")
                elif status_type == "error":
                    error = data.get("error", "未知错误")
                    table.add_row(f"{icon} {name}", f"[red]✗ {error}[/red]", "")

        return Panel(table, title="🏁 Model Latency Benchmark - Racing Mode 🏁", border_style="cyan")

    return Live(generate_display(), refresh_per_second=4)

def display_results(console: Console, results: list):
    """显示最终排名表"""
    # 按 TTFT 排序（成功的在前）
    successful = [r for r in results if r.success]
    failed = [r for r in results if not r.success]
    successful.sort(key=lambda x: x.ttft or float('inf'))

    # 创建结果表格
    table = Table(title="📊 最终结果", show_header=True, header_style="bold cyan")
    table.add_column("排名", justify="center", style="cyan")
    table.add_column("Provider", style="bold")
    table.add_column("TTFT", justify="right")
    table.add_column("总时间", justify="right")
    table.add_column("状态", justify="center")

    # 添加成功的结果
    for i, result in enumerate(successful, 1):
        rank = "🏆" if i == 1 else f"{i}"
        ttft_str = f"{int(result.ttft * 1000)}ms" if result.ttft else "-"
        total_str = f"{result.total_time:.2f}s" if result.total_time else "-"
        status = "[green]✓[/green]"

        style = "bold green" if i == 1 else None
        table.add_row(rank, result.provider_name, ttft_str, total_str, status, style=style)

    # 添加失败的结果
    for result in failed:
        table.add_row("-", result.provider_name, "-", "-", f"[red]✗ {result.error}[/red]")

    console.print()
    console.print(table)

    # 显示冠军信息
    if successful:
        winner = successful[0]
        console.print()
        console.print(
            f"[bold green]🏆 Winner: {winner.provider_name}[/bold green] "
            f"([cyan]{int(winner.ttft * 1000)}ms[/cyan] TTFT, "
            f"[cyan]{winner.total_time:.2f}s[/cyan] total)"
        )
