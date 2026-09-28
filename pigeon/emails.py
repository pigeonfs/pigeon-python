from typing import Any, Mapping, Optional, Union


def _list(value: Union[str, list[str], None]) -> Optional[list[str]]:
    if value is None:
        return None
    if isinstance(value, str):
        return [value]
    return value


class Emails:
    @classmethod
    def send(cls, params: Mapping[str, Any]) -> Any:
        import pigeon

        body = dict(params)
        if "replyTo" in body and "reply_to" not in body:
            body["reply_to"] = body.pop("replyTo")
        for key in ("to", "cc", "bcc", "reply_to"):
            if key in body:
                body[key] = _list(body[key])
        return pigeon.default_http_client.request("POST", "/api/emails", body)

    @classmethod
    def list(cls, status: Optional[str] = None, q: Optional[str] = None) -> Any:
        import pigeon

        return pigeon.default_http_client.request("GET", "/api/emails", query={"status": status, "q": q})

    @classmethod
    def get(cls, email_id: str) -> Any:
        import pigeon

        return pigeon.default_http_client.request("GET", f"/api/emails/{email_id}")

    @classmethod
    def cancel(cls, email_id: str) -> Any:
        import pigeon

        return pigeon.default_http_client.request("POST", f"/api/emails/{email_id}/cancel")
