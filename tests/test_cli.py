"""CLI 测试"""
import pytest
from click.testing import CliRunner
from model_latency_benchmark.cli import main

def test_cli_help():
    """测试 --help 选项"""
    runner = CliRunner()
    result = runner.invoke(main, ['--help'])
    assert result.exit_code == 0
    assert '国产大模型 API 延迟对比工具' in result.output

def test_cli_no_api_keys(monkeypatch):
    """测试没有 API keys 的情况"""
    runner = CliRunner()
    # 清除所有环境变量
    monkeypatch.delenv("DEEPSEEK_API_KEY", raising=False)
    monkeypatch.delenv("BAIDU_API_KEY", raising=False)
    monkeypatch.delenv("ALIBABA_API_KEY", raising=False)
    monkeypatch.delenv("BYTEDANCE_API_KEY", raising=False)

    result = runner.invoke(main, [])
    assert result.exit_code == 1
    assert '未找到任何有效的 API key' in result.output
