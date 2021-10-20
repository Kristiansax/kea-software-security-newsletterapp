# Django Newsletter App 
KEA Django project af: Kristian Saxkjær, Kristian Bredal og Morten Linnemann

## Beskrivelse
Django projektet består af en enkelt applikation `signupform` som tager mod brugerens 'username', 'first name', 'last name' og 'email'.

### Opbygning
```bash
kea-software-security-newsletterapp/
├── db.sqlite3
├── manage.py
├── NewsletterApp
│   ├── __init__.py
│   ├── __pycache__
│   ├── settings.py
│   ├── templates
│   │   ├── signup.html
│   │   └── thanks.html
│   ├── urls.py
│   └── wsgi.py
└── signupform
    ├── admin.py
    ├── apps.py
    ├── forms.py
    ├── __init__.py
    ├── migrations
    │   ├── __init__.py
    │   └── __pycache__
    ├── models.py
    ├── __pycache__
    ├── tests.py
    ├── urls.py
    └── views.py

```

## Tekniske detaljer

### urls.py
Foruden default admin page defineret i `NewsletterApp/urls.py`, er der inkluderet urls fra `signupform`, som har en index på `/signupform/`, og en formular til indregistering på `/signupform/signup`.

### forms.py
Definerer klassen `NewsletterForm` som definerer felterne i formen:
- username
- first_name
- last_name
- email_address

Her har vi sat en limit på 30 tegn på de tre 'name' felter.

### views.py
I vores views har vi defineret to forskellige klasser; `index` og `newsletter_form`.

#### index
Returnerer et HTTP response med teksten 'Hello, world. You're at the signup index.'

#### newsletter_form
Hvis HTTP forespørgselsmetoden er 'GET' returnerer den en form baseret på `NewsletterForm` klassen i `forms.py`. Hvis forespørgselsmetoden derimod er `POST`, validerer vi formen, og hvis den er valid bliver dataen gemt i databasen vha. vores model `SignupDetail`.

### templates
Til vores formular tilhører templaten `signup.html`, samt en thank you page `thanks.html`.

`signup.html` er lige nu ikke skalérbar, den burde, i stedet for at have hardcoded felter for input, iterére over felterne defineret i `forms.py` og lave inputs til dem.

### models.py
Definerer klassen `SignupDetail` som indeholder samme felter og constraints som findes i vores formular.

## Sikkerhed
Django indeholder mange funktioner som kan hjælpe udviklere med at lave sikre applikationer, uden selv at skulle gøre det store. 
Her har vi bl.a. gjort brug af Djangos indbyggede `{% csrf_token %}` som beskytter mod Cross-site Request Forgery.

Derudover har vi gjort brug af Djangos eget library `django.db` til at gemme information til databasen. Dette library sørger selv for at sanitere input så man ikke er sårbar over for SQL injection.

## Fake data
En del af opgaven var at teste vores form ved at skrive et script som kunne input falsk brugerdata, men denne del nåede vi ikke at udvikle.

Vores plan var at fange en 'POST' forespørgsel gennem Firefox, og genbruge det request i et Python script vha. `requests` library, med falsk data fra `faker` library ('https://pypi.org/project/Faker/').

## Referencer
https://docs.djangoproject.com/en/2.2/intro/tutorial01/
https://www.tutorialspoint.com/django/django_quick_guide.htm
https://docs.djangoproject.com/en/3.2/topics/templates/
https://docs.djangoproject.com/en/3.2/topics/forms/
https://pypi.org/project/Faker/
https://exceptionshub.com/django-model-doesnt-declare-an-explicit-app_label.html
