#!/bin/bash

# Activate the virtual environment
source .venv/bin/activate

# Load environment variables from the .env file
export $(cat .env | xargs)

# Run the tests with unittest
python3 -m unittest discover -s tests

# Deactivate the virtual environment after running tests (optional)
deactivate

# if tests break try this
# python3 -m unittest discover -s tests