from typing import Any, Mapping


class Contacts:
    @classmethod
    def create(cls, params: Mapping[str, Any]) -> Any:
        import pigeon

        return pigeon.default_http_client.request("POST", "/api/contacts", dict(params))
