# Quickstart

1. Start the app (after following installation):

```powershell
python -m mailer.web
```

2. Open the UI: `http://127.0.0.1:5000/`

3. Subscribe a user:
- Fill `Email` and optional `Name`, click `Subscribe`.

4. Send a test email:
- Use `Send Email` form to send to a recipient. If you do not have a working SMTP account, prefer using mocks and tests.

5. Run tests from the UI:
- Click `Open Test Runner` and `Run Tests` — the server will execute `pytest` and show the verbose output.

6. Run tests from the command line:

```powershell
python -m pytest -vv -rA
```
