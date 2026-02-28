#!/bin/bash
echo "Setting up RANA.Nj System..."
pkg update && pkg upgrade -y
pkg install python -y
pip install colorama
echo "Installation Complete!"
echo "Now run the tool using: python rana-vai.py"
