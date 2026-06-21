import pytest
from mailer.email_templates import EmailTemplateRenderer, EmailTemplateError


@pytest.fixture
def renderer() -> EmailTemplateRenderer:
    return EmailTemplateRenderer()


def test_render_welcome_templates(renderer: EmailTemplateRenderer) -> None:
    context = {"user_name": "Anna", "action_url": "https://example.com/start", "title": "Welcome", "subject": "Welcome Email"}

    html_output = renderer.render_html("welcome", context)
    text_output = renderer.render_text("welcome", context)

    assert "Hello Anna" in html_output
    assert "Get Started" in html_output
    assert "https://example.com/start" in text_output


def test_render_confirmation_templates(renderer: EmailTemplateRenderer) -> None:
    context = {"user_name": "Jan", "confirmation_link": "https://example.com/confirm", "title": "Confirm", "subject": "Confirmation"}

    html_output = renderer.render_html("confirmation", context)
    text_output = renderer.render_text("confirmation", context)

    assert "Please confirm your email" in html_output
    assert "https://example.com/confirm" in text_output


def test_render_missing_template_raises_error(renderer: EmailTemplateRenderer) -> None:
    with pytest.raises(EmailTemplateError):
        renderer.render_html("missing", {"title": "Missing", "subject": "Missing"})
