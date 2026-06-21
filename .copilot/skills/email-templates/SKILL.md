# Email Templates Skill

## Cel
Celem tego skilla jest wsparcie projektowania i implementacji systemu szablonów email w projekcie Mailer. Skill ma pomóc w tworzeniu spójnych, łatwych do utrzymania szablonów HTML i tekstowych, obsłudze zmiennych, oraz testowaniu i weryfikacji poprawności wyjścia.

## Zakres funkcjonalności
Skill koncentruje się na kluczowych aspektach email templates:
- Template inheritance: dziedziczenie wspólnych elementów takich jak nagłówki, stopki i podstawowy layout.
- Variable substitution: podstawianie dynamicznych wartości do szablonów, takich jak imię użytkownika, link potwierdzający lub data.
- HTML/Plain text templates: wspieranie zarówno wersji HTML, jak i uproszczonej wersji tekstowej dla klientów email, które nie renderują HTML.
- Template testing: testowanie generowanego outputu, weryfikacja obecności kluczowych zmiennych i poprawnych bloków warunkowych.
- Examples: przykłady zastosowania w kontekstach Welcome, Confirmation oraz Newsletter.

## Ogólne zasady
1. Utrzymuj szablony modularne i czytelne.
2. Używaj `jinja2` lub innego zgodnego silnika templatingu, który wspiera dziedziczenie i bloki.
3. Wzorce HTML powinny być odporne na brak wartości: stosuj domyślne wartości i zabezpieczenia przed pustymi zmiennymi.
4. Twórz zawsze dwie wersje: HTML oraz Plain text.
5. Testy powinny obejmować zarówno rendering właściwych danych, jak i zabezpieczenia przed brakującymi polami.

## Template inheritance
Template inheritance pozwala oddzielić strukturę wiadomości od treści. W użyciu:
- `base.html` definiuje główne sekcje: nagłówek, ciało, stopkę.
- Szablon specyficzny dla wiadomości (`welcome.html`, `confirmation.html`, `newsletter.html`) rozszerza `base.html` i definiuje własne bloki.
- Dzięki temu aktualizacja layoutu zachodzi w jednym miejscu, a poszczególne wiadomości odziedziczą spójny wygląd.

## Variable substitution
Zmienna substytucja to podstawa mailer templates. Przykłady:
- `{{ user_name }}` – imię odbiorcy.
- `{{ confirmation_link }}` – link weryfikacyjny.
- `{{ newsletter_summary }}` – skrócony opis newslettera.

Należy:
- walidować dane przed przekazaniem do szablonu,
- przygotować domyślne wartości dla brakujących pól,
- unikać bezpośredniego wstrzykiwania surowego HTML bez escaping.

## HTML / Plain text templates
Każdy email powinien mieć dwie wersje:
1. HTML: bogatsza prezentacja z layoutem, przyciskami i stylami.
2. Plain text: prosta wersja tekstowa dla klientów, które nie renderują HTML lub blokują obrazy.

Przykład struktury:
- `templates/email/base.html`
- `templates/email/welcome.html`
- `templates/email/confirmation.html`
- `templates/email/newsletter.html`
- `templates/email/welcome.txt`
- `templates/email/confirmation.txt`
- `templates/email/newsletter.txt`

## Template testing
Testy szablonów powinny obejmować:
- Renderowanie z pełnym zestawem danych.
- Renderowanie z brakującymi wartościami.
- Weryfikację obecności kluczowych fragmentów, np. `{{ confirmation_link }}` lub `{{ unsubscribe_url }}`.
- Porównanie HTML i tekstowej wersji tam, gdzie to możliwe.
- Testowanie warunkowych bloków i pętli.

Przykładowe testy:
- `test_templates_render_correctly`
- `test_welcome_message_contains_user_name`
- `test_newsletter_contains_unsubscribe_link`
- `test_confirmation_message_uses_default_values`

## Examples
### Welcome
- Wysłać spersonalizowany email powitalny.
- Zawiera imię odbiorcy, wprowadzenie i wezwanie do akcji.
- Ma wersję HTML z przyciskiem oraz wersję tekstową z linkiem.

### Confirmation
- Zawiera link potwierdzający lub kod aktywacyjny.
- Powinna weryfikować, czy `confirmation_link` jest poprawnie wstawiony.
- HTML powinien zawierać wyróżniony przycisk, plain text wersja prosty URL.

### Newsletter
- Szablon newslettera może wykorzystywać listę wpisów lub sekcji.
- Powinien wspierać zmienne `newsletter_summary`, `articles`, `unsubscribe_url`.
- Testy walidują, czy lista artykułów i link do wypisania są obecne.

## Implementacja w kontekście Mailer
Skill wspiera tworzenie kodu w `mailer/` oraz szablonów w `templates/` i testów w `tests/`.
Powinien sugerować zarówno strukturę plików, jak i wzorce użycia, np. funkcje do renderowania szablonów oraz automatyczne generowanie tekstowej wersji wiadomości.

## Przykładowe użycie
- `@copilot use email-templates skill`
- `Create a welcome email template with HTML and plain text versions`
- `Add a confirmation email template using template inheritance`
- `Write tests validating variable substitution in newsletter templates`

## Podsumowanie
Skill dla email templates ma zapewnić, że wszystkie komponenty wiadomości są zorganizowane, bezpieczne i łatwe do testowania. Dzięki niemu tworzenie nowych szablonów będzie spójne, a zmiany layoutu proste do wdrożenia dzięki dziedziczeniu i modularności.
