# generated by datamodel-codegen:
#   filename:  character.json
#   timestamp: 2022-01-29T11:18:48+00:00

from __future__ import annotations

from typing import List, Optional

from pydantic import Field, BaseModel


class Metadata(BaseModel):
    backgroundImage: str
    emblemImage: str
    lightLevel: str
    level: str
    class_: str = Field(..., alias='class')
    race: str


class Attributes(BaseModel):
    mobility: int
    resilience: int
    recovery: int


class Super(BaseModel):
    name: str
    imageUrl: str
    description: str


class Metadata1(BaseModel):
    hash: int
    slug: str
    imageUrl: str
    screenshotUrl: Optional[str]
    name: str
    subTitle: str
    damageType: str
    primaryStat: Optional[int]
    rating: Optional[float]
    subclassPath: Optional[str] = None
    super: Optional[Super] = None


class Perk(BaseModel):
    name: str
    imageUrl: str
    description: Optional[str]


class GearItem(BaseModel):
    isSubClass: bool
    metadata: Metadata1
    perks: Optional[List[Perk]]


class Character(BaseModel):
    id: str
    activeCharacter: bool
    metadata: Metadata
    attributes: Attributes
    gear: List[GearItem]