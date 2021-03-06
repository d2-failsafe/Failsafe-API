# generated by datamodel-codegen:
#   filename:  pvpweapon.json
#   timestamp: 2022-01-29T11:38:41+00:00

from __future__ import annotations

from pydantic import BaseModel


class PVPWeapon(BaseModel):
    hash: str
    name: str
    iconUrl: str
    kills: int
    precisionKills: int
    accuracy: float
