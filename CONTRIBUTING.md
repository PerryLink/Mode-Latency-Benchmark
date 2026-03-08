# Contributing to Model Latency Benchmark

## Project Status

This is currently a personal project maintained by Chance Dean (novelnexusai@outlook.com). While contributions are welcome, please note that this project is primarily developed and maintained by a single person.

## How to Report Issues

If you encounter any bugs or have feature suggestions, please:

1. Check the [existing issues](https://github.com/PerryLink/model-latency-benchmark/issues) to avoid duplicates
2. Create a new issue with:
   - A clear, descriptive title
   - Detailed description of the problem or suggestion
   - Steps to reproduce (for bugs)
   - Expected vs actual behavior
   - Your environment (OS, Python version, etc.)

## Development Environment Setup

### Prerequisites

- Python 3.9 or higher
- Poetry (for dependency management)

### Setup Steps

1. Clone the repository:
```bash
git clone https://github.com/PerryLink/model-latency-benchmark.git
cd model-latency-benchmark
```

2. Install dependencies using Poetry:
```bash
poetry install
```

3. Set up your API keys in a `.env` file:
```bash
cp .env.example .env
# Edit .env and add your API keys
```

4. Run tests to verify setup:
```bash
poetry run pytest
```

## Code Standards

This project follows Python best practices:

### PEP 8 Style Guide

- Follow [PEP 8](https://pep8.org/) for Python code style
- Use 4 spaces for indentation (no tabs)
- Maximum line length: 100 characters
- Use meaningful variable and function names

### Code Formatting

We use automated tools to maintain code quality:

```bash
# Format code with Black
poetry run black .

# Check code with Ruff
poetry run ruff check .

# Type checking with mypy
poetry run mypy src/
```

### Testing

- Write tests for new features
- Ensure all tests pass before submitting:
```bash
poetry run pytest --cov
```

## Pull Request Process

1. **Fork the repository** and create your branch from `main`:
```bash
git checkout -b feature/your-feature-name
```

2. **Make your changes**:
   - Write clear, concise commit messages
   - Follow the code standards above
   - Add tests for new functionality
   - Update documentation if needed

3. **Test your changes**:
```bash
# Run tests
poetry run pytest --cov

# Format code
poetry run black .

# Check linting
poetry run ruff check .

# Type check
poetry run mypy src/
```

4. **Commit your changes**:
```bash
git add .
git commit -m "Add: brief description of your changes"
```

5. **Push to your fork**:
```bash
git push origin feature/your-feature-name
```

6. **Create a Pull Request**:
   - Go to the original repository
   - Click "New Pull Request"
   - Select your fork and branch
   - Provide a clear description of your changes
   - Reference any related issues

### PR Guidelines

- Keep PRs focused on a single feature or fix
- Write a clear PR description explaining:
  - What changes were made
  - Why the changes were necessary
  - How to test the changes
- Be responsive to feedback and questions
- Ensure CI checks pass

## Commit Message Format

Use clear, descriptive commit messages:

```
Add: new feature description
Fix: bug description
Update: improvement description
Refactor: code restructuring description
Docs: documentation changes
Test: test-related changes
```

## Questions?

If you have questions about contributing, feel free to:
- Open an issue for discussion
- Contact the maintainer at novelnexusai@outlook.com

## License

By contributing to this project, you agree that your contributions will be licensed under the Apache License 2.0.

---

Thank you for contributing to Model Latency Benchmark! 🚀
