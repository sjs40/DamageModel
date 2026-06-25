"""Project configuration for relative paths and application constants."""

from __future__ import annotations

import os
from datetime import date
from pathlib import Path

APP_TITLE = "DamageModel"
APP_SUBTITLE = "Cubs Baseball Probability Engine"
DEFAULT_PLAYER = "Pete Crow-Armstrong"

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
MODELS_DIR = PROJECT_ROOT / "models"

STATCAST_CACHE_PREFIX = "statcast"
STATCAST_SEASONS = (2025, 2026)

# Regular season date windows. Keep these centralized so the fetcher and UI agree.
REGULAR_SEASON_DATES = {
    2025: (date(2025, 3, 27), date(2025, 9, 28)),
    2026: (date(2026, 3, 25), date.today()),
}

# Development-friendly sample mode. Set DAMAGE_SAMPLE_MODE=false to fetch full seasons.
SAMPLE_MODE = os.getenv("DAMAGE_SAMPLE_MODE", "true").lower() in {"1", "true", "yes", "on"}
SAMPLE_DAYS_PER_SEASON = int(os.getenv("DAMAGE_SAMPLE_DAYS_PER_SEASON", "7"))
