from typing import Any, Mapping, Optional


class Automations:
    @classmethod
    def trigger(cls, automation_id: str, params: Optional[Mapping[str, Any]] = None) -> Any:
        import pigeon

        return pigeon.default_http_client.request(
            "POST", f"/api/automations/{automation_id}/trigger", dict(params or {})
        )
