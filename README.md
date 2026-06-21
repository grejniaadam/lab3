# Mailer Project

Prosty projekt Flask do zarządzania subskrybentami i wysyłania emaili.

## Struktura projektu

- `mailer/` – logika biznesowa, wysyłanie maili, zarządzanie subskrybentami
- `templates/` – HTML dla aplikacji Flask
- `tests/` – testy jednostkowe Pytest

## Uruchomienie

1. Utwórz wirtualne środowisko:
   ```bash
   python -m venv .venv
   ```
2. Zainstaluj zależności:
   ```bash
   pip install -r requirements.txt
   ```
3. Skopiuj `.env.example` do `.env` i uzupełnij ustawienia SMTP.
4. Uruchom aplikację:
   ```bash
   python -m mailer.web
   ```

## Testy

```bash
pytest
```

## Pliki kluczowe

- `mailer/email_sender.py` – wysyłanie wiadomości email przez SMTP
- `mailer/subscribers.py` – zarządzanie subskrybentami i walidacja emaili
- `mailer/web.py` – aplikacja Flask
- `templates/index.html` – proste UI do subskrypcji i wysyłania wiadomości
