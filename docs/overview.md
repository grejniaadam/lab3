# Mailer — Project Overview

Mailer is a small Flask-based application for managing email subscribers and sending messages. The repository contains:

- `mailer/` — core Python package with modules:
  - `email_sender.py` — `EmailSender` for sending emails via SMTP.
  - `subscribers.py` — `Subscriber` model and `SubscriberManager` for in-memory management and validation.
  - `email_templates.py` — renderer for Jinja2 templates (HTML and plain text).
  - `web.py` — Flask app exposing UI and a test-runner endpoint.
- `templates/` — Jinja2 templates used by the web UI and email rendering.
- `tests/` — pytest test suite covering main functionality.

Goals of this documentation:
- Provide installation and quickstart steps.
- Document public API of the main modules.
- Give examples how to use the library and run the web UI.
