# Contributing to easy-dotenv

We love your input! We want to make contributing to easy-dotenv as easy and transparent as possible.

## Development Process

1. Fork the repo and create your branch from `main`
2. Set up your development environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # or `venv\Scripts\activate` on Windows
   pip install -e ".[dev]"
   ```
3. Make your changes
4. Run tests and ensure they pass:
   ```bash
   pytest
   pytest --cov=easy_dotenv
   ```
5. Push your changes and create a pull request

## Pull Request Process

1. Update the README.md with details of changes if needed
2. Update the CHANGELOG.md with details of changes
3. The PR will be merged once you have the sign-off of at least one maintainer

## Code Style

- Follow PEP 8 guidelines
- Write docstrings for new functions and classes
- Add type hints where possible
- Write tests for new functionality

## License

By contributing, you agree that your contributions will be licensed under the MIT License. 