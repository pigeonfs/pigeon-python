# Pigeon Python SDK

Official Python client for the [Pigeon](https://github.com/pigeonfs/pigeon) email API. API shape follows [resend-python](https://github.com/resend/resend-python): `pigeon.Emails.send({...})`.

## Installation

```bash
pip install git+https://github.com/pigeonfs/pigeon-python.git
```

## Setup

Create an API key in the Pigeon dashboard (`pg_…`). Local default host is `http://localhost:4005`.

```python
import pigeon

pigeon.api_key = "pg_xxxx"
# pigeon.base_url = "https://pigeon.bitscorp.co"
```

## Send an email

```python
email = pigeon.Emails.send({
    "from": "Ada <ada@yourdomain.com>",
    "to": ["person@example.com"],
    "subject": "hi",
    "html": "<strong>hello, world!</strong>",
    "reply_to": "ada@yourdomain.com",
})
print(email["id"])
```

## Other methods

```python
pigeon.Emails.list(status="sent")
pigeon.Emails.get(email_id)
pigeon.Emails.cancel(email_id)

pigeon.Domains.list()
pigeon.Domains.create("yourdomain.com")
pigeon.Domains.verify(domain_id)

pigeon.Contacts.create({"email": "person@example.com", "name": "Ada"})
pigeon.Automations.trigger(automation_id, {"to": "person@example.com"})
```

The from address must use a domain you verified in Pigeon.

## License

MIT
