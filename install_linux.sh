#!/usr/bin/env bash
# Instalator pentru YouTube -> WAV Downloader pe Linux (Pop!_OS, Ubuntu,
# Debian, Fedora, Arch). Creeaza un mediu virtual Python izolat, instaleaza
# dependentele de sistem necesare si adauga aplicatia in meniul de aplicatii.
set -e

APP_NAME="YouTube WAV Downloader"
APP_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VENV_DIR="$APP_DIR/venv"
LAUNCHER="$APP_DIR/run.sh"
DESKTOP_FILE="$HOME/.local/share/applications/youtube-wav-downloader.desktop"

echo "== Instalare: $APP_NAME =="
echo "Folder aplicatie: $APP_DIR"
echo ""

install_system_deps() {
    if command -v apt >/dev/null 2>&1; then
        echo "-> Detectat apt (Pop!_OS / Ubuntu / Debian)."
        echo "   Instalez: python3-venv, python3-tk, ffmpeg"
        sudo apt update
        sudo apt install -y python3-venv python3-tk ffmpeg
    elif command -v pacman >/dev/null 2>&1; then
        echo "-> Detectat pacman (Arch)."
        echo "   Instalez: tk, ffmpeg"
        sudo pacman -S --needed --noconfirm tk ffmpeg
    elif command -v dnf >/dev/null 2>&1; then
        echo "-> Detectat dnf (Fedora)."
        echo "   Instalez: python3-tkinter, ffmpeg"
        sudo dnf install -y python3-tkinter ffmpeg
    else
        echo "!! Nu am recunoscut managerul de pachete (apt/pacman/dnf)."
        echo "   Instaleaza manual echivalentul pentru: python3-venv, python3-tk (tkinter), ffmpeg"
        echo "   apoi ruleaza din nou acest script."
        exit 1
    fi
}

install_system_deps

echo ""
echo "-> Creez mediul virtual Python in: $VENV_DIR"
python3 -m venv "$VENV_DIR"
"$VENV_DIR/bin/pip" install --upgrade pip -q

echo "-> Instalez yt-dlp (ultima versiune de pe PyPI)"
"$VENV_DIR/bin/pip" install --upgrade yt-dlp -q

echo "-> Creez scriptul de pornire: $LAUNCHER"
cat > "$LAUNCHER" <<EOF
#!/usr/bin/env bash
cd "$APP_DIR"
exec "$VENV_DIR/bin/python" "$APP_DIR/main.py"
EOF
chmod +x "$LAUNCHER"

echo "-> Adaug aplicatia in meniul de aplicatii"
mkdir -p "$(dirname "$DESKTOP_FILE")"
cat > "$DESKTOP_FILE" <<EOF
[Desktop Entry]
Type=Application
Name=$APP_NAME
Comment=Descarca audio de pe YouTube in format WAV
Exec=$LAUNCHER
Icon=$APP_DIR/icons/youtube-wav-downloader.png
Terminal=false
Categories=AudioVideo;Utility;
EOF

echo ""
echo "== Instalare terminata =="
echo "Poti porni aplicatia:"
echo "  - din meniul de aplicatii al sistemului, cautand \"$APP_NAME\""
echo "  - sau direct din terminal cu: $LAUNCHER"
echo ""
echo "Daca peste timp apar erori de tip \"HTTP 403 Forbidden\" (YouTube isi"
echo "schimba des protectiile), ruleaza: ./update.sh"
