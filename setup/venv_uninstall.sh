#!/bin/bash


# Define the name of the virtual environment directory
VENV_DIR=".venv"

# Function to ask for confirmation
confirm_deletion() {
    read -p "Are you sure you want to delete the virtual environment? (y/n): " -n 1 -r
    echo    # Move to a new line
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        # Confirmation received, proceed with deletion
        return 0
    else
        # Confirmation not received, do not delete
        return 1
    fi
}

# Check if the virtual environment directory exists
if [ -d "$VENV_DIR" ]; then
    echo "Virtual environment directory detected."

    # Ask for confirmation
    if confirm_deletion; then
        # Remove the virtual environment directory
        rm -rf $VENV_DIR
        echo "Virtual environment deleted."
    else
        echo "Deletion cancelled."
    fi
else
    echo "Virtual environment does not exist."
fi
