<div align="center">

# Mode-Latency-Benchmark

**A CLI tool for real-time comparison of Chinese LLM API response speed (TTFT and total time).**

*Ported into [dsh-budget](https://github.com/PerryLink/dsh-budget) — part of the PerryLink DSH Plugin Family.*

[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)

[English](README.md) · [简体中文](README.zh.md)

</div>

---

## What it does

`model-latency-benchmark` streams the same prompt to multiple Chinese LLM providers concurrently and
measures each one's time-to-first-token (TTFT) and total response time, showing live, racing-style
progress bars and a ranked result table.

## Features

- 🚀 Concurrent real-time comparison of multiple LLM APIs
- ⚡ Time-to-first-token (TTFT) and total-time measurement
- 🎮 Racing-style live progress bars (Rich)
- 🔧 Custom prompt, provider selection, and timeout

## Quick start

```bash
pip install model-latency-benchmark
```

Create a `.env` file with the API keys for the providers you want to test:

```bash
DEEPSEEK_API_KEY=sk-your-key-here
BAIDU_API_KEY=your-key-here
ALIBABA_API_KEY=your-key-here
BYTEDANCE_API_KEY=your-key-here
```

## Usage

```bash
# Test all providers with an API key set
model-latency-benchmark

# Custom prompt
model-latency-benchmark --prompt "Introduce machine learning in one sentence"

# Only specific providers
model-latency-benchmark --providers deepseek,baidu

# Set request timeout (default 30 s)
model-latency-benchmark --timeout 60

# Show debug information
model-latency-benchmark --debug
```

## Supported providers

| Provider | Name | Environment variable |
|----------|------|---------------------|
| `deepseek` | DeepSeek | `DEEPSEEK_API_KEY` |
| `baidu` | 百度文心 | `BAIDU_API_KEY` |
| `alibaba` | 阿里通义 | `ALIBABA_API_KEY` |
| `bytedance` | 字节豆包 | `BYTEDANCE_API_KEY` |

## Development

```bash
poetry install
poetry run pytest --cov
poetry run black .
poetry run ruff check .
```

## License

[Apache License 2.0](LICENSE) © 2026 PerryLink
