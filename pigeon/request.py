from __future__ import annotations

import json
import os
import urllib.error
import urllib.parse
import urllib.request
from typing import Any, Mapping, Optional


class PigeonError(Exception):
    def __init__(self, message: str, status_code: int | None = None, name: str | None = None, body: Any = None):
        super().__init__(message)
        self.status_code = status_code
        self.name = name or "pigeon_error"
        self.body = body


class Request:
    def request(
        self,
        method: str,
        path: str,
        json_body: Optional[Mapping[str, Any]] = None,
        query: Optional[Mapping[str, Any]] = None,
    ) -> Any:
        import pigeon

        api_key = pigeon.api_key or os.environ.get("PIGEON_API_KEY")
        if not api_key:
            raise PigeonError("Pigeon API key is required. Set pigeon.api_key or PIGEON_API_KEY.")

        base = (pigeon.base_url or os.environ.get("PIGEON_BASE_URL") or "http://localhost:4005").rstrip("/")
        url = base + path
        if query:
            params = {k: str(v) for k, v in query.items() if v is not None and v != ""}
            if params:
                url += "?" + urllib.parse.urlencode(params)

        data = None if json_body is None else json.dumps(json_body).encode("utf-8")
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Accept": "application/json",
            "User-Agent": "pigeon-python/0.1.0",
        }
        if data is not None:
            headers["Content-Type"] = "application/json"

        req = urllib.request.Request(url, data=data, headers=headers, method=method)
        try:
            with urllib.request.urlopen(req) as response:
                raw = response.read().decode("utf-8")
                return json.loads(raw) if raw else None
        except urllib.error.HTTPError as error:
            raw = error.read().decode("utf-8")
            try:
                body = json.loads(raw) if raw else {}
            except json.JSONDecodeError:
                body = {"message": raw}
            raise PigeonError(
                body.get("message") or error.reason,
                status_code=error.code,
                name=body.get("name"),
                body=body,
            ) from error
