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

Using pip:

```bash
pip install model-latency-benchmark
```

Using Poetry (for development):

```bash
git clone https://github.com/PerryLink/model-latency-benchmark.git
cd model-latency-benchmark
poetry install
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

| Provider | Name | Environment variable | Get API key |
|----------|------|---------------------|-------------|
| `deepseek` | DeepSeek | `DEEPSEEK_API_KEY` | [DeepSeek Platform](https://platform.deepseek.com/) |
| `baidu` | 百度文心 | `BAIDU_API_KEY` | [Baidu AI Cloud](https://cloud.baidu.com/) |
| `alibaba` | 阿里通义 | `ALIBABA_API_KEY` | [Alibaba Cloud DashScope](https://dashscope.aliyun.com/) |
| `bytedance` | 字节豆包 | `BYTEDANCE_API_KEY` | [Volcano Engine](https://www.volcengine.com/) |

## Project structure

```
model-latency-benchmark/
├── src/model_latency_benchmark/
│   ├── __init__.py
│   ├── __main__.py
│   ├── cli.py              # CLI interface
│   ├── core.py             # Core benchmark logic
│   └── utils.py            # Utility functions
├── tests/                  # Test files
├── pyproject.toml          # Poetry configuration
└── README.md
```

## Tech stack

- **CLI framework**: Click
- **HTTP client**: httpx (async support)
- **Terminal UI**: Rich
- **Environment**: python-dotenv
- **Package manager**: Poetry

## Development

```bash
poetry install
poetry run pytest --cov
poetry run black .
poetry run ruff check .
poetry run mypy src/
```

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for contribution guidelines. For issues or suggestions,
please submit an [Issue](https://github.com/PerryLink/model-latency-benchmark/issues).

## Related

- [dsh-budget](https://github.com/PerryLink/dsh-budget) — the DSH plugin this project was ported into
- [PerryLink](https://github.com/PerryLink) — the PerryLink DSH Plugin Family

## License

[Apache License 2.0](LICENSE) © 2026 PerryLink
