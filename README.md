# YouTube -> WAV Downloader

🇷🇴 [Română](#-română) · 🇬🇧 [English](#-english)

---

## 🇷🇴 Română

Aplicație desktop cu interfață grafică (Tkinter) care descarcă audio din
linkuri YouTube și îl salvează în format **WAV**, folosind
[yt-dlp](https://github.com/yt-dlp/yt-dlp). Testat pe **Linux** (Arch,
Pop!_OS) — scriptul de instalare acoperă și Ubuntu/Debian/Fedora.

> ⚠️ Folosește-l doar pentru conținut la care ai drepturi sau pentru uz
> personal. Descărcarea materialelor protejate prin drepturi de autor
> poate încălca Termenii de Serviciu ai YouTube.

### Instalare (recomandat)

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

### Instalare manuală (fără script)

```
sudo apt install python3-venv python3-tk ffmpeg   # Pop!_OS / Ubuntu / Debian
# sau: sudo pacman -S tk ffmpeg                    # Arch
# sau: sudo dnf install python3-tkinter ffmpeg     # Fedora

python3 -m venv venv
venv/bin/pip install --upgrade yt-dlp
venv/bin/python main.py
```

### Construirea unui executabil de sine stătător (opțional)

```
python3 -m venv build-env && build-env/bin/pip install yt-dlp pyinstaller
build-env/bin/pyinstaller --onefile --name YouTubeWavDownloader main.py
```

**Atenție la portabilitate:** binarul rezultat funcționează doar pe
mașini cu o versiune de `glibc` **egală sau mai nouă** decât cea de pe
calculatorul unde a fost construit (ex. un binar făcut pe Arch de multe
ori nu pornește pe Ubuntu mai vechi — eroare `GLIBC_2.XX not found`).
Pentru distribuire pe alt Linux e mai sigură **instalarea de mai sus**
cu `install_linux.sh`, care nu are această problemă.

### Structura proiectului

```
youtube-wav-downloader/
├── main.py            # aplicația (GUI + logica de descărcare)
├── install_linux.sh   # instalator automat pentru Linux (venv + meniu aplicații)
├── update.sh          # actualizează yt-dlp la ultima versiune
├── run.sh             # generat automat de install_linux.sh — pornește aplicația
├── icons/             # iconița aplicației
└── README.md          # acest fișier
```

---

## 🇬🇧 English

A desktop app with a graphical interface (Tkinter) that downloads audio
from YouTube links and saves it as **WAV**, using
[yt-dlp](https://github.com/yt-dlp/yt-dlp). Tested on **Linux** (Arch,
Pop!_OS) — the install script also covers Ubuntu/Debian/Fedora.

> ⚠️ Use it only for content you have the rights to, or for personal
> use. Downloading copyrighted material may violate YouTube's Terms of
> Service.

### Install (recommended)

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

### Manual install (without the script)

```
sudo apt install python3-venv python3-tk ffmpeg   # Pop!_OS / Ubuntu / Debian
# or: sudo pacman -S tk ffmpeg                     # Arch
# or: sudo dnf install python3-tkinter ffmpeg      # Fedora

python3 -m venv venv
venv/bin/pip install --upgrade yt-dlp
venv/bin/python main.py
```

### Building a standalone executable (optional)

```
python3 -m venv build-env && build-env/bin/pip install yt-dlp pyinstaller
build-env/bin/pyinstaller --onefile --name YouTubeWavDownloader main.py
```

**Portability note:** the resulting binary only runs on machines with a
`glibc` version equal to or newer than the build machine's (e.g. a
binary built on Arch often won't start on an older Ubuntu — a
`GLIBC_2.XX not found` error). For distributing to other Linux systems,
the **install above** using `install_linux.sh` is safer, since it
doesn't have this problem.

### Project structure

```
youtube-wav-downloader/
├── main.py            # the app (GUI + download logic)
├── install_linux.sh   # automatic Linux installer (venv + app menu entry)
├── update.sh          # updates yt-dlp to the latest version
├── run.sh             # auto-generated by install_linux.sh — launches the app
├── icons/             # the app icon
└── README.md          # this file
```
