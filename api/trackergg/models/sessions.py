# generated by datamodel-codegen:
#   filename:  sessions.json
#   timestamp: 2022-01-29T10:38:41+00:00

from __future__ import annotations

from typing import Any, Dict, List, Optional

from pydantic import Field, BaseModel


class StartDate(BaseModel):
    value: str
    displayValue: str


class EndDate(BaseModel):
    value: str
    displayValue: str


class Duration(BaseModel):
    value: str
    displayValue: str


class IsActive(BaseModel):
    value: bool
    displayValue: str


class Metadata(BaseModel):
    startDate: StartDate
    endDate: EndDate
    duration: Duration
    isActive: IsActive


class EndDate1(BaseModel):
    value: str
    displayValue: str


class Result(BaseModel):
    value: str
    displayValue: str


class ResultColor(BaseModel):
    value: Optional[str]
    displayValue: Optional[str]


class Completed(BaseModel):
    value: str
    displayValue: str


class Class(BaseModel):
    value: str
    displayValue: str


class Playlist(BaseModel):
    value: int
    displayValue: str


class Map(BaseModel):
    value: str
    displayValue: str


class PlaylistIconUrl(BaseModel):
    value: str
    displayValue: str


class AvgKd(BaseModel):
    kd: Any
    pct: Any


class Metadata1(BaseModel):
    endDate: EndDate1
    result: Result
    resultColor: ResultColor
    completed: Completed
    class_: Class = Field(..., alias="class")
    playlist: Playlist
    map: Map
    playlistIconUrl: PlaylistIconUrl
    avgKd: AvgKd


class Score(BaseModel):
    rank: Any
    percentile: Any
    displayName: str
    displayCategory: Any
    category: Any
    metadata: Dict[str, Any]
    value: int
    displayValue: str
    displayType: str


class Assists(BaseModel):
    rank: Any
    percentile: Any
    displayName: str
    displayCategory: Any
    category: Any
    metadata: Dict[str, Any]
    value: int
    displayValue: str
    displayType: str


class Deaths(BaseModel):
    rank: Any
    percentile: Any
    displayName: str
    displayCategory: Any
    category: Any
    metadata: Dict[str, Any]
    value: int
    displayValue: str
    displayType: str


class Kills(BaseModel):
    rank: Any
    percentile: Any
    displayName: str
    displayCategory: Any
    category: Any
    metadata: Dict[str, Any]
    value: int
    displayValue: str
    displayType: str


class Kd(BaseModel):
    rank: Any
    percentile: Any
    displayName: str
    displayCategory: Any
    category: Any
    metadata: Dict[str, Any]
    value: float
    displayValue: str
    displayType: str


class Kda(BaseModel):
    rank: Any
    percentile: Any
    displayName: str
    displayCategory: Any
    category: Any
    metadata: Dict[str, Any]
    value: float
    displayValue: str
    displayType: str


class Metadata2(BaseModel):
    iconUrl: str


class Glory(BaseModel):
    rank: Any
    percentile: Any
    displayName: str
    displayCategory: Any
    category: Any
    metadata: Metadata2
    value: Any
    displayValue: Any
    displayType: str


class Elo(BaseModel):
    rank: Any
    percentile: Any
    displayName: str
    displayCategory: Any
    category: Any
    metadata: Dict[str, Any]
    value: int
    displayValue: str
    displayType: str


class EloDelta(BaseModel):
    rank: Any
    percentile: Any
    displayName: str
    displayCategory: Any
    category: Any
    metadata: Dict[str, Any]
    value: int
    displayValue: str
    displayType: str


class Stats(BaseModel):
    score: Score
    assists: Assists
    deaths: Deaths
    kills: Kills
    kd: Kd
    kda: Kda
    glory: Glory
    elo: Optional[Elo] = None
    eloDelta: Optional[EloDelta] = None


class Match(BaseModel):
    id: str
    metadata: Metadata1
    stats: Stats


class Wins(BaseModel):
    rank: Any
    percentile: Any
    displayName: str
    displayCategory: Any
    category: Any
    metadata: Dict[str, Any]
    value: int
    displayValue: str
    displayType: str


class Losses(BaseModel):
    rank: Any
    percentile: Any
    displayName: str
    displayCategory: Any
    category: Any
    metadata: Dict[str, Any]
    value: int
    displayValue: str
    displayType: str


class WlPercentage(BaseModel):
    rank: Any
    percentile: Any
    displayName: str
    displayCategory: Any
    category: Any
    metadata: Dict[str, Any]
    value: int
    displayValue: str
    displayType: str


class Kills1(BaseModel):
    rank: Any
    percentile: Any
    displayName: str
    displayCategory: Any
    category: Any
    metadata: Dict[str, Any]
    value: int
    displayValue: str
    displayType: str


class Kd1(BaseModel):
    rank: Any
    percentile: Any
    displayName: str
    displayCategory: Any
    category: Any
    metadata: Dict[str, Any]
    value: float
    displayValue: str
    displayType: str


class Kda1(BaseModel):
    rank: Any
    percentile: Any
    displayName: str
    displayCategory: Any
    category: Any
    metadata: Dict[str, Any]
    value: float
    displayValue: str
    displayType: str


class Stats1(BaseModel):
    wins: Wins
    losses: Losses
    wlPercentage: WlPercentage
    kills: Kills1
    kd: Kd1
    kda: Kda1


class Item(BaseModel):
    metadata: Metadata
    matches: List[Match]
    stats: Stats1
    playlists: List


class Sessions(BaseModel):
    expiryDate: str
    items: List[Item]
