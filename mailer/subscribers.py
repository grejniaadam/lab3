import re
from dataclasses import dataclass, field
from typing import Dict, List, Optional


EMAIL_PATTERN = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"


@dataclass
class Subscriber:
    email: str
    name: Optional[str] = None


class SubscriberManager:
    def __init__(self) -> None:
        self._subscribers: Dict[str, Subscriber] = {}

    def add(self, subscriber: Subscriber) -> bool:
        if not self._validate_email(subscriber.email):
            return False
        normalized = subscriber.email.strip().lower()
        if normalized in self._subscribers:
            return False
        self._subscribers[normalized] = subscriber
        return True

    def remove(self, email: str) -> bool:
        normalized = email.strip().lower()
        if normalized not in self._subscribers:
            return False
        del self._subscribers[normalized]
        return True

    def list(self) -> List[Subscriber]:
        return list(self._subscribers.values())

    def get(self, email: str) -> Optional[Subscriber]:
        return self._subscribers.get(email.strip().lower())

    @staticmethod
    def _validate_email(email: str) -> bool:
        if not email or not isinstance(email, str):
            return False
        return bool(re.match(EMAIL_PATTERN, email.strip()))
