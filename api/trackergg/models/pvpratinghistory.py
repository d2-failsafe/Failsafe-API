# generated by datamodel-codegen:
#   filename:  pvpratinghis.json
#   timestamp: 2022-01-29T11:48:23+00:00

from __future__ import annotations

from typing import Any, List, Union, Optional

from pydantic import BaseModel


class Metadata(BaseModel):
    key: str
    name: str
    description: Any


class Datum(BaseModel):
    value: int
    displayValue: str
    displayType: str


class ValorRating(BaseModel):
    metadata: Metadata
    data: List[List[Union[str, Datum]]]


class Metadata1(BaseModel):
    key: str
    name: str
    description: Any


class Datum1(BaseModel):
    value: int
    displayValue: str
    displayType: str


class GloryRating(BaseModel):
    metadata: Metadata1
    data: List[List[Union[str, Datum1]]]


class Metadata2(BaseModel):
    key: str
    name: str
    description: Any


class Datum2(BaseModel):
    value: int
    displayValue: str
    displayType: str


class InfamyRating(BaseModel):
    metadata: Metadata2
    data: List[List[Union[str, Datum2]]]


class Metadata3(BaseModel):
    key: str
    name: str
    description: Any


class Datum3(BaseModel):
    value: float
    displayValue: str
    displayType: str


class Kd(BaseModel):
    metadata: Metadata3
    data: List[List[Union[str, Datum3]]]


class Metadata4(BaseModel):
    key: str
    name: str
    description: Any


class Datum4(BaseModel):
    value: float
    displayValue: str
    displayType: str


class Wl(BaseModel):
    metadata: Metadata4
    data: List[List[Union[str, Datum4]]]


class Series(BaseModel):
    ValorRating: ValorRating
    GloryRating: GloryRating
    InfamyRating: InfamyRating
    Kd: Kd
    Wl: Wl


class PVPRatingHistory(BaseModel):
    series: Series
