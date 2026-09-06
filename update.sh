#!/usr/bin/env bash
# Actualizeaza yt-dlp la ultima versiune in mediul virtual local.
# Ruleaza asta daca descarcarile incep sa dea erori (ex. "HTTP 403
# Forbidden") -- YouTube isi schimba des protectiile impotriva
# descarcarilor, iar yt-dlp scoate actualizari frecvente ca sa tina pasul.
set -e
APP_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

if [ ! -d "$APP_DIR/venv" ]; then
    echo "Nu gasesc mediul virtual in $APP_DIR/venv."
    echo "Ruleaza mai intai ./install_linux.sh"
    exit 1
fi

echo "-> Actualizez yt-dlp..."
"$APP_DIR/venv/bin/pip" install --upgrade yt-dlp
echo "-> Gata. Versiune curenta:"
"$APP_DIR/venv/bin/python" -c "import yt_dlp; print(yt_dlp.version.__version__)"
