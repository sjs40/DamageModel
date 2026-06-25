"""Player lookup helpers for dashboard defaults and future roster integration."""

from src.config import DEFAULT_PLAYER


_INITIAL_CUBS_PLAYERS = [
    DEFAULT_PLAYER,
]


def get_default_player() -> str:
    """Return the default dashboard player."""
    return DEFAULT_PLAYER


def get_player_options() -> list[str]:
    """Return available player names for the initial dashboard selector."""
    return _INITIAL_CUBS_PLAYERS.copy()
