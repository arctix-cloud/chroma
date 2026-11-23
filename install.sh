#!/data/data/com.termux/files/usr/bin/bash
# Termux 환경에 chroma 및 자동 업데이트 별칭을 설치하는 스크립트임다

echo "Installing dependencies..."
pkg install -y python git > /dev/null 2>&1

echo "Installing chroma to $PREFIX/bin/chroma..."
cp chroma.py "$PREFIX/bin/chroma"
chmod +x "$PREFIX/bin/chroma"

# 쉘 설정 파일(~/.bashrc, ~/.zshrc) 자동 별칭 등록 로직임다
ALIAS_CMD="alias chroma-update='(cd ~/chroma && git pull && ./install.sh)'"

for RC in "$HOME/.bashrc" "$HOME/.zshrc"; do
    if [ -f "$RC" ] || [ "$(basename "$SHELL")" = "$(basename "${RC%.*}")" ]; then
        touch "$RC"
        if ! grep -q "chroma-update" "$RC"; then
            echo "" >> "$RC"
            echo "# Chroma auto-update shortcut" >> "$RC"
            echo "$ALIAS_CMD" >> "$RC"
            echo "Added 'chroma-update' alias to $(basename "$RC")."
        fi
    fi
done

echo ""
echo "Installation complete!"
echo "- Run 'chroma' to open theme manager."
echo "- Run 'chroma-update' anytime to pull the latest updates."
