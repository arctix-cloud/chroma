#!/usr/bin/env python3
# Arctix 테마 라인업과 재정렬이 적용된 chroma 최신 소스코드임다

import os
import sys
import tty
import termios
import select
import shutil
import subprocess

# Termux 기본값 및 Arctix 최우선 정렬 테마 데이터베이스임다
THEMES = {
    "Termux (Default)": None,
    "Arctix Dynamic Aero 2X": """background=#000000
foreground=#f0f6fc
cursor=#00f5d4
color0=#1f2430
color1=#ff3366
color2=#00f676
color3=#ffb703
color4=#2979ff
color5=#d946ef
color6=#00e5ff
color7=#d8dee9
color8=#4b5563
color9=#ff6584
color10=#69f0ae
color11=#ffe169
color12=#70a9ff
color13=#f472b6
color14=#7df9ff
color15=#ffffff""",
    "Arctix Pastel Aero": """background=#000000
foreground=#dce2ec
cursor=#5eead4
color0=#1c2331
color1=#f07178
color2=#7bc876
color3=#e5c07b
color4=#6cb6ff
color5=#c792ea
color6=#56b6c2
color7=#c5cdd9
color8=#4f5b66
color9=#ff8b92
color10=#98e094
color11=#f5d58c
color12=#8ed0ff
color13=#ddb0ff
color14=#79e0ee
color15=#ffffff""",
    "Arctix Nightshift Aero": """background=#000000
foreground=#e8dec8
cursor=#f4a261
color0=#1f1c18
color1=#e86a70
color2=#7ec699
color3=#e5b567
color4=#689fb8
color5=#d484b5
color6=#5eb5a6
color7=#d5cbb8
color8=#5c5346
color9=#ff8589
color10=#a3e0b5
color11=#f7d08a
color12=#8ec2db
color13=#eb9fd0
color14=#80d6c7
color15=#f5efe6""",
    "Ubuntu": """background=#300a24
foreground=#ffffff
cursor=#bbbbbb
color0=#2e3436
color1=#cc0000
color2=#4e9a06
color3=#c4a000
color4=#3465a4
color5=#75507b
color6=#06989a
color7=#d3d7cf
color8=#555753
color9=#ef2929
color10=#8ae234
color11=#fce94f
color12=#729fcf
color13=#ad7fa8
color14=#34e2e2
color15=#eeeeec""",
    "Dracula": """background=#282a36
foreground=#f8f8f2
cursor=#f8f8f2
color0=#21222c
color1=#ff5555
color2=#50fa7b
color3=#f1fa8c
color4=#bd93f9
color5=#ff79c6
color6=#8be9fd
color7=#f8f8f2
color8=#6272a4
color9=#ff6e6e
color10=#69ff94
color11=#ffffa5
color12=#d6acff
color13=#ff92df
color14=#a4ffff
color15=#ffffff""",
    "Nord": """background=#2e3440
foreground=#d8dee9
cursor=#d8dee9
color0=#3b4252
color1=#bf616a
color2=#a3be8c
color3=#ebcb8b
color4=#81a1c1
color5=#b48ead
color6=#88c0d0
color7=#e5e9f0
color8=#4c566a
color9=#bf616a
color10=#a3be8c
color11=#ebcb8b
color12=#81a1c1
color13=#b48ead
color14=#8fbcbb
color15=#eceff4""",
    "Gruvbox Dark": """background=#282828
foreground=#ebdbb2
cursor=#ebdbb2
color0=#282828
color1=#cc241d
color2=#98971a
color3=#d79921
color4=#458588
color5=#b16286
color6=#689d6a
color7=#a89984
color8=#928374
color9=#fb4934
color10=#b8bb26
color11=#fabd2f
color12=#83a598
color13=#d3869b
color14=#8ec07c
color15=#ebdbb2""",
    "Catppuccin Mocha": """background=#1e1e2e
foreground=#cdd6f4
cursor=#f5e0dc
color0=#45475a
color1=#f38ba8
color2=#a6e3a1
color3=#f9e2af
color4=#89b4fa
color5=#f5c2e7
color6=#94e2d5
color7=#bac2de
color8=#585b70
color9=#f38ba8
color10=#a6e3a1
color11=#f9e2af
color12=#89b4fa
color13=#f5c2e7
color14=#94e2d5
color15=#a6adc8""",
    "Breeze (KDE)": """background=#232629
foreground=#eff0f1
cursor=#eff0f1
color0=#232629
color1=#ed1515
color2=#11d116
color3=#f67400
color4=#1d99f3
color5=#9b59b6
color6=#1abc9c
color7=#fcfcfc
color8=#7f8c8d
color9=#c0392b
color10=#27ae60
color11=#f39c1f
color12=#2980b9
color13=#8e44ad
color14=#16a085
color15=#ffffff""",
    "Tokyo Night": """background=#1a1b26
foreground=#a9b1d6
cursor=#c0caf5
color0=#32344a
color1=#f7768e
color2=#9ece6a
color3=#e0af68
color4=#7aa2f7
color5=#ad8ee6
color6=#444b6a
color7=#787c99
color8=#444b6a
color9=#ff7a93
color10=#b9f27c
color11=#ff9e64
color12=#7da6ff
color13=#bb9af7
color14=#0db9d7
color15=#acb0be""",
    "One Half Dark": """background=#282c34
foreground=#dcdfe4
cursor=#a3b3cc
color0=#282c34
color1=#e06c75
color2=#98c379
color3=#e5c07b
color4=#61afef
color5=#c678dd
color6=#56b6c2
color7=#dcdfe4
color8=#5c6370
color9=#e06c75
color10=#98c379
color11=#e5c07b
color12=#61afef
color13=#c678dd
color14=#56b6c2
color15=#eceff4""",
    "One Half Light": """background=#fafafa
foreground=#383a42
cursor=#4f525d
color0=#383a42
color1=#e45649
color2=#50a14f
color3=#c18401
color4=#4078f2
color5=#a626a4
color6=#0184bc
color7=#a0a1a7
color8=#4f525d
color9=#df6c75
color10=#98c379
color11=#e5c07b
color12=#61afef
color13=#c678dd
color14=#56b6c2
color15=#ffffff""",
    "Solarized Dark": """background=#002b36
foreground=#839496
cursor=#93a1a1
color0=#073642
color1=#dc322f
color2=#859900
color3=#b58900
color4=#268bd2
color5=#d33682
color6=#2aa198
color7=#eee8d5
color8=#002b36
color9=#cb4b16
color10=#586e75
color11=#657b83
color12=#839496
color13=#6c71c4
color14=#93a1a1
color15=#fdf6e3""",
    "Solarized Light": """background=#fdf6e3
foreground=#657b83
cursor=#586e75
color0=#073642
color1=#dc322f
color2=#859900
color3=#b58900
color4=#268bd2
color5=#d33682
color6=#2aa198
color7=#eee8d5
color8=#002b36
color9=#cb4b16
color10=#586e75
color11=#657b83
color12=#839496
color13=#6c71c4
color14=#93a1a1
color15=#fdf6e3""",
    "Tango Dark": """background=#2e3436
foreground=#d3d7cf
cursor=#ffffff
color0=#2e3436
color1=#cc0000
color2=#4e9a06
color3=#c4a000
color4=#3465a4
color5=#75507b
color6=#06989a
color7=#d3d7cf
color8=#555753
color9=#ef2929
color10=#8ae234
color11=#fce94f
color12=#729fcf
color13=#ad7fa8
color14=#34e2e2
color15=#eeeeec""",
    "Tango Light": """background=#ffffff
foreground=#2e3436
cursor=#000000
color0=#2e3436
color1=#cc0000
color2=#4e9a06
color3=#c4a000
color4=#3465a4
color5=#75507b
color6=#06989a
color7=#d3d7cf
color8=#555753
color9=#ef2929
color10=#8ae234
color11=#fce94f
color12=#729fcf
color13=#ad7fa8
color14=#34e2e2
color15=#eeeeec""",
    "Dark+": """background=#1e1e1e
foreground=#cccccc
cursor=#ffffff
color0=#000000
color1=#cd3131
color2=#0dbc79
color3=#e5e510
color4=#2472c8
color5=#bc3fbc
color6=#11a8cd
color7=#e5e5e5
color8=#666666
color9=#f14c4c
color10=#23d18b
color11=#f5f543
color12=#3b8eea
color13=#d670d6
color14=#29b8db
color15=#e5e5e5""",
    "Campbell": """background=#0c0c0c
foreground=#cccccc
cursor=#ffffff
color0=#0c0c0c
color1=#c50f1f
color2=#13a10e
color3=#c19c00
color4=#0037da
color5=#881798
color6=#3a96dd
color7=#cccccc
color8=#767676
color9=#e74856
color10=#16c60c
color11=#f9f1a5
color12=#3b78ff
color13=#b4009e
color14=#61d6d6
color15=#f2f2f2""",
    "Campbell Powershell": """background=#012456
foreground=#cccccc
cursor=#ffffff
color0=#0c0c0c
color1=#c50f1f
color2=#13a10e
color3=#c19c00
color4=#0037da
color5=#881798
color6=#3a96dd
color7=#cccccc
color8=#767676
color9=#e74856
color10=#16c60c
color11=#f9f1a5
color12=#3b78ff
color13=#b4009e
color14=#61d6d6
color15=#f2f2f2""",
    "Vintage": """background=#000000
foreground=#c0c0c0
cursor=#ffffff
color0=#000000
color1=#800000
color2=#008000
color3=#808000
color4=#000080
color5=#800080
color6=#008080
color7=#c0c0c0
color8=#808080
color9=#ff0000
color10=#00ff00
color11=#ffff00
color12=#0000ff
color13=#ff00ff
color14=#00ffff
color15=#ffffff""",
    "CGA": """background=#000000
foreground=#aaaaaa
cursor=#ffffff
color0=#000000
color1=#aa0000
color2=#00aa00
color3=#aa5500
color4=#0000aa
color5=#aa00aa
color6=#00aaaa
color7=#aaaaaa
color8=#555555
color9=#ff5555
color10=#55ff55
color11=#ffff55
color12=#5555ff
color13=#ff55ff
color14=#55ffff
color15=#ffffff""",
    "IBM 5153": """background=#000000
foreground=#aaaaaa
cursor=#ffffff
color0=#000000
color1=#aa0000
color2=#00aa00
color3=#aa5500
color4=#0000aa
color5=#aa00aa
color6=#00aaaa
color7=#aaaaaa
color8=#555555
color9=#ff5555
color10=#55ff55
color11=#ffff55
color12=#5555ff
color13=#ff55ff
color14=#55ffff
color15=#ffffff""",
    "Dimidium": """background=#222222
foreground=#bbbbbb
cursor=#ffffff
color0=#222222
color1=#aa3333
color2=#33aa33
color3=#aaaa33
color4=#3333aa
color5=#aa33aa
color6=#33aaaa
color7=#bbbbbb
color8=#444444
color9=#ee4444
color10=#44ee44
color11=#eeee44
color12=#4444ee
color13=#ee44ee
color14=#44eeee
color15=#ffffff""",
    "Ottosson": """background=#161819
foreground=#e1e1e1
cursor=#ffffff
color0=#161819
color1=#e0534d
color2=#4ebb6f
color3=#d8a635
color4=#4997e5
color5=#be6ce5
color6=#34b6b6
color7=#e1e1e1
color8=#545b61
color9=#f1706b
color10=#67d487
color11=#f0be4d
color12=#68aff5
color13=#d38bf5
color14=#53d4d4
color15=#ffffff""",
    "Colorblind-friendly Dark": """background=#1a1a1a
foreground=#ffffff
cursor=#e69f00
color0=#1a1a1a
color1=#d55e00
color2=#009e73
color3=#f0e442
color4=#0072b2
color5=#cc79a7
color6=#56b4e9
color7=#f0f0f0
color8=#666666
color9=#e69f00
color10=#56b4e9
color11=#009e73
color12=#f0e442
color13=#0072b2
color14=#d55e00
color15=#ffffff""",
    "Colorblind-friendly Light": """background=#ffffff
foreground=#000000
cursor=#0072b2
color0=#000000
color1=#d55e00
color2=#009e73
color3=#f0e442
color4=#0072b2
color5=#cc79a7
color6=#56b4e9
color7=#999999
color8=#666666
color9=#e69f00
color10=#56b4e9
color11=#009e73
color12=#f0e442
color13=#0072b2
color14=#d55e00
color15=#ffffff"""
}

# 16진수 색상 코드를 정수형 RGB 튜플로 파싱하는 함수임다
def parse_hex(hex_str):
    h = hex_str.strip().lstrip('#')
    if len(h) != 6:
        return (200, 200, 200)
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))

# 프로퍼티 설정을 딕셔너리 구조로 파싱하는 함수임다
def get_theme_dict(raw_str):
    if raw_str is None:
        raw_str = """background=#000000
foreground=#ffffff
cursor=#ffffff
color0=#000000
color1=#cd0000
color2=#00cd00
color3=#cdcd00
color4=#0000ee
color5=#cd00cd
color6=#00cdcd
color7=#e5e5e5
color8=#7f7f7f
color9=#ff0000
color10=#00ff00
color11=#ffff00
color12=#5c5cff
color13=#ff00ff
color14=#00ffff
color15=#ffffff"""
    d = {}
    for line in raw_str.strip().splitlines():
        if '=' in line and not line.startswith('#'):
            k, v = line.split('=', 1)
            d[k.strip()] = v.strip()
    return d

# 선택한 테마를 Termux 설정에 기록하고 리로드하는 함수임다
def apply_theme(name):
    target = os.path.expanduser("~/.termux/colors.properties")
    val = THEMES.get(name)
    if val is None:
        if os.path.exists(target):
            os.remove(target)
    else:
        os.makedirs(os.path.dirname(target), exist_ok=True)
        with open(target, "w", encoding="utf-8") as f:
            f.write(val + "\n")
    subprocess.run(["termux-reload-settings"], check=False)

# 커널 레벨에서 원시 패킷을 즉시 수신하는 키 파서임다
def get_raw_key(fd):
    select.select([fd], [], [])
    raw = os.read(fd, 32)
    if not raw:
        return 'IGNORE'

    if raw == b'\x1b':
        if select.select([fd], [], [], 0.05)[0]:
            raw += os.read(fd, 32)
        else:
            return 'ESC'

    if raw in (b'\x1b[A', b'\x1bOA') or (raw.startswith(b'\x1b') and raw.endswith(b'A')):
        return 'UP'
    elif raw in (b'\x1b[B', b'\x1bOB') or (raw.startswith(b'\x1b') and raw.endswith(b'B')):
        return 'DOWN'
    elif raw in (b'\t', b'\x1b[Z'):
        return 'TAB'
    elif raw in (b'\r', b'\n'):
        return 'ENTER'
    elif raw in (b'q', b'Q'):
        return 'QUIT'
    elif raw in (b'k', b'K'):
        return 'UP'
    elif raw in (b'j', b'J'):
        return 'DOWN'

    return 'IGNORE'

# TUI 렌더링 루프를 구동하는 메인 함수임다
def main():
    names = list(THEMES.keys())
    idx = 0
    top_offset = 0
    show_demo = False

    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    tty.setcbreak(fd)
    sys.stdout.write("\033[?25l")
    sys.stdout.flush()

    try:
        while True:
            cols, rows = shutil.get_terminal_size((80, 24))
            curr_name = names[idx]
            c_dict = get_theme_dict(THEMES[curr_name])

            out = ["\033[H\033[2J"]

            if not show_demo:
                title = "=== Chroma Theme Manager ==="
                guide = "[Tab] Preview Toggle  |  [Up/Down] Navigate  |  [Enter] Apply  |  [q] Quit"
                out.append(f"\033[1;36m{title[:cols]}\033[0m\r\n")
                out.append(f"\033[33m{guide[:cols]}\033[0m\r\n\r\n")

                list_capacity = max(3, rows - 5)
                if idx < top_offset:
                    top_offset = idx
                elif idx >= top_offset + list_capacity:
                    top_offset = idx - list_capacity + 1

                for i in range(list_capacity):
                    cur_item_idx = top_offset + i
                    if cur_item_idx >= len(names):
                        break
                    tname = names[cur_item_idx]
                    if cur_item_idx == idx:
                        out.append(f"\033[7;1;32m > {tname:<{cols-4}} \033[0m\r\n")
                    else:
                        out.append(f"   {tname[:cols-4]}\r\n")

                stat = f"[{idx + 1}/{len(names)}] - Press Tab to toggle Truecolor preview"
                out.append(f"\r\n\033[2m{stat[:cols]}\033[0m")
            else:
                bg_r, bg_g, bg_b = parse_hex(c_dict.get('background', '#000000'))
                fg_r, fg_g, fg_b = parse_hex(c_dict.get('foreground', '#ffffff'))

                header = f"=== [PREVIEW] : {curr_name} ==="
                guide = "[Tab] Back to List  |  [Up/Down] Switch Theme  |  [Enter] Apply  |  [q] Quit"
                out.append(f"\033[1;35m{header[:cols]}\033[0m\r\n")
                out.append(f"\033[33m{guide[:cols]}\033[0m\r\n\r\n")

                out.append("Palette 0-7  : ")
                for i in range(8):
                    r, g, b = parse_hex(c_dict.get(f'color{i}', '#888888'))
                    out.append(f"\033[48;2;{r};{g};{b}m  \033[0m ")
                out.append("\r\nPalette 8-15 : ")
                for i in range(8, 16):
                    r, g, b = parse_hex(c_dict.get(f'color{i}', '#888888'))
                    out.append(f"\033[48;2;{r};{g};{b}m  \033[0m ")
                out.append("\r\n\r\n")

                def fg(c_idx):
                    r, g, b = parse_hex(c_dict.get(f'color{c_idx}', '#ffffff'))
                    return f"\033[38;2;{r};{g};{b}m"

                t_bg = f"\033[48;2;{bg_r};{bg_g};{bg_b}m"
                t_fg = f"\033[38;2;{fg_r};{fg_g};{fg_b}m"

                pad_w = max(20, cols - 4)
                def box_line(content):
                    return f"  {t_bg}{content:<{pad_w}}\033[0m\r\n"

                out.append("--- Terminal Preview Window ---\r\n")
                out.append(box_line(f"{fg(2)}user@termux{t_fg}:{fg(4)}~/chroma{t_fg}$ uname -a"))
                out.append(box_line(f"{t_fg}Linux termux 6.1.0-arm64 #1 SMP PREEMPT Android"))
                out.append(box_line(f"{fg(2)}user@termux{t_fg}:{fg(4)}~/chroma{t_fg}$ git status"))
                if "Arctix" in curr_name:
                    s_msg = "Arctix AMOLED 2X Series - Pure Black"
                elif "Termux" in curr_name:
                    s_msg = "Termux Vanilla Default Series"
                elif curr_name in ("Ubuntu", "Dracula", "Nord", "Gruvbox Dark", "Catppuccin Mocha", "Breeze (KDE)"):
                    s_msg = "Linux Heritage Series - Classic Desktop"
                elif curr_name in ("Tokyo Night", "One Half Dark", "One Half Light", "Dark+"):
                    s_msg = "Modern Editor & IDE Series"
                elif curr_name in ("Solarized Dark", "Solarized Light", "Tango Dark", "Tango Light"):
                    s_msg = "UNIX Terminal Classic Series"
                elif "Colorblind" in curr_name:
                    s_msg = "Accessibility Colorblind-Friendly Series"
                else:
                    s_msg = "Retro & PC Console Heritage Series"
                out.append(box_line(f"{fg(3)}On branch main - {s_msg}"))
                out.append(box_line(f"{fg(1)}[ALERT]  {fg(5)}Virtualization KVM Module Loaded{t_fg}"))
                out.append(box_line(f"{fg(6)}[STATUS] {fg(10)}All checks passed (24-bit Truecolor OK){t_fg}"))
                out.append(box_line(f"{fg(2)}user@termux{t_fg}:{fg(4)}~/chroma{t_fg}$ \033[7m \033[0m"))
                out.append("-------------------------------\r\n")

            sys.stdout.write("".join(out))
            sys.stdout.flush()

            while True:
                k = get_raw_key(fd)
                if k == 'IGNORE':
                    continue
                break

            if k == 'TAB':
                show_demo = not show_demo
            elif k == 'UP':
                idx = (idx - 1) % len(names)
            elif k == 'DOWN':
                idx = (idx + 1) % len(names)
            elif k == 'ENTER':
                chosen = names[idx]
                apply_theme(chosen)
                return chosen
            elif k in ('ESC', 'QUIT'):
                return None

    finally:
        sys.stdout.write("\033[?25h\033[0m\033[H\033[2J")
        sys.stdout.flush()
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

if __name__ == "__main__":
    try:
        res = main()
        if res:
            print(f"Theme successfully applied: {res}")
        else:
            print("Selection cancelled.")
    except KeyboardInterrupt:
        print("\nOperation aborted.")
