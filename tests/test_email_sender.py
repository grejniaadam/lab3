import pytest
from unittest.mock import Mock
from mailer.email_sender import EmailSender, EmailSendResult


def test_send_success_with_mock_smtp() -> None:
    mock_smtp = Mock()
    sender = EmailSender(smtp_client=mock_smtp)

    result = sender.send("user@example.com", "Subject", "Body")

    mock_smtp.sendmail.assert_called_once()
    assert result.success
    assert result.error is None


def test_send_failure_returns_error() -> None:
    mock_smtp = Mock()
    mock_smtp.sendmail.side_effect = Exception("SMTP error")
    sender = EmailSender(smtp_client=mock_smtp)

    result = sender.send("user@example.com", "Subject", "Body")

    assert not result.success
    assert result.error == "SMTP error"
