---

### ২/ `install.sh` ফাইলে যা লিখবেন:
এটি আপনার বন্ধুর ফোনে সব প্রয়োজনীয় সফটওয়্যার অটোমেটিক সেটআপ করবে।

```bash
#!/bin/bash
echo "Setting up RANA.Nj System..."
pkg update && pkg upgrade -y
pkg install python -y
pip install colorama
echo "Installation Complete! Now run the tool using: python rana-vai.py"
