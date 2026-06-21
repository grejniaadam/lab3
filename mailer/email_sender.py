import os
import smtplib
from dataclasses import dataclass
from email.message import EmailMessage
from typing import Optional, Protocol


class SMTPClientProtocol(Protocol):
    def sendmail(self, from_addr: str, to_addrs: list[str], msg: str) -> None:
        ...


@dataclass
class EmailSendResult:
    success: bool
    error: Optional[str] = None


class EmailSender:
    def __init__(
        self,
        smtp_host: Optional[str] = None,
        smtp_port: Optional[int] = None,
        smtp_username: Optional[str] = None,
        smtp_password: Optional[str] = None,
        use_tls: bool = True,
        smtp_client: Optional[SMTPClientProtocol] = None,
    ) -> None:
        self.smtp_host = smtp_host or os.getenv("SMTP_HOST", "localhost")
        self.smtp_port = smtp_port or int(os.getenv("SMTP_PORT", "25"))
        self.smtp_username = smtp_username or os.getenv("SMTP_USERNAME", "")
        self.smtp_password = smtp_password or os.getenv("SMTP_PASSWORD", "")
        self.use_tls = use_tls
        self.smtp_client = smtp_client

    def send(
        self,
        recipient: str,
        subject: str,
        body: str,
        html: Optional[str] = None,
        sender: Optional[str] = None,
    ) -> EmailSendResult:
        sender_address = sender or os.getenv("MAILER_FROM", "no-reply@example.com")
        message = EmailMessage()
        message["From"] = sender_address
        message["To"] = recipient
        message["Subject"] = subject
        message.set_content(body)

        if html:
            message.add_alternative(html, subtype="html")

        return self._send_message(sender_address, recipient, message)

    def _send_message(
        self,
        sender_address: str,
        recipient: str,
        message: EmailMessage,
    ) -> EmailSendResult:
        try:
            if self.smtp_client is not None:
                self.smtp_client.sendmail(
                    sender_address, [recipient], message.as_string()
                )
                return EmailSendResult(success=True)

            with smtplib.SMTP(self.smtp_host, self.smtp_port, timeout=10) as smtp:
                if self.use_tls:
                    smtp.starttls()
                if self.smtp_username and self.smtp_password:
                    smtp.login(self.smtp_username, self.smtp_password)
                smtp.sendmail(
                    sender_address, [recipient], message.as_string()
                )
            return EmailSendResult(success=True)
        except Exception as exc:
            return EmailSendResult(success=False, error=str(exc))
