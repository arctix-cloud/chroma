#!/data/data/com.termux/files/usr/bin/bash
# Chroma installer: deploys binary and configures shell shortcuts

echo "Installing dependencies..."
pkg install -y python git > /dev/null 2>&1

echo "Installing chroma to $PREFIX/bin/chroma..."
cp chroma.py "$PREFIX/bin/chroma"
chmod +x "$PREFIX/bin/chroma"

# Register auto-update alias across available shell configurations
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
