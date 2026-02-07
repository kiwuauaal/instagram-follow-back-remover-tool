#!/bin/bash

echo "========================================"
echo "Instagram Mutual-Follow Analyzer Setup"
echo "========================================"
echo

echo "Checking Python installation..."
if ! command -v python3 &> /dev/null; then
    echo "Python3 not found. Installing..."
    
    # Detect package manager
    if command -v apt &> /dev/null; then
        pkg install python
    elif command -v pacman &> /dev/null; then
        pacman -S python
    else
        echo "Please install Python manually"
        exit 1
    fi
fi

echo "Python found successfully!"
echo

echo "Installing/upgrading pip..."
python3 -m pip install --upgrade pip

echo
echo "Setup complete! You can now run:"
echo "python3 instagram_analyzer.py"
echo