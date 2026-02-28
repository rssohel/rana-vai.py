#!/bin/bash

echo "Installing requirements..."

pkg update -y
pkg install python -y
pip install -r requirements.txt

echo "Installation Complete!"
