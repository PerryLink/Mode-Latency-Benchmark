<div align="center">

# Mode-Latency-Benchmark

**实时对比国内大模型 API 响应速度（首字延迟与总耗时）的 CLI 工具。**

*已移植到 [dsh-budget](https://github.com/PerryLink/dsh-budget) —— PerryLink DSH 插件家族的一员。*

[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)

[English](README.md) · [简体中文](README.zh.md)

</div>

---

## 功能简介

`model-latency-benchmark` 将同一条提示词并发发送给多个国内大模型提供商，测量各自的首字延迟（TTFT）
和总响应时间，并以赛车式实时进度条和排序结果表展示。

## 特性

- 🚀 并发实时对比多个大模型 API
- ⚡ 测量首字延迟（TTFT）与总耗时
- 🎮 赛车式实时进度条（基于 Rich）
- 🔧 支持自定义提示词、选择提供商、设置超时

## 快速开始

```bash
pip install model-latency-benchmark
```

创建 `.env` 文件，填写你要测试的提供商 API key：

```bash
DEEPSEEK_API_KEY=sk-your-key-here
BAIDU_API_KEY=your-key-here
ALIBABA_API_KEY=your-key-here
BYTEDANCE_API_KEY=your-key-here
```

## 使用方法

```bash
# 测试所有已配置 API key 的提供商
model-latency-benchmark

# 自定义提示词
model-latency-benchmark --prompt "请用一句话介绍机器学习"

# 只测试指定提供商
model-latency-benchmark --providers deepseek,baidu

# 设置请求超时（默认 30 秒）
model-latency-benchmark --timeout 60

# 显示调试信息
model-latency-benchmark --debug
```

## 支持的提供商

| Provider | 名称 | 环境变量 |
|----------|------|----------|
| `deepseek` | DeepSeek | `DEEPSEEK_API_KEY` |
| `baidu` | 百度文心 | `BAIDU_API_KEY` |
| `alibaba` | 阿里通义 | `ALIBABA_API_KEY` |
| `bytedance` | 字节豆包 | `BYTEDANCE_API_KEY` |

## 开发

```bash
poetry install
poetry run pytest --cov
poetry run black .
poetry run ruff check .
```

## 许可证

[Apache License 2.0](LICENSE) © 2026 PerryLink
