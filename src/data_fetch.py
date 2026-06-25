"""Fetch and cache pitch-level Statcast data."""

from __future__ import annotations

from datetime import date, timedelta
from pathlib import Path

import pandas as pd
from pybaseball import cache, statcast

from src.config import (
    RAW_DATA_DIR,
    REGULAR_SEASON_DATES,
    SAMPLE_DAYS_PER_SEASON,
    SAMPLE_MODE,
    STATCAST_CACHE_PREFIX,
    STATCAST_SEASONS,
)
from src.player_lookup import Player, get_pete_crow_armstrong

DATE_FORMAT = "%Y-%m-%d"


def get_raw_data_dir() -> Path:
    """Return the project raw data directory path, creating it if needed."""
    RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)
    return RAW_DATA_DIR


def data_download_enabled() -> bool:
    """Indicate that this version can perform remote Statcast downloads."""
    return True


def _date_to_string(value: date) -> str:
    return value.strftime(DATE_FORMAT)


def get_statcast_date_range(season: int, sample_mode: bool = SAMPLE_MODE) -> tuple[date, date]:
    """Return the regular-season date range to fetch for a season."""
    start_date, end_date = REGULAR_SEASON_DATES[season]
    if sample_mode:
        end_date = min(end_date, start_date + timedelta(days=SAMPLE_DAYS_PER_SEASON - 1))
    return start_date, end_date


def get_statcast_cache_path(season: int, sample_mode: bool = SAMPLE_MODE) -> Path:
    """Return the parquet cache path for a season and mode."""
    suffix = "sample" if sample_mode else "full"
    return get_raw_data_dir() / f"{STATCAST_CACHE_PREFIX}_{season}_{suffix}.parquet"


def fetch_statcast_season(season: int, sample_mode: bool = SAMPLE_MODE, force_refresh: bool = False) -> pd.DataFrame:
    """Load a season of pitch-level Statcast data from cache or pybaseball."""
    cache_path = get_statcast_cache_path(season, sample_mode)
    if cache_path.exists() and not force_refresh:
        return pd.read_parquet(cache_path)

    start_date, end_date = get_statcast_date_range(season, sample_mode)
    cache.enable()
    data = statcast(start_dt=_date_to_string(start_date), end_dt=_date_to_string(end_date))

    # Normalize date values before parquet write/read so downstream UI is stable.
    if "game_date" in data.columns:
        data["game_date"] = pd.to_datetime(data["game_date"], errors="coerce")

    data.to_parquet(cache_path, index=False)
    return data


def load_statcast_data(sample_mode: bool = SAMPLE_MODE, force_refresh: bool = False) -> pd.DataFrame:
    """Load all configured Statcast seasons into one DataFrame."""
    frames = [fetch_statcast_season(season, sample_mode, force_refresh) for season in STATCAST_SEASONS]
    if not frames:
        return pd.DataFrame()
    return pd.concat(frames, ignore_index=True)


def filter_player_pitches(data: pd.DataFrame, player: Player | None = None) -> pd.DataFrame:
    """Return Statcast pitches where the selected player is the batter."""
    if data.empty:
        return data.copy()

    player = player or get_pete_crow_armstrong()
    if player.mlbam_id is not None and "batter" in data.columns:
        return data[data["batter"] == player.mlbam_id].copy()
    if "player_name" in data.columns:
        return data[data["player_name"].eq(player.name)].copy()
    return data.iloc[0:0].copy()
