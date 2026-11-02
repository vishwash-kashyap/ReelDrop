# ReelDrop

Beginner-friendly Flask starter with responsive frontend and a backend attempt for publicly accessible Instagram Reel/post URLs.

## Important
- Use only for videos you own or have permission to download.
- No Instagram login cookies, private-post access, or access-control bypass.
- Instagram can change its systems; public URL extraction may fail. This is not an official Instagram API or a guaranteed service.
- Follow Instagram's terms and applicable copyright law.
- Before public deployment, add rate limiting, automatic file cleanup, request limits, abuse protection, and a production WSGI server. Change `app.secret_key`.

## Run on Windows
1. Install Python 3.10+.
2. Extract this ZIP and open the `ReelDrop` folder in VS Code.
3. Open Terminal → New Terminal.
4. Run:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python app.py
```

If PowerShell blocks activation, use Command Prompt and run:
` .\.venv\Scripts\activate.bat `

5. Visit http://127.0.0.1:5000

## Structure
- `app.py` — Flask backend
- `templates/index.html` — page structure
- `static/style.css` — design
- `static/script.js` — paste button
