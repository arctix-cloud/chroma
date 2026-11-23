# Chroma

An interactive TUI terminal theme manager for **Termux**, featuring 27 curated color schemes and a real-time 24-bit Truecolor preview mode.

## Features
- **27 Built-in Themes**: Includes the custom *Arctix* AMOLED 2X series (*Dynamic Aero 2X*, *Pastel Aero*, *Nightshift Aero*), Linux classics (*Ubuntu*, *Dracula*, *Nord*, *Gruvbox*, *Catppuccin*, *Breeze*), and retro consoles.
- **Live 24-bit Truecolor Preview**: Press `Tab` anytime to toggle between the theme list and a live simulated terminal preview.
- **Wrap-around Scrolling**: Seamless navigation with `↑`/`↓` (or `j`/`k`) keys.
- **Instant Apply**: Automatically updates `~/.termux/colors.properties` and reloads Termux settings.

## Installation
```bash
git clone https://github.com/arctix-cloud/chroma.git
cd chroma
./install.sh
```

## Usage
Simply run `chroma` in your Termux terminal:
- `↑` / `↓` (or `k` / `j`): Navigate themes
- `Tab`: Toggle 24-bit Truecolor preview
- `Enter`: Apply selected theme
- `Esc` / `q`: Cancel and exit
