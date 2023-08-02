#!/bin/bash

# Activate the virtual environment
source "$(poetry env info --path)/bin/activate"

# Install dev dependencies
poetry install --no-interaction --no-ansi --with dev

pip install pre-commit

# Install pre-commit hooks
pre-commit install
