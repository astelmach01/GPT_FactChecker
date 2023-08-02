#!/bin/bash

# Install poetry
curl -sSL https://install.python-poetry.org | python3 -

# Install dependencies and create a virtual environment
poetry install --no-interaction --no-ansi

# Activate the virtual environment
source "$(poetry env info --path)/bin/activate"
