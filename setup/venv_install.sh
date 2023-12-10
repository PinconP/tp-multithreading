#!/bin/bash

# Define the name of the virtual environment directory
VENV_DIR=".venv"

# Check if the virtual environment directory exists
if [ -d "$VENV_DIR" ]; then
    echo "Virtual environment already exists"
else
    # Create the virtual environment
    python3 -m venv $VENV_DIR
    echo "Virtual environment created"
fi

# Activate the virtual environment
source $VENV_DIR/bin/activate

# Upgrade pip
pip install --upgrade pip

# Check if requirements.txt exists
if [ -f "setup/requirements.txt" ]; then
    # Install requirements
    pip install -r setup/requirements.txt
    echo "Requirements installed"
else
    echo "requirements.txt not found"
fi

# Deactivate the virtual environment
deactivate
