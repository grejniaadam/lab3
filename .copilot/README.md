# GitHub Copilot Configuration for Mailer

## Instrukcje (Instructions)
- `copilot-instructions.md` – Globalne standardy projektu

## Skills (Umiejętności)
1. **email-validation** – Walidacja adresów email
2. **mailer-complete-testing** – Kompletne testowanie

Użycie:
```bash
@copilot use email-validation skill
```

## Agenci (Agents)
1. **docs-generator-agent** – Generowanie dokumentacji
2. [Dodaj więcej w przyszłości]

Użycie:
```bash
Generate API documentation for mailer.subscribers module
```

## Workflow
1. Developer pisze kod
2. Copilot sugeruje pattern z odpowiedniego skill
3. Dev generuje testy używając skill
4. Docs generator tworzy dokumentację
5. Code reviews wspierane instrukcjami

## Best Practices
- Zawsze patrz na instrukcje przed rozpoczęciem
- Użyj skill jeśli dostępny
- Agenci dla złożonych, wieloetapowych zadań
