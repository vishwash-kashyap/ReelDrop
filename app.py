from pathlib import Path
import re, uuid
from flask import Flask, render_template, request, send_file, flash, redirect, url_for
import yt_dlp

app = Flask(__name__)
app.secret_key = "change-this-before-deployment"
OUT = Path("downloads")
OUT.mkdir(exist_ok=True)
# IG_URL = re.compile(r"^https?://(www\\.)?instagram\\.com/(reel|reels|p)/[A-Za-z0-9_-]+/?(?:\\?.*)?$", re.I)
IG_URL = re.compile(
    r"^https?://(www\.)?instagram\.com/(reel|reels|p)/[A-Za-z0-9_-]+/?(?:\?.*)?$",
    re.I
)

@app.get("/")
def home():
    return render_template("index.html")

@app.post("/download")
def download():
    url = request.form.get("url", "").strip()
    if not IG_URL.match(url):
        flash("Please enter a valid public Instagram Reel or post URL.", "error")
        return redirect(url_for("home"))

    # No login cookies, private-post access, or access-control bypass.
    job = uuid.uuid4().hex
    opts = {
        "outtmpl": str(OUT / f"{job}.%(ext)s"),
        "format": "best[ext=mp4]/best",
        "noplaylist": True, "quiet": True, "no_warnings": True,
        "socket_timeout": 20, "max_filesize": 150 * 1024 * 1024,
    }
    try:
        with yt_dlp.YoutubeDL(opts) as ydl:
            info = ydl.extract_info(url, download=True)
            path = Path(ydl.prepare_filename(info))
        if not path.exists():
            found = list(OUT.glob(f"{job}.*"))
            if not found:
                raise FileNotFoundError()
            path = found[0]
        return send_file(path, as_attachment=True, download_name=f"reeldrop-{job[:8]}{path.suffix}")
    except Exception:
        flash("Couldn't download this Reel. It may be private, unavailable, or unsupported. This tool does not sign in or bypass access controls.", "error")
        return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
