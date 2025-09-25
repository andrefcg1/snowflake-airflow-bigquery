# Contributing to Snowflake to BigQuery ETL Pipeline

Thank you for your interest in contributing to this project! This document provides guidelines and information for contributors.

## 🚀 Getting Started

1. Fork the repository
2. Clone your fork locally
3. Create a new branch for your feature or bugfix
4. Make your changes
5. Test your changes
6. Submit a pull request

## 📋 Development Setup

### Prerequisites
- Python 3.8+
- Docker
- Git

### Setup Steps
1. Clone the repository
2. Create a virtual environment
3. Install dependencies
4. Set up your local configuration

```bash
git clone <your-fork-url>
cd snowflake-airflow-bigquery
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## 🔧 Configuration

Before contributing, make sure to:
1. Copy `airflow_settings.yaml.example` to `airflow_settings.yaml`
2. Update the configuration with your test credentials
3. Never commit real credentials or sensitive data

## 📝 Code Style

- Follow PEP 8 style guidelines
- Use meaningful variable and function names
- Add docstrings to functions and classes
- Include type hints where appropriate

## 🧪 Testing

Before submitting a pull request:
1. Test your changes locally
2. Ensure all existing tests pass
3. Add new tests for new functionality
4. Test with different Airflow versions if applicable

## 📋 Pull Request Process

1. **Create a feature branch** from `main`
2. **Make your changes** following the code style guidelines
3. **Test your changes** thoroughly
4. **Update documentation** if needed
5. **Submit a pull request** with a clear description

### Pull Request Template

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Testing
- [ ] Local testing completed
- [ ] All existing tests pass
- [ ] New tests added (if applicable)

## Checklist
- [ ] Code follows style guidelines
- [ ] Self-review completed
- [ ] Documentation updated
- [ ] No sensitive data committed
```

## 🐛 Reporting Issues

When reporting issues, please include:
- Airflow version
- Python version
- Error messages and logs
- Steps to reproduce
- Expected vs actual behavior

## 💡 Feature Requests

For feature requests, please:
- Check existing issues first
- Provide a clear description
- Explain the use case
- Consider contributing the feature yourself

## 📄 License

By contributing, you agree that your contributions will be licensed under the MIT License.

## 🆘 Getting Help

- Check existing issues and discussions
- Review the README.md for setup instructions
- Open a new issue for questions or problems

Thank you for contributing! 🎉
