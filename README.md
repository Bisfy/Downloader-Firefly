Downloader "Firefly"

A versatile CLI Downloader with an ASCII-style terminal interface. Built with Python, this tool allows you to seamlessly download videos and audio from various platforms such as YouTube, TikTok, Instagram, and X.

 Key Features
- Multi-Platform Support:** Download from hundreds of sites supported by `yt-dlp`.
- Smart Format Selection:** Automatically merge high-quality video/audio into `.mp4`, or extract pure audio to `.mp3`.
- Auto-Setup Engine:** The program automatically downloads the latest version of `yt-dlp` and offers a multi-OS `FFmpeg` installation prompt (Windows, macOS, Linux).
- Portable (.exe):** Available as a standalone executable for Windows, 100% plug-and-play with no Python installation required.
- Bypass Limits:** Utilizes a Deno runtime workaround to bypass YouTube's download speed throttling.

Usage (End-User)
1. Visit the [Releases](https://github.com/Bisfy/Downloader-Firefly/releases) page.
2. Download the `downloader.exe` file from the latest release.
3. Place it in any folder and double-click the file.
4. The program will automatically download the required engine components (`bin/`) and create a `Downloads/` folder.
5. Enter the link/URL and choose your preferred download format.

Running from Source (Developer)
If you wish to modify or run the tool directly from the source code:

1. Clone this repository:
   ```bash
   git clone [https://github.com/Bisfy/Downloader-Firefly.git](https://github.com/Bisfy/Downloader-Firefly.git)
   cd Downloader-Firefly

2. Run the main script (Pillow will be installed automatically if not present):
   ```bash
   python Downloader.py

======================================================================================

Tech Stack & Dependencies
Language: Python 3.x

Core Engine: yt-dlp

Media Processing: FFmpeg

Image/ASCII Rendering: Pillow (PIL)

======================================================================================

== License ==
This project is licensed under the MIT License. You are free to use, modify, and distribute this software, provided that proper credit is given to the original author.
