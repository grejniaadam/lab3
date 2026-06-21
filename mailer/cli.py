import argparse
import os
import smtplib
import subprocess
from typing import Optional

from .subscribers import SubscriberManager


def check_smtp(
    host: str,
    port: int,
    username: Optional[str] = None,
    password: Optional[str] = None,
    use_tls: bool = True,
) -> bool:
    print(f"Sprawdzanie SMTP: {host}:{port}")
    try:
        with smtplib.SMTP(host, port, timeout=10) as client:
            print("Połączono z serwerem SMTP")
            if use_tls:
                print("Rozpoczynam STARTTLS...")
                client.starttls()
                print("STARTTLS zakończony")
            if username and password:
                print(f"Logowanie jako {username}...")
                client.login(username, password)
                print("Logowanie powiodło się")
        print("Sprawdzenie SMTP zakończone sukcesem")
        return True
    except Exception as exc:
        print(f"Błąd połączenia SMTP: {exc}")
        return False


def run_tests() -> bool:
    print("Uruchamianie testów...")
    result = subprocess.run(
        ["python", "-m", "pytest", "-vv", "-rA"],
        capture_output=True,
        text=True,
    )
    print(result.stdout)
    if result.stderr:
        print(result.stderr)
    if result.returncode == 0:
        print("Wszystkie testy przeszły pomyślnie")
        return True
    print(f"Testy zakończone z kodem {result.returncode}")
    return False


def validate_form(email: str, name: str) -> bool:
    print("Walidacja formularza...")
    valid = True
    if "@" not in email or "." not in email:
        print("Błąd: email ma niepoprawny format")
        valid = False
    if len(name) > 128:
        print("Błąd: nazwa jest za długa (max 128 znaków)")
        valid = False
    if valid:
        print("Walidacja poprawna")
    return valid


def status() -> None:
    manager = SubscriberManager()
    print("Stan terminala Mailer")
    print("=======================")
    print(f"Liczba subskrybentów: {len(manager.list())}")
    print("Ustawienia SMTP:")
    print(f"  HOST: {os.getenv('SMTP_HOST', 'brak')}")
    print(f"  PORT: {os.getenv('SMTP_PORT', 'brak')}")
    print(f"  FROM: {os.getenv('MAILER_FROM', 'brak')}")
    print("Aby sprawdzić SMTP, użyj `check-smtp`.")


def main() -> int:
    parser = argparse.ArgumentParser(description="Mailer CLI - terminalowy interfejs monitorowania SMTP")
    subparsers = parser.add_subparsers(dest="command", required=True)

    subparsers.add_parser("status", help="Pokaż stan subskrybentów i konfigurację SMTP")

    check_parser = subparsers.add_parser("check-smtp", help="Sprawdź połączenie do serwera SMTP")
    check_parser.add_argument("--host", default=os.getenv("SMTP_HOST", "localhost"))
    check_parser.add_argument("--port", type=int, default=int(os.getenv("SMTP_PORT", "25")))
    check_parser.add_argument("--username", default=os.getenv("SMTP_USERNAME", ""))
    check_parser.add_argument("--password", default=os.getenv("SMTP_PASSWORD", ""))
    check_parser.add_argument("--no-tls", action="store_true", help="Wyłącz STARTTLS")

    subparsers.add_parser("run-tests", help="Uruchom testy Pytest i pokaż wynik")

    validate_parser = subparsers.add_parser("validate-form", help="Sprawdź dane formularza pod kątem podstawowej walidacji")
    validate_parser.add_argument("--email", required=True, help="Adres email do walidacji")
    validate_parser.add_argument("--name", default="", help="Imię/nazwisko do walidacji")

    args = parser.parse_args()

    if args.command == "status":
        status()
        return 0
    if args.command == "check-smtp":
        use_tls = not args.no_tls
        success = check_smtp(args.host, args.port, args.username, args.password, use_tls=use_tls)
        return 0 if success else 1
    if args.command == "run-tests":
        success = run_tests()
        return 0 if success else 1
    if args.command == "validate-form":
        success = validate_form(args.email, args.name)
        return 0 if success else 1

    return 1


if __name__ == "__main__":
    raise SystemExit(main())
