from dataclasses import dataclass
import typing as t
from datetime import datetime

@dataclass(frozen=True)
class PingResponse:
    is_alive: bool
    rtt: int
    date: datetime

@dataclass(frozen=True)
class Site:
    domain: str
    ip_address: str
    ports: t.Tuple[int]

