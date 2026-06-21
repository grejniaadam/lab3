# SMTP Monitoring Skill

## Cel umiejętności
Skill wspiera tworzenie monitoringu i testów dla połączeń SMTP w projekcie Mailer.

## Kontekst
- Projekt: Mailer
- Wymaganie: sprawdzanie stabilności serwera SMTP i poprawności konfiguracji
- Zastosowanie: testy integracyjne, sanity checks, monitoring stanu wysyłki

## Wzorzec: Walidacja połączenia SMTP

```python
import smtplib

class SmtpMonitor:
    def __init__(self, host: str, port: int, username: str = "", password: str = "", use_tls: bool = True):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.use_tls = use_tls

    def check(self) -> bool:
        try:
            with smtplib.SMTP(self.host, self.port, timeout=10) as client:
                if self.use_tls:
                    client.starttls()
                if self.username and self.password:
                    client.login(self.username, self.password)
            return True
        except Exception:
            return False
```

## Wzorzec: Testy monitoringu SMTP

```python
def test_smtp_connection_success(mock_smtp):
    monitor = SmtpMonitor("smtp.example.com", 587, username="user", password="pass")
    assert monitor.check()
```

## Reguły
- Sprawdź połączenie, uwierzytelnienie i TLS.
- Uwzględnij timeout i wyjątki.
- Testuj z mockowanym klientem SMTP, aby unikać realnych wysyłek.
- Zwracaj wyraźny komunikat o błędzie w terminalu lub logu.
