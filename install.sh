#!/data/data/com.termux/files/usr/bin/bash
# Termux 환경에 chroma를 설치하는 스크립트임다

echo "Installing dependencies..."
pkg install -y python

echo "Installing chroma to $PREFIX/bin/chroma..."
cp chroma.py "$PREFIX/bin/chroma"
chmod +x "$PREFIX/bin/chroma"

echo "Installation complete! Run 'chroma' anywhere."
