# Agent 1 — SMTP Monitor

## Co zostało dodane
- Skill: `smtp-monitoring` w `.copilot/skills/smtp-monitoring/`
- Agent: `SMTP Monitor Agent` w `.github/agents/smtp-monitor-agent.yaml`
- Terminalowy interfejs: `mailer/cli.py`

## Jak to działa
1. Agent firmware analizuje kod z `mailer/email_sender.py` i `mailer/web.py`.
2. Skill `smtp-monitoring` opisuje wzorce dla sprawdzania połączenia SMTP, próby logowania oraz obsługi błędów.
3. Terminalowy interfejs w `mailer/cli.py` pozwala na:
   - sprawdzenie połączenia SMTP (`check-smtp`),
   - wyświetlenie stanu subskrybentów (`status`),
   - uruchomienie testów (`run-tests`).

## Uruchomienie
```powershell
python -m mailer.cli status
python -m mailer.cli check-smtp
python -m mailer.cli run-tests
```

## Cel
Skill i agent wspierają budowę niezawodnego monitoringu SMTP w Mailerze oraz pokazują, jak testować i obserwować stan systemu z terminala.
