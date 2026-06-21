# Flask Form Validation Skill

## Cel umiejętności
Skill wspiera tworzenie walidacji formularzy we Flask oraz bezpieczne przetwarzanie danych wysyłanych z UI.

## Kontekst
- Projekt: Mailer
- Wymaganie: walidacja subskrypcji i wysyłki maili
- Zastosowanie: sprawdzanie pól email, długości tekstu i ochrony przed złą treścią

## Wzorzec: Walidacja formularza

```python
from flask import request
from wtforms import Form, StringField, validators

class SubscribeForm(Form):
    email = StringField("Email", [validators.DataRequired(), validators.Email()])
    name = StringField("Name", [validators.Optional(), validators.Length(max=128)])

@app.route('/subscribe', methods=['POST'])
def subscribe():
    form = SubscribeForm(request.form)
    if not form.validate():
        return render_template('index.html', error='Niepoprawne dane')
    # dalej przetwarzanie
```

## Wzorzec: Testy walidacji

```python
def test_subscribe_form_validation():
    form = SubscribeForm(data={"email": "bad", "name": "Ala"})
    assert not form.validate()
```

## Reguły
- Używaj walidatorów `DataRequired`, `Email`, `Length`, `Optional`.
- Waliduj zarówno email, jak i treść pól tekstowych.
- Obsługuj błędy formularza w UI i pokazuj komunikaty użytkownikowi.
- Nie ufaj danym z klienta; zawsze waliduj po stronie serwera.
