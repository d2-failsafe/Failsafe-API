import enum
from json import JSONDecodeError
from typing import Any, Dict, Optional

import httpx
from pyrate_limiter import Limiter, Duration, RequestRate

from ...utils.ua import get_ua
from ...utils.enums import RequestMethods
from .models.manifest import Manifest
from ...utils.exceptions import APIError, APICallFailed

limiter = Limiter(RequestRate(1, Duration.SECOND))


class URL(str, enum.Enum):
    BASE = "https://www.bungie.net"
    API_ENDPOINT = "/Platform"
    API = BASE + API_ENDPOINT


class API:
    def __init__(self, api_key: str, **kwargs) -> None:
        headers = {"X-API-Key": api_key, "User-Agent": get_ua()}
        self.client = httpx.AsyncClient(headers=headers, **kwargs)

    @limiter.ratelimit(delay=True)
    async def call(
        self,
        method: RequestMethods,
        path: str,
        params: Optional[Dict[Any, Any]] = None,
        **kwargs,
    ) -> Dict[Any, Any]:
        async with self.client as client:
            response = await client.request(
                method, URL.API + path, params=params, **kwargs
            )

        if response.status_code != 200:
            raise APICallFailed(response.status_code)

        try:
            resp: dict = response.json()
        except JSONDecodeError:
            raise APIError(
                0, "Unknown", "JSON Decode Error. Check endpoint spelling and params."
            )

        if errc := resp.get("ErrorCode") != 1:
            raise APIError(
                errc,
                resp.get("ErrorStatus", "Unknown"),
                resp.get("Message", "Unknown"),
            )

        return resp

    async def get_destiny_manifest(self) -> Manifest:
        resp = await self.call(RequestMethods.GET, "/Destiny2/Manifest/")
        return Manifest(**resp)
