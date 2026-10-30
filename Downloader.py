import os
import sys
import subprocess
import platform
import shutil
import urllib.request

try:
    from PIL import Image, ImageEnhance
except ImportError:
    print("System checking... Pillow not found.")
    print("Installing Pillow...\n")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "Pillow"])
        from PIL import Image, ImageEnhance
    except Exception as e:
        print(f"Error installing Pillow: {e}")
        sys.exit(1)

BASE_DIR = os.path.dirname(os.path.abspath(sys.argv[0]))
DOWNLOAD_FOLDER = os.path.join(BASE_DIR, "Downloads")
BIN_DIR = os.path.join(BASE_DIR, "bin") 

os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)
os.makedirs(BIN_DIR, exist_ok=True)

OS_NAME = platform.system()
EXE_EXT = ".exe" if OS_NAME == "Windows" else ""
YTDLP_BIN = os.path.join(BIN_DIR, f"yt-dlp{EXE_EXT}")

def get_resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), relative_path)

IMAGE_PATH = get_resource_path("logo.jpg")

def setup_engine():
    if not os.path.exists(YTDLP_BIN):
        print(f"\n\033[93m[*] yt-dlp engine not found in folder 'bin/'.\033[0m")
        print("\033[96m[*] Downloading...\033[0m")
        
        if OS_NAME == "Windows":
            url = "https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp.exe"
        elif OS_NAME == "Darwin": # macOS
            url = "https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp_macos"
        else: # Linux
            url = "https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp"

        try:
            urllib.request.urlretrieve(url, YTDLP_BIN)
            if OS_NAME != "Windows":
                os.chmod(YTDLP_BIN, 0o755)
            print("\033[92m[*] Success\033[0m\n")
        except Exception as e:
            print(f"\033[91m[!] Error : {e}\033[0m")
            sys.exit(1)
    else:
        print("\033[96m[*] Checking...\033[0m")
        subprocess.run([YTDLP_BIN, "-U"], check=False)

def setup_ffmpeg():
    if shutil.which("ffmpeg") or os.path.exists(os.path.join(BIN_DIR, f"ffmpeg{EXE_EXT}")):
        return True

    print("\n\033[93m[!] FFmpeg not found in folder 'bin/'.\033[0m")
    pilihan = input("\033[96m[?] Do you want to install it now? (y/n): \033[0m").strip().lower()
    
    if pilihan != 'y':
        print("\033[91m[!] Hmm, okay, but if it fails, don't be angry, okay? \033[0m")
        return False

    print(f"\n\033[92m[*] OS: {OS_NAME}. Starting...\033[0m")
    try:
        if OS_NAME == "Windows":
            subprocess.run(["winget", "install", "Gyan.FFmpeg", "-e", "--accept-source-agreements", "--accept-package-agreements"], check=True)
        elif OS_NAME == "Darwin":
            if not shutil.which("brew"): return False
            subprocess.run(["brew", "install", "ffmpeg"], check=True)
        elif OS_NAME == "Linux":
            if shutil.which("apt"):
                subprocess.run(["sudo", "apt", "update"], check=True)
                subprocess.run(["sudo", "apt", "install", "-y", "ffmpeg"], check=True)
            elif shutil.which("pacman"):
                subprocess.run(["sudo", "pacman", "-S", "--noconfirm", "ffmpeg"], check=True)
        return True
    except:
        return False

LEBAR_ASCII = 45 
ASCII_CHARS = [" ", ".", ",", ":", ";", "+", "*", "?", "%", "$", "#", "@"]

CYAN = "\033[38;2;100;255;218m"    
ORANGE = "\033[38;2;255;140;100m"  
WHITE = "\033[97m"                
RESET = "\033[0m"

def render_local_ascii(image_path, width=50):
    if not os.path.exists(image_path):
        return []
    try:
        img = Image.open(image_path)
        w, h = img.size
        aspect_ratio = h / w
        height = max(1, int(width * aspect_ratio * 0.45))
        img = img.resize((width, height), Image.Resampling.LANCZOS).convert("RGB")
        enhancer = ImageEnhance.Contrast(img)
        img = enhancer.enhance(1.2) 

        ascii_lines = []
        for y in range(height):
            line = ""
            for x in range(width):
                r, g, b = img.getpixel((x, y))
                brightness = int(0.299 * r + 0.587 * g + 0.114 * b)
                if brightness < 35: 
                    line += " "
                else:
                    char = ASCII_CHARS[int((brightness / 255) * (len(ASCII_CHARS) - 1))]
                    line += f"\033[38;2;{r};{g};{b}m{char}"
            line += "\033[0m"
            ascii_lines.append(line)
        return ascii_lines
    except:
        return []

def download_video():
    os.system('cls' if os.name == 'nt' else 'clear') 
    ascii_lines = render_local_ascii(IMAGE_PATH, LEBAR_ASCII)
    ui_lines = [
        f"{CYAN}╔════════════════════════════╗{RESET}",
        f"{CYAN}║ {WHITE}  ✦ DOWNLOADER ✦           {CYAN}║{RESET}",
        f"{CYAN}║ {WHITE}                           {CYAN}║{RESET}",
        f"{CYAN}╠════════════════════════════╣{RESET}",
        f"{CYAN}║ {ORANGE}▶{RESET} {WHITE}YouTube                  {CYAN}║{RESET}",
        f"{CYAN}║ {ORANGE}▶{RESET} {WHITE}Instagram                {CYAN}║{RESET}",
        f"{CYAN}║ {ORANGE}▶{RESET} {WHITE}TikTok                   {CYAN}║{RESET}",
        f"{CYAN}╠════════════════════════════╣{RESET}",
        f"{CYAN}║ {WHITE}\"I dream of a world where  {CYAN}║{RESET}",
        f"{CYAN}║ {WHITE} we can live together.\"    {CYAN}║{RESET}",
        f"{CYAN}╚════════════════════════════╝{RESET}",
        "",
        f"   {ORANGE}[!]{RESET} To exit type : {WHITE}'exit'{RESET}",
        ""
    ]

    if len(ascii_lines) > len(ui_lines):
        offset = (len(ascii_lines) - len(ui_lines)) // 2
        ui_lines = [""] * offset + ui_lines
    elif len(ui_lines) > len(ascii_lines):
        offset = (len(ui_lines) - len(ascii_lines)) // 2
        ascii_lines = [""] * offset + ascii_lines

    max_lines = max(len(ascii_lines), len(ui_lines))
    print("\n") 
    for i in range(max_lines):
        left_ui = ui_lines[i] if i < len(ui_lines) else " " * 30
        right_ascii = ascii_lines[i] if i < len(ascii_lines) else " " * LEBAR_ASCII
        print(f"{left_ui}      {right_ascii}")
    print("\n")
    
    url = input(f"{ORANGE}➤ {WHITE}enter the link : {RESET}")
    if url.lower() == 'exit': sys.exit()

    print(f"\n{ORANGE}Select a format : {RESET}")
    print(f"  {WHITE}[1]{RESET} Video (.mp4)")
    print(f"  {WHITE}[2]{RESET} Audio (.mp3)")
    pilihan = input(f"{ORANGE}➤ {WHITE}choose (1/2, default 1): {RESET}").strip()

    cmd = [
        YTDLP_BIN, url, 
        '-o', os.path.join(DOWNLOAD_FOLDER, '%(title)s.%(ext)s'),
        '--extractor-args', 'youtube:js_runtimes=deno'
    ]

    if pilihan == '2':
        print(f"\n{CYAN}[*] Mode: Audio MP3{RESET}")
        cmd.extend(['-x', '--audio-format', 'mp3', '--audio-quality', '192'])
    else:
        print(f"\n{CYAN}[*] Mode: Video MP4{RESET}")
        cmd.extend(['-f', 'bv*+ba/b', '--merge-output-format', 'mp4'])

    print(f"{CYAN}[*] Start downloading....{RESET}\n")
    try:
        subprocess.run(cmd, check=True)
        print(f"\n{CYAN}[*] Finished check 'Downloads'.{RESET}")
    except subprocess.CalledProcessError:
        print(f"\n{ORANGE}[!] Error{RESET}")
    
    input(f"\n{WHITE}Press Enter to continue...{RESET}")


if __name__ == "__main__":
    try:
        setup_engine()
        setup_ffmpeg()
        while True:
            download_video()
    except KeyboardInterrupt:
        print(f"\n\n{CYAN}✦ See you, have a nice day.. ✦{RESET}\n")
        sys.exit(0)