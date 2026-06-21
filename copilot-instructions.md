# Copilot Instructions for Mailer Project

## Cel
Ten dokument definiuje globalne standardy i wytyczne dla projektu Mailer, aby zapewnić spójność kodu, bezpieczeństwo i wysoką jakość implementacji.

## Wersja Pythona i bibliotek
- Używaj Pythona 3.11 lub nowszego, jeśli projekt to wspiera.
- Zarządzaj zależnościami w `requirements.txt` lub `pyproject.toml`.
- Dokładnie deklaruj wersje bibliotek w plikach konfiguracyjnych.
- Unikaj instalowania zależności globalnie; używaj środowiska wirtualnego (`venv`, `virtualenv`, `pipenv`, `poetry`).

## Standardy PEP 8
- Stosuj się do zasad PEP 8 w całym repozytorium.
- Maksymalna długość linii: 79 znaków (lub 99, jeśli projekt już tak ustalono, ale najpierw uzgadniaj).
- Używaj 4 spacji zamiast tabulatorów.
- Odstępy wokół operatorów, po przecinkach i podziałach linii.
- Nazwy klas w PascalCase, funkcji i zmiennych w snake_case.
- Dla stałych używaj UPPER_SNAKE_CASE.
- Zachowuj czytelne importy: standardowe biblioteki, zewnętrzne pakiety, importy lokalne.
- Utrzymuj jednolitą strukturę plików i modułów.

## Konwencje nazewnicze
- `mailer/` – moduły związane z logiką biznesową.
  - Moduły i pliki: `snake_case.py`.
  - Klasy: PascalCase.
  - Funkcje i metody: snake_case.
  - Zmienna instancji: snake_case.
- `templates/` – szablony Flask HTML.
  - Pliki `.html` w snake_case.
  - Używaj czytelnych nazw bloków i zmiennych w Jinja2.
  - Unikaj wstawiania złożonej logiki w szablonach; logika powinna być w Pythonie.
- `static/` – pliki CSS/JavaScript.
  - Pliki CSS: snake_case, używaj nowoczesnych standardów CSS.
  - Pliki JavaScript: snake_case lub camelCase zgodnie z już przyjętymi standardami frontendu.
  - Unikaj globalnych zmiennych JS; używaj modułów i izolacji przestrzeni nazw.
- `tests/` – testy pytest.
  - Pliki testowe: `test_*.py`.
  - Funkcje testowe: `test_*`.
  - Używaj opisowych nazw testów, które wyjaśniają zachowanie.

## Wymagania testowania
- Wykorzystuj `pytest` jako główny framework testowy.
- Pokryj kluczową logikę biznesową w `mailer/` testami jednostkowymi.
- Testy integracyjne powinny weryfikować połączenia między komponentami, gdy to potrzebne.
- Unikaj testowania szczegółów implementacji; skup się na zachowaniu i kontraktach.
- Wszystkie nowe funkcje powinny mieć odpowiadające testy.
- Uruchamiaj testy lokalnie przed commitowaniem.

## Strategia testowania
Zwróć się do "Mailer Complete Testing Skill" dla szczegółów.

Minimum requirements:
- Każda funkcja: min. 2 testy
- Edge cases + error handling
- Mocking external services
- Coverage: min. 80%

Polecenie: "Use mailer-complete-testing skill"

## Bezpieczeństwo (secrets, env vars)
- Nigdy nie umieszczaj sekretów, kluczy API ani haseł w repozytorium.
- Wykorzystuj zmienne środowiskowe (`.env`, systemowe zmienne środowiskowe) do konfiguracji wrażliwych danych.
- Dodaj `.env` do `.gitignore` i przechowuj tylko `.env.example` z przykładową strukturą.
- Korzystaj z bezpiecznych bibliotek do ładowania konfiguracji, np. `python-dotenv` tylko w lokalnym/deweloperskim środowisku.
- Waliduj i obsługuj brakujące wymagane zmienne środowiskowe w kodzie.

## Konwencje commitów
- Używaj jasnych, opisowych komunikatów commitów.
- Format: `typ: krótki opis`.
- Typy commitów mogą obejmować:
  - `feat:` nowa funkcja
  - `fix:` poprawka błędu
  - `refactor:` refaktoryzacja kodu bez zmiany zachowania
  - `docs:` aktualizacja dokumentacji
  - `test:` dodanie lub poprawka testów
  - `chore:` zmiany narzędzi/dependencies/konfiguracji
- Unikaj commitów typu „update” lub „poprawki” bez kontekstu.

## Obsługa błędów
- Błędy należy obsługiwać expresyjnie i logować.
- Nie ignoruj wyjątków; przechwytuj tylko te, które możesz obsłużyć sensownie.
- Używaj customowych wyjątków tam, gdzie to ma sens, aby oddzielić warstwy biznesowe i aplikacyjne.
- Raportuj użytkownikowi przyjazne komunikaty zamiast surowych tracebacks w interfejsie.
- W przypadku krytycznych błędów zwracaj odpowiednie kody statusu HTTP i komunikaty.

## Komponenty projektu
- `mailer/` – implementacja logiki biznesowej i wysyłania maili.
- `templates/` – widoki Flask HTML i szablony UI.
- `static/` – style CSS i skrypty JavaScript.
- `tests/` – testy jednostkowe i integracyjne realizowane przez `pytest`.

## Dodatkowe uwagi
- Utrzymuj czytelność kodu jako priorytet.
- Komentarze stosuj tylko tam, gdzie kod nie jest wystarczająco samoopisowy.
- Dokumentuj kluczowe decyzje architektoniczne i przypadki użycia w `README.md` lub odpowiednich plikach dokumentacji.
- Przed publikacją zawsze uruchamiaj testy i sprawdzaj formatowanie zgodnie z przyjętymi standardami.
