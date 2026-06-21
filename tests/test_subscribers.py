import pytest
from mailer.subscribers import Subscriber, SubscriberManager


def test_add_subscriber_success() -> None:
    manager = SubscriberManager()
    result = manager.add(Subscriber(email="user@example.com", name="User"))

    assert result is True
    assert len(manager.list()) == 1


def test_add_subscriber_duplicate_fails() -> None:
    manager = SubscriberManager()
    manager.add(Subscriber(email="user@example.com", name="User"))
    result = manager.add(Subscriber(email="user@example.com", name="User"))

    assert result is False
    assert len(manager.list()) == 1


def test_remove_subscriber_success() -> None:
    manager = SubscriberManager()
    manager.add(Subscriber(email="user@example.com", name="User"))

    assert manager.remove("user@example.com") is True
    assert len(manager.list()) == 0


def test_remove_nonexistent_subscriber_fails() -> None:
    manager = SubscriberManager()

    assert manager.remove("missing@example.com") is False
