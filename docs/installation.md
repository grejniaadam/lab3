# Installation

Prerequisites
- Python 3.9+ installed and available as `python`.

Steps
1. Create and activate a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
pip install --upgrade pip
pip install -r requirements.txt
```

3. Copy env example and configure SMTP settings:

```powershell
copy .env.example .env
# Edit .env and set SMTP_HOST, SMTP_PORT, SMTP_USERNAME, SMTP_PASSWORD, MAILER_FROM
```

4. Run the development server:

```powershell
python -m mailer.web
```

The web UI will be available at `http://127.0.0.1:5000/` by default.
