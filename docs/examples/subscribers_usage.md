# Example: Managing Subscribers

Python usage example (script)

```python
from mailer.subscribers import Subscriber, SubscriberManager

manager = SubscriberManager()
added = manager.add(Subscriber(email="alice@example.com", name="Alice"))
print("Added?", added)
print("All subscribers:", manager.list())

# Remove
manager.remove("alice@example.com")
```

Example: rendering a welcome email

```python
from mailer.email_templates import EmailTemplateRenderer

renderer = EmailTemplateRenderer()
context = {"user_name": "Alice", "action_url": "https://example.com/start", "title": "Welcome", "subject": "Welcome"}
html = renderer.render_html("welcome", context)
text = renderer.render_text("welcome", context)
```
