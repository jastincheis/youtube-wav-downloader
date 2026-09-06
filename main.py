"""
YouTube -> WAV Downloader
=========================
Interfata grafica simpla (Tkinter) pentru descarcarea audio-ului din
linkuri YouTube si convertirea lui in format WAV, folosind yt-dlp.

Ruleaza cu: python main.py (vezi install_linux.sh / README.md pentru
instalarea dependentelor pe Linux).
"""

import os
import shutil
import threading
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext

import yt_dlp


def get_ffmpeg_path():
    """Gaseste binarul ffmpeg instalat pe sistem (in PATH). Daca nu e
    gasit, foloseste ca rezerva pachetul imageio-ffmpeg, atunci cand
    este instalat."""
    system_ffmpeg = shutil.which("ffmpeg")
    if system_ffmpeg:
        return system_ffmpeg
    try:
        import imageio_ffmpeg
    except ImportError:
        return None

    return imageio_ffmpeg.get_ffmpeg_exe()


def set_window_icon(root):
    """Seteaza iconita ferestrei, daca gaseste fisierul icons/youtube-wav-downloader.png
    langa acest script (nu e o eroare fatala daca lipseste)."""
    icon_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "icons",
        "youtube-wav-downloader.png",
    )
    if os.path.isfile(icon_path):
        try:
            icon_img = tk.PhotoImage(file=icon_path)
            root.iconphoto(True, icon_img)
            root._icon_img_ref = icon_img  # evita garbage-collection
        except tk.TclError:
            pass


class DownloaderApp:
    def __init__(self, root):
        self.root = root
        root.title("YouTube -> WAV Downloader")
        root.geometry("620x480")
        root.minsize(560, 420)
        set_window_icon(root)

        tk.Label(root, text="Link-uri YouTube (unul pe linie):", anchor="w").pack(
            fill="x", padx=10, pady=(10, 0)
        )
        self.url_text = scrolledtext.ScrolledText(root, height=8)
        self.url_text.pack(fill="x", padx=10)

        dir_frame = tk.Frame(root)
        dir_frame.pack(fill="x", padx=10, pady=10)
        default_dir = os.path.join(os.path.expanduser("~"), "Downloads")
        self.out_dir = tk.StringVar(value=default_dir)
        tk.Label(dir_frame, text="Folder destinatie:").pack(side="left")
        tk.Entry(dir_frame, textvariable=self.out_dir).pack(
            side="left", fill="x", expand=True, padx=5
        )
        tk.Button(dir_frame, text="Alege...", command=self.choose_dir).pack(side="left")

        self.download_btn = tk.Button(
            root,
            text="Descarca (WAV)",
            command=self.start_download,
            bg="#c00000",
            fg="white",
            height=2,
        )
        self.download_btn.pack(fill="x", padx=10, pady=5)

        tk.Label(root, text="Status:", anchor="w").pack(fill="x", padx=10)
        self.status = scrolledtext.ScrolledText(root, height=10, state="disabled")
        self.status.pack(fill="both", expand=True, padx=10, pady=(0, 10))

    def choose_dir(self):
        d = filedialog.askdirectory()
        if d:
            self.out_dir.set(d)

    def log(self, msg):
        def _do():
            self.status.configure(state="normal")
            self.status.insert("end", msg + "\n")
            self.status.see("end")
            self.status.configure(state="disabled")

        self.root.after(0, _do)

    def set_button_state(self, enabled):
        def _do():
            self.download_btn.config(
                state="normal" if enabled else "disabled",
                text="Descarca (WAV)" if enabled else "Se descarca...",
            )

        self.root.after(0, _do)

    def start_download(self):
        urls = [u.strip() for u in self.url_text.get("1.0", "end").splitlines() if u.strip()]
        if not urls:
            messagebox.showwarning("Atentie", "Introdu cel putin un link YouTube.")
            return
        out_dir = self.out_dir.get().strip()
        if not out_dir:
            messagebox.showwarning("Atentie", "Alege un folder destinatie.")
            return
        os.makedirs(out_dir, exist_ok=True)
        self.set_button_state(False)
        threading.Thread(target=self.run_downloads, args=(urls, out_dir), daemon=True).start()

    def run_downloads(self, urls, out_dir):
        ffmpeg_path = get_ffmpeg_path()
        total = len(urls)
        for i, url in enumerate(urls, start=1):
            self.log(f"[{i}/{total}] Pornesc: {url}")
            ydl_opts = {
                "format": "bestaudio/best",
                "outtmpl": os.path.join(out_dir, "%(title)s.%(ext)s"),
                "ffmpeg_location": ffmpeg_path,
                "postprocessors": [
                    {
                        "key": "FFmpegExtractAudio",
                        "preferredcodec": "wav",
                    }
                ],
                "noplaylist": True,
                "progress_hooks": [self._progress_hook],
                "quiet": True,
                "no_warnings": True,
            }
            try:
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([url])
                self.log(f"[{i}/{total}] Terminat: {url}")
            except Exception as e:
                self.log(f"[{i}/{total}] Eroare la {url}: {e}")
        self.log("Toate descarcarile s-au terminat.")
        self.set_button_state(True)

    def _progress_hook(self, d):
        if d.get("status") == "downloading":
            pct_str = (d.get("_percent_str") or "").strip().rstrip("%")
            try:
                pct = float(pct_str)
            except ValueError:
                return
            # afiseaza doar din 10 in 10% ca sa nu inunde log-ul
            bucket = int(pct // 10)
            if bucket != getattr(self, "_last_bucket", -1):
                self._last_bucket = bucket
                speed = (d.get("_speed_str") or "").strip()
                self.log(f"   {pct_str}% {speed}")
        elif d.get("status") == "finished":
            self._last_bucket = -1
            self.log("   Conversie in WAV...")


def main():
    root = tk.Tk()
    DownloaderApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
