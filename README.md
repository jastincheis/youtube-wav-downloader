# YouTube -> WAV Downloader

Program cu interfață grafică (Tkinter) care descarcă audio din linkuri
YouTube și îl salvează în format **WAV**, folosind [yt-dlp](https://github.com/yt-dlp/yt-dlp).
Merge pe **Windows** și pe **Linux** (testat pe Arch; scriptul de instalare
acoperă și Pop!_OS / Ubuntu / Debian / Fedora).

> ⚠️ Folosește-l doar pentru conținut la care ai drepturi sau pentru uz
> personal. Descărcarea materialelor protejate prin drepturi de autor
> poate încălca Termenii de Serviciu ai YouTube.

## 0. Instalare pe alt calculator Linux (recomandat)

Funcționează pe **Pop!_OS, Ubuntu, Debian, Fedora și Arch** — scriptul
detectează singur managerul de pachete (`apt`/`dnf`/`pacman`).

1. Copiază tot folderul `youtube-wav-downloader/` pe calculatorul nou
   (arhivă zip, USB, git — orice metodă).
2. Deschide un terminal în acel folder și rulează:
   ```
   chmod +x install_linux.sh
   ./install_linux.sh
   ```
3. Îți va cere parola de `sudo` o dată (ca să instaleze `python3-tk` și
   `ffmpeg` dacă lipsesc). Restul — mediul virtual Python și `yt-dlp` —
   se instalează izolat, fără să atingă sistemul.
4. La final, aplicația apare în meniul de aplicații ca **"YouTube WAV
   Downloader"**, sau o pornești direct cu `./run.sh`.

Dacă la un moment dat descărcările încep să dea eroare (ex. `HTTP 403
Forbidden` — YouTube își schimbă des protecțiile), rulează:
```
./update.sh
```
Asta aduce ultima versiune de `yt-dlp`, fără să reinstalezi nimic altceva.

## 1. Rulare manuală pe Linux (fără script)

Dacă preferi să faci pașii singur, în loc de `install_linux.sh`:

```
sudo apt install python3-venv python3-tk ffmpeg   # Pop!_OS / Ubuntu / Debian
# sau: sudo pacman -S tk ffmpeg                    # Arch
# sau: sudo dnf install python3-tkinter ffmpeg     # Fedora

python3 -m venv venv
venv/bin/pip install --upgrade yt-dlp
venv/bin/python main.py
```

## 2. Rulare pe Windows

Ai nevoie de Python 3.10+ (de pe [python.org](https://www.python.org/downloads/),
bifează "Add python.exe to PATH" la instalare).

```
pip install -r requirements.txt
python main.py
```

Se deschide fereastra: lipești linkurile (unul pe linie), alegi folderul
de destinație și apeși "Descarcă (WAV)".

## 3. Construirea unui executabil de sine stătător (opțional)

### Pe Windows

```
pip install -r requirements.txt
pyinstaller --onefile --windowed --name YouTubeWavDownloader --collect-all imageio_ffmpeg main.py
```

Rezultatul apare în `dist\YouTubeWavDownloader.exe` — îl poți muta/trimite
oriunde pe alt PC Windows (nu mai are nevoie de Python instalat).

### Pe Linux

```
python3 -m venv build-env && build-env/bin/pip install yt-dlp pyinstaller
build-env/bin/pyinstaller --onefile --name YouTubeWavDownloader main.py
```

**Atenție la portabilitate:** un binar Linux construit cu PyInstaller
funcționează doar pe mașini cu o versiune de `glibc` **egală sau mai
nouă** decât cea de pe calculatorul unde a fost construit. Un binar
făcut pe Arch (glibc foarte recent) de multe ori **nu pornește** pe
Pop!_OS/Ubuntu mai vechi (eroare gen `GLIBC_2.XX not found`). Din acest
motiv, pentru distribuire pe alt Linux e mai sigură **secțiunea 0**
(scriptul de instalare), nu acest binar.

### Notă despre antivirus / SmartScreen (Windows)

Fiindcă e un `.exe` nesemnat digital, e posibil ca Windows Defender
SmartScreen să arate un avertisment la prima rulare. E un fals-pozitiv
comun pentru executabile PyInstaller — apeși "More info" → "Run anyway".

## 4. Structura proiectului

```
youtube-wav-downloader/
├── main.py            # aplicația (GUI + logica de descărcare)
├── requirements.txt   # dependențe Python (pentru instalare manuală/Windows)
├── install_linux.sh   # instalator automat pentru Linux (venv + meniu aplicații)
├── update.sh          # actualizează yt-dlp la ultima versiune
├── run.sh             # generat automat de install_linux.sh — pornește aplicația
└── README.md          # acest fișier
```
