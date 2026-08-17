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

使用 pip：

```bash
pip install model-latency-benchmark
```

使用 Poetry（开发）：

```bash
git clone https://github.com/PerryLink/model-latency-benchmark.git
cd model-latency-benchmark
poetry install
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

| Provider | 名称 | 环境变量 | 获取 API Key |
|----------|------|----------|--------------|
| `deepseek` | DeepSeek | `DEEPSEEK_API_KEY` | [DeepSeek 平台](https://platform.deepseek.com/) |
| `baidu` | 百度文心 | `BAIDU_API_KEY` | [百度智能云](https://cloud.baidu.com/) |
| `alibaba` | 阿里通义 | `ALIBABA_API_KEY` | [阿里云 DashScope](https://dashscope.aliyun.com/) |
| `bytedance` | 字节豆包 | `BYTEDANCE_API_KEY` | [火山引擎](https://www.volcengine.com/) |

## 项目结构

```
model-latency-benchmark/
├── src/model_latency_benchmark/
│   ├── __init__.py
│   ├── __main__.py
│   ├── cli.py              # CLI 接口
│   ├── core.py             # 核心基准测试逻辑
│   └── utils.py            # 工具函数
├── tests/                  # 测试文件
├── pyproject.toml          # Poetry 配置
└── README.md
```

## 技术栈

- **CLI 框架**：Click
- **HTTP 客户端**：httpx（异步支持）
- **终端 UI**：Rich
- **环境配置**：python-dotenv
- **包管理器**：Poetry

## 开发

```bash
poetry install
poetry run pytest --cov
poetry run black .
poetry run ruff check .
poetry run mypy src/
```

## 贡献

查看 [CONTRIBUTING.md](CONTRIBUTING.md) 了解贡献指南。如有问题或建议，
请提交 [Issue](https://github.com/PerryLink/model-latency-benchmark/issues)。

## 相关项目

- [dsh-budget](https://github.com/PerryLink/dsh-budget) — 本项目被移植进的 DSH 插件
- [PerryLink](https://github.com/PerryLink) — PerryLink DSH 插件家族

## 许可证

[Apache License 2.0](LICENSE) © 2026 PerryLink
