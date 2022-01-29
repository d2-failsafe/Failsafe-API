import typing
import asyncio
from json import JSONDecodeError
from urllib.parse import quote

import httpx
from pyrate_limiter import Limiter, Duration, RequestRate

from utils.ua import get_ua
from utils.enums import RequestMethods
from utils.exceptions import APIError, APICallFailed

from .models import (
    ID,
    Sessions,
    Character,
    PVPSeason,
    PVPWeapon,
    PVPHistory,
    PlayerProfile,
    PVPRatingHistory,
)

if typing.TYPE_CHECKING:
    from typing import Any, Dict, List, Union, Optional

limiter = Limiter(RequestRate(15, Duration.MINUTE))


class BaseAPI:
    def __init__(self, id: str, **kwargs) -> None:
        self.client = httpx.AsyncClient(**kwargs)
        self.id = asyncio.run(self.get_id(id))[0].platformUserIdentifier

    async def call(
        self,
        method: RequestMethods,
        url: str,
        params: Optional[Dict[Any, Any]] = None,
        **kwargs,
    ) -> Dict[Any, Any]:
        async with self.client as client:
            header = {
                "User-Agent": get_ua(),
                "origin": "https://destinytracker.com",
                "referer": "https://destinytracker.com/",
            }
            response = await client.request(
                method, url, params=params, headers=header, **kwargs
            )

        if response.status_code != 200:
            raise APICallFailed(response.status_code)

        try:
            resp: Dict[Any, Any] = response.json()
        except JSONDecodeError:
            raise APIError(
                0, "Unknown", "JSON Decode Error. Check endpoint spelling and params."
            )
        return resp["data"]

    async def get_id(self, id: str, platform: str = "bungie") -> List[ID]:
        """
        :说明: `get_id`
        > 根据游戏内ID获取其他API所需的ID

        :参数:
          * `id: str`: 游戏内ID

        :可选参数:
          * `platform: str = "bungie"`: 游戏平台，如不清楚请勿修改

        :返回:
          - `List[ID]`: 可能的ID列表
        """
        url = "https://api.tracker.gg/api/v2/destiny-2/standard/search"
        params = {"platform": platform, "query": quote(id)}
        data = await self.call(RequestMethods.GET, url, params=params)
        return [ID(**d) for d in data]


class Profile(BaseAPI):
    async def get_profile(self) -> PlayerProfile:
        """
        :说明: `get_profile`
        > 获取玩家档案

        :参数:
          * `id: Union[int, str]`: ID

        :返回:
          - `PlayerProfile`: 玩家档案
        """
        url = (
            f"https://api.tracker.gg/api/v2/destiny-2/standard/profile/bungie/{self.id}"
        )
        data = await self.call(RequestMethods.GET, url)
        return PlayerProfile(**data)

    async def get_sessions(self) -> Sessions:
        """
        :说明: `get_sessions`
        > 获取玩家登录记录

        :参数:
          * `id: Union[int, str]`: ID

        :返回:
          - `Sessions`: 玩家登录记录
        """
        url = f"https://api.tracker.gg/api/v2/destiny-2/standard/profile/bungie/{self.id}/sessions"
        data = await self.call(RequestMethods.GET, url)
        return Sessions(**data)

    async def get_character(self) -> List[Character]:
        """
        :说明: `get_character`
        > 获取玩家人物信息

        :参数:
          * `id: Union[int, str]`: ID

        :返回:
          - `List[Character]`: 人物信息列表
        """
        url = f"https://api.tracker.gg/api/v1/destiny-2/stats/characters/17/{self.id}"
        data = await self.call(RequestMethods.GET, url)
        return [Character(**d) for d in data]


class PVP(BaseAPI):
    async def get_pvp_weapon(self) -> List[PVPWeapon]:
        """
        :说明: `get_pvp_weapon`
        > 获取玩家近30天内PVP武器击杀情况

        :参数:
          * `id: Union[int, str]`: ID

        :返回:
          - `List[PVPWeapon]`: PVP武器击杀情况列表
        """
        url = "https://api.tracker.gg/api/v1/destiny-2/stats/player-weapons"
        params = {"mode": 5, "uniqueId": id}
        data = await self.call(RequestMethods.GET, url, params=params)
        return [PVPWeapon(**d) for d in data]

    async def get_pvp_season(self, season: int) -> List[PVPSeason]:
        """
        :说明: `get_pvp_season`
        > 获取玩家赛季表现

        :参数:
          * `id: Union[int, str]`: ID
          * `season: int`: 赛季

        :返回:
          - `List[PVPSeason]`: 赛季各PVP活动表现列表
        """
        url = f"https://api.tracker.gg/api/v2/destiny-2/standard/profile/bungie/{self.id}/segments/playlist"
        params = {"season": season}
        data = await self.call(RequestMethods.GET, url, params=params)
        return [PVPSeason(**d) for d in data]

    async def get_pvp_history(self) -> PVPHistory:
        """
        :说明: `get_pvp_history`
        > 获取玩家最近50场PVP记录

        :参数:
          * `id: Union[int, str]`: ID

        :返回:
          - `PVPHistory`: PVP历史记录
        """
        url = f"https://api.tracker.gg/api/v2/destiny-2/standard/profile/bungie/{self.id}/sessions?perspective=pvp"
        data = await self.call(RequestMethods.GET, url)
        return PVPHistory(**data)

    async def get_pvp_ratinghistory(self) -> PVPRatingHistory:
        """
        :说明: `get_pvp_ratinghistory`
        > 获取玩家30天内PVP评级和KD变化

        :参数:
          * `id: Union[int, str]`: ID

        :返回:
          - `PVPRatingHistory`: PVP评级和KD变化
        """
        url = f"https://api.tracker.gg/api/v2/destiny-2/standard/profile/bungie/{self.id}/history"
        data = await self.call(RequestMethods.GET, url)
        return PVPRatingHistory(**data)


class PVE(BaseAPI):
    """WIP"""

    pass


class Database(BaseAPI):
    """WIP"""

    pass


class API(PlayerProfile, PVP, PVE, Database):
    """整合各个API"""

    pass
