"""Player lookup helpers for dashboard defaults and Statcast filtering."""

from __future__ import annotations

from dataclasses import dataclass

from src.config import DEFAULT_PLAYER


@dataclass(frozen=True)
class Player:
    """Minimal player metadata needed by the dashboard."""

    name: str
    mlbam_id: int | None = None


PETE_CROW_ARMSTRONG = Player(name=DEFAULT_PLAYER, mlbam_id=691718)

_PLAYERS = [PETE_CROW_ARMSTRONG]
_PLAYER_BY_NAME = {player.name: player for player in _PLAYERS}


def get_default_player() -> str:
    """Return the default dashboard player."""
    return DEFAULT_PLAYER


def get_player_options() -> list[str]:
    """Return available player names for the dashboard selector."""
    return [player.name for player in _PLAYERS]


def get_player(name: str = DEFAULT_PLAYER) -> Player:
    """Return player metadata for a display name."""
    return _PLAYER_BY_NAME.get(name, Player(name=name))


def get_pete_crow_armstrong() -> Player:
    """Return Pete Crow-Armstrong metadata, including MLBAM id."""
    return PETE_CROW_ARMSTRONG
