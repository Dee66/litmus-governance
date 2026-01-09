.PHONY: help install install-dev test lint clean build

help:
	@echo "Available commands:"
	@echo "  make install      - Install package"
	@echo "  make install-dev  - Install package with dev dependencies"
	@echo "  make test         - Run tests"
	@echo "  make lint         - Run linters"
	@echo "  make clean        - Remove build artifacts"
	@echo "  make build        - Build distribution"

install:
	pip install -e .

install-dev:
	pip install -e .[dev]

test:
	pytest

lint:
	@echo "Linting not configured yet"

clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

build:
	python -m build
