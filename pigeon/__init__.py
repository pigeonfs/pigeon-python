"""Official Python SDK for the Pigeon email API."""

from pigeon.request import PigeonError, Request

api_key = None
base_url = None
default_http_client = Request()

from pigeon import automations, contacts, domains, emails  # noqa: E402

Emails = emails.Emails
Domains = domains.Domains
Contacts = contacts.Contacts
Automations = automations.Automations

__all__ = [
    "Emails",
    "Domains",
    "Contacts",
    "Automations",
    "PigeonError",
    "api_key",
    "base_url",
]
