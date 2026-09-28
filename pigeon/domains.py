from typing import Any, Mapping, Union


class Domains:
    @classmethod
    def list(cls) -> Any:
        import pigeon

        return pigeon.default_http_client.request("GET", "/api/domains")

    @classmethod
    def create(cls, name_or_params: Union[str, Mapping[str, Any]]) -> Any:
        import pigeon

        body = {"name": name_or_params} if isinstance(name_or_params, str) else dict(name_or_params)
        return pigeon.default_http_client.request("POST", "/api/domains", body)

    @classmethod
    def verify(cls, domain_id: str) -> Any:
        import pigeon

        return pigeon.default_http_client.request("POST", f"/api/domains/{domain_id}/verify")

    @classmethod
    def remove(cls, domain_id: str) -> Any:
        import pigeon

        return pigeon.default_http_client.request("DELETE", f"/api/domains/{domain_id}")
