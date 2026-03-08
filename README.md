# Model Latency Benchmark

> A CLI tool for real-time comparison of Chinese LLM API response speeds

[![Python Version](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

## Features

- 🚀 **Real-time Performance Comparison** - Concurrently measure response speeds of multiple LLM APIs
- ⚡ **TTFT Measurement** - Precisely record Time To First Token
- 🎮 **Racing-style Visualization** - Dynamic progress bars using Rich library, intuitive like a racing game
- 🎯 **Developer Friendly** - Simple CLI commands to run
- 🔧 **Flexible Configuration** - Support custom prompts, select specific providers, set timeout

## Quick Start

### Installation

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

### Configuration

Create a `.env` file and add your API keys:

```bash
# DeepSeek API Key
DEEPSEEK_API_KEY=sk-your-key-here

# Baidu Wenxin API Key
BAIDU_API_KEY=your-key-here

# Alibaba Tongyi API Key
ALIBABA_API_KEY=your-key-here

# ByteDance Doubao API Key
BYTEDANCE_API_KEY=your-key-here
```

### Usage

```bash
# Test all configured providers with default prompt
model-latency-benchmark

# Use custom prompt
model-latency-benchmark --prompt "Introduce machine learning in one sentence"

# Test specific providers only
model-latency-benchmark --providers deepseek,baidu

# Set timeout (default 30 seconds)
model-latency-benchmark --timeout 60

# Show debug information
model-latency-benchmark --debug
```

## Supported Providers

| Provider | Name | Environment Variable | Get API Key |
|----------|------|---------------------|-------------|
| `deepseek` | DeepSeek | `DEEPSEEK_API_KEY` | [DeepSeek Platform](https://platform.deepseek.com/) |
| `baidu` | Baidu Wenxin | `BAIDU_API_KEY` | [Baidu AI Cloud](https://cloud.baidu.com/) |
| `alibaba` | Alibaba Tongyi | `ALIBABA_API_KEY` | [Alibaba Cloud DashScope](https://dashscope.aliyun.com/) |
| `bytedance` | ByteDance Doubao | `BYTEDANCE_API_KEY` | [Volcano Engine](https://www.volcengine.com/) |

## Project Structure

```
model-latency-benchmark/
├── src/
│   └── model_latency_benchmark/
│       ├── __init__.py
│       ├── __main__.py
│       ├── cli.py          # CLI interface
│       ├── core.py         # Core benchmark logic
│       └── utils.py        # Utility functions
├── tests/                  # Test files
├── pyproject.toml          # Project configuration
└── README.md
```

## Tech Stack

- **CLI Framework**: Click
- **HTTP Client**: httpx (async support)
- **Terminal UI**: Rich
- **Environment**: python-dotenv
- **Package Manager**: Poetry

## Development

### Install Dependencies

```bash
poetry install
```

### Run Tests

```bash
poetry run pytest --cov
```

### Code Formatting

```bash
poetry run black .
poetry run ruff check .
```

### Type Checking

```bash
poetry run mypy src/
```

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

Copyright 2026 Chance Dean (novelnexusai@outlook.com)

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for contribution guidelines.

## Feedback

For issues or suggestions, please submit an [Issue](https://github.com/PerryLink/model-latency-benchmark/issues).

---

# Model Latency Benchmark

> 实时对比国产大模型 API 响应速度的 CLI 工具

[![Python 版本](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![许可证](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

## 核心特性

- 🚀 **实时性能对比** - 并发测量多个大模型 API 的响应速度
- ⚡ **TTFT 测量** - 精确记录首字延迟(Time To First Token)
- 🎮 **赛车式可视化** - 使用 Rich 库创建动态进度条,像赛车游戏一样直观
- 🎯 **开发者友好** - 简单的 CLI 命令即可运行
- 🔧 **灵活配置** - 支持自定义提示词、选择特定 providers、设置超时时间

## 快速开始

### 安装

使用 pip:

```bash
pip install model-latency-benchmark
```

使用 Poetry(开发):

```bash
git clone https://github.com/PerryLink/model-latency-benchmark.git
cd model-latency-benchmark
poetry install
```

### 配置

创建 `.env` 文件并添加你的 API keys:

```bash
# DeepSeek API Key
DEEPSEEK_API_KEY=sk-your-key-here

# 百度文心 API Key
BAIDU_API_KEY=your-key-here

# 阿里通义 API Key
ALIBABA_API_KEY=your-key-here

# 字节豆包 API Key
BYTEDANCE_API_KEY=your-key-here
```

### 使用指南

```bash
# 使用默认提示词测试所有配置的 providers
model-latency-benchmark

# 使用自定义提示词
model-latency-benchmark --prompt "请用一句话介绍机器学习"

# 只测试特定的 providers
model-latency-benchmark --providers deepseek,baidu

# 设置超时时间(默认 30 秒)
model-latency-benchmark --timeout 60

# 显示调试信息
model-latency-benchmark --debug
```

## 支持的 Providers

| Provider | 名称 | 环境变量 | 获取 API Key |
|----------|------|----------|--------------|
| `deepseek` | DeepSeek | `DEEPSEEK_API_KEY` | [DeepSeek 平台](https://platform.deepseek.com/) |
| `baidu` | 百度文心 | `BAIDU_API_KEY` | [百度智能云](https://cloud.baidu.com/) |
| `alibaba` | 阿里通义 | `ALIBABA_API_KEY` | [阿里云 DashScope](https://dashscope.aliyun.com/) |
| `bytedance` | 字节豆包 | `BYTEDANCE_API_KEY` | [火山引擎](https://www.volcengine.com/) |

## 项目结构

```
model-latency-benchmark/
├── src/
│   └── model_latency_benchmark/
│       ├── __init__.py
│       ├── __main__.py
│       ├── cli.py          # CLI 接口
│       ├── core.py         # 核心基准测试逻辑
│       └── utils.py        # 工具函数
├── tests/                  # 测试文件
├── pyproject.toml          # 项目配置
└── README.md
```

## 技术栈

- **CLI 框架**: Click
- **HTTP 客户端**: httpx (异步支持)
- **终端 UI**: Rich
- **环境配置**: python-dotenv
- **包管理器**: Poetry

## 开发

### 安装依赖

```bash
poetry install
```

### 运行测试

```bash
poetry run pytest --cov
```

### 代码格式化

```bash
poetry run black .
poetry run ruff check .
```

### 类型检查

```bash
poetry run mypy src/
```

## 许可证

本项目采用 Apache License 2.0 许可证 - 详见 [LICENSE](LICENSE) 文件。

版权所有 2026 Chance Dean (novelnexusai@outlook.com)

## 贡献

查看 [CONTRIBUTING.md](CONTRIBUTING.md) 了解贡献指南。

## 反馈

如有问题或建议,请提交 [Issue](https://github.com/PerryLink/model-latency-benchmark/issues)。
