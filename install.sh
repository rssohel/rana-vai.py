#!/bin/bash
pkg update && pkg upgrade -y
pkg install python curl -y
pip install colorama
echo "Setup Complete. Now run: python rana-vai.py"
