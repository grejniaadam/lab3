# API Reference — `mailer` package

This file documents the public classes and functions in the `mailer` package.

## `mailer.email_sender`

- `class EmailSender` — convenience wrapper for sending messages via SMTP.
  - Constructor args: `smtp_host`, `smtp_port`, `smtp_username`, `smtp_password`, `use_tls=True`, `smtp_client=None`.
  - `send(recipient: str, subject: str, body: str, html: Optional[str] = None, sender: Optional[str] = None) -> EmailSendResult` — constructs an `email.message.EmailMessage`, sets text and optional HTML alternative, then sends either using the injected `smtp_client` (for tests) or a real `smtplib.SMTP` connection. Returns `EmailSendResult(success: bool, error: Optional[str])`.

## `mailer.subscribers`

- `@dataclass Subscriber(email: str, name: Optional[str])` — simple DTO for subscriber data.
- `class SubscriberManager` — in-memory manager for subscribers.
  - `add(subscriber: Subscriber) -> bool` — validates email format and prevents duplicates; returns True if added.
  - `remove(email: str) -> bool` — removes by normalized email, returns True if removed.
  - `list() -> List[Subscriber]` — returns current subscribers.
  - `get(email: str) -> Optional[Subscriber]` — lookup by email.

Email validation uses a simple regex (`EMAIL_PATTERN`) that checks `user@domain.tld` style addresses.

## `mailer.email_templates`

- `class EmailTemplateRenderer` — convenience wrapper around a Jinja2 `Environment` configured to load templates from `templates/email`.
  - `render_html(template_name: str, context: Dict[str, str]) -> str`
  - `render_text(template_name: str, context: Dict[str, str]) -> str`
  - Raises `EmailTemplateError` on missing templates or rendering errors.

## `mailer.web`

- `create_app() -> Flask` — builds the Flask app and routes:
  - `/` — index rendering `templates/index.html` (subscribe, send forms).
  - `/subscribe` — POST endpoint to add subscriber.
  - `/send` — POST endpoint to send email using `EmailSender`.
  - `/tests` — GET endpoint showing the Test Runner UI.
  - `/run-tests` — POST endpoint that runs `pytest` in a subprocess and returns the captured output (verbose mode).

Notes
- The web UI is intentionally simple and intended for development/demo use. It stores subscribers in memory only. For production use, replace `SubscriberManager` with persistent storage and secure SMTP credentials via environment variables or secret management.
