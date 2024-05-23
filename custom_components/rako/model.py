"""Rako shared models."""
from __future__ import annotations

from asyncio import Task
from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    from .bridge import RakoBridge
    from .light import RakoLight
    from .curtain import RakoCurtainEntity
    from .rgbw_switch import RakoRGBWSwitchEntity

class RakoDomainEntryData(TypedDict):
    """A single Rako config entry's data."""

    rako_bridge_client: RakoBridge
    rako_light_map: dict[str, RakoLight]
    rako_curtain_map: dict[str, RakoCurtainEntity]
    rako_rgbw_switch_map: dict[str, RakoRGBWSwitchEntity]
    rako_listener_task: Task | None
