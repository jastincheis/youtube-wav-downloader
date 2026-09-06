# YouTube -> WAV Downloader

🇷🇴 [Română](#-română) · 🇬🇧 [English](#-english)

---

## 🇷🇴 Română

Aplicație desktop cu interfață grafică (Tkinter) care descarcă audio din
linkuri YouTube și îl salvează în format **WAV**, folosind
[yt-dlp](https://github.com/yt-dlp/yt-dlp). Merge pe **Windows** și pe
**Linux** (Pop!_OS, Ubuntu, Debian, Fedora, Arch).

> ⚠️ Folosește-l doar pentru conținut la care ai drepturi sau pentru uz
> personal. Descărcarea materialelor protejate prin drepturi de autor
> poate încălca Termenii de Serviciu ai YouTube.

### Instalare pe Linux (recomandat)

Funcționează pe **Pop!_OS, Ubuntu, Debian, Fedora și Arch** — scriptul
detectează singur managerul de pachete (`apt`/`dnf`/`pacman`).

```
git clone https://github.com/jastincheis/youtube-wav-downloader.git
cd youtube-wav-downloader
chmod +x install_linux.sh
./install_linux.sh
```

Îți va cere parola de `sudo` o dată (ca să instaleze `python3-tk` și
`ffmpeg` dacă lipsesc). Restul — mediul virtual Python și `yt-dlp` — se
instalează izolat, fără să atingă sistemul. La final, aplicația apare în
meniul de aplicații ca **"YouTube WAV Downloader"**, sau o pornești
direct cu `./run.sh`.

Dacă la un moment dat descărcările încep să dea eroare (ex. `HTTP 403
Forbidden` — YouTube își schimbă des protecțiile), rulează `./update.sh`
ca să aduci ultima versiune de `yt-dlp`.

**Instalare manuală** (fără script):

```
sudo apt install python3-venv python3-tk ffmpeg   # Pop!_OS / Ubuntu / Debian
# sau: sudo pacman -S tk ffmpeg                    # Arch
# sau: sudo dnf install python3-tkinter ffmpeg     # Fedora

python3 -m venv venv
venv/bin/pip install --upgrade yt-dlp
venv/bin/python main.py
```

### Instalare pe Windows

Ai nevoie de Python 3.10+ (de pe [python.org](https://www.python.org/downloads/),
bifează "Add python.exe to PATH" la instalare).

```
pip install -r requirements.txt
python main.py
```

Se deschide fereastra: lipești linkurile (unul pe linie), alegi folderul
de destinație și apeși "Descarcă (WAV)".

**Executabil de sine stătător (opțional):**

```
pip install -r requirements.txt
pyinstaller --onefile --windowed --name YouTubeWavDownloader --collect-all imageio_ffmpeg main.py
```

Rezultatul apare în `dist\YouTubeWavDownloader.exe`. Fiindcă e un `.exe`
nesemnat digital, Windows Defender SmartScreen poate arăta un
avertisment la prima rulare — e un fals-pozitiv comun pentru
executabile PyInstaller ("More info" → "Run anyway").

Pe Linux, un binar echivalent se construiește cu
`pyinstaller --onefile --name YouTubeWavDownloader main.py`, dar
funcționează doar pe mașini cu `glibc` egal sau mai nou decât cel de pe
calculatorul unde a fost construit — pentru distribuire pe alt Linux e
mai sigur scriptul `install_linux.sh` de mai sus.

### Structura proiectului

```
youtube-wav-downloader/
├── main.py            # aplicația (GUI + logica de descărcare)
├── requirements.txt   # dependențe Python (pentru instalare manuală/Windows)
├── install_linux.sh   # instalator automat pentru Linux (venv + meniu aplicații)
├── update.sh          # actualizează yt-dlp la ultima versiune
├── run.sh             # generat automat de install_linux.sh — pornește aplicația
└── README.md          # acest fișier
```

---

## 🇬🇧 English

A desktop app with a graphical interface (Tkinter) that downloads audio
from YouTube links and saves it as **WAV**, using
[yt-dlp](https://github.com/yt-dlp/yt-dlp). Works on **Windows** and
**Linux** (Pop!_OS, Ubuntu, Debian, Fedora, Arch).

> ⚠️ Use it only for content you have the rights to, or for personal
> use. Downloading copyrighted material may violate YouTube's Terms of
> Service.

### Install on Linux (recommended)

Works on **Pop!_OS, Ubuntu, Debian, Fedora, and Arch** — the script
auto-detects your package manager (`apt`/`dnf`/`pacman`).

```
git clone https://github.com/jastincheis/youtube-wav-downloader.git
cd youtube-wav-downloader
chmod +x install_linux.sh
./install_linux.sh
```

It will ask for your `sudo` password once (to install `python3-tk` and
`ffmpeg` if missing). Everything else — the Python virtual environment
and `yt-dlp` — is installed in isolation, without touching your system.
Once done, the app appears in your application menu as **"YouTube WAV
Downloader"**, or you can launch it directly with `./run.sh`.

If downloads ever start failing (e.g. `HTTP 403 Forbidden` — YouTube
frequently changes its protections), run `./update.sh` to pull the
latest `yt-dlp`.

**Manual install** (without the script):

```
sudo apt install python3-venv python3-tk ffmpeg   # Pop!_OS / Ubuntu / Debian
# or: sudo pacman -S tk ffmpeg                     # Arch
# or: sudo dnf install python3-tkinter ffmpeg      # Fedora

python3 -m venv venv
venv/bin/pip install --upgrade yt-dlp
venv/bin/python main.py
```

### Install on Windows

You need Python 3.10+ (from [python.org](https://www.python.org/downloads/),
check "Add python.exe to PATH" during install).

```
pip install -r requirements.txt
python main.py
```

The window opens: paste your links (one per line), pick a destination
folder, and click "Descarcă (WAV)" (Download).

**Standalone executable (optional):**

```
pip install -r requirements.txt
pyinstaller --onefile --windowed --name YouTubeWavDownloader --collect-all imageio_ffmpeg main.py
```

The result lands in `dist\YouTubeWavDownloader.exe`. Since it's an
unsigned `.exe`, Windows Defender SmartScreen may show a warning on
first run — a common false positive for PyInstaller executables
("More info" → "Run anyway").

On Linux, an equivalent binary can be built with
`pyinstaller --onefile --name YouTubeWavDownloader main.py`, but it
only runs on machines with `glibc` equal to or newer than the build
machine's — for distributing to other Linux systems, the
`install_linux.sh` script above is the safer route.

### Project structure

```
youtube-wav-downloader/
├── main.py            # the app (GUI + download logic)
├── requirements.txt   # Python dependencies (manual install/Windows)
├── install_linux.sh   # automatic Linux installer (venv + app menu entry)
├── update.sh          # updates yt-dlp to the latest version
├── run.sh             # auto-generated by install_linux.sh — launches the app
└── README.md          # this file
```
