# Agent 2 — Flask Form Validation

## Co zostało dodane
- Skill: `form-validation` w `.copilot/skills/form-validation/`
- Agent: `Form Validation Agent` w `.github/agents/form-validation-agent.yaml`
- Rozszerzenie CLI: `mailer/cli.py` o komendę `validate-form`

## Jak to działa
1. Agent analizuje formularze w `mailer/web.py` i szablony w `templates/`.
2. Skill `form-validation` opisuje zasady walidacji danych wejściowych we Flask.
3. CLI w `mailer/cli.py` pozwala sprawdzić konfigurację walidacji i uruchomić sanity check danych formularza.

## Uruchomienie
```powershell
python -m mailer.cli validate-form --email user@example.com --name "Jan Kowalski"
```

## Cel
Skill i agent pomagają w stworzeniu bezpiecznego i poprawnego przetwarzania formularzy w aplikacji Mailer, pokazując jak weryfikować dane użytkownika przed dalszym przetwarzaniem.
