"""Project configuration for relative paths and application constants."""

from pathlib import Path

APP_TITLE = "DamageModel"
APP_SUBTITLE = "Cubs Baseball Probability Engine"
DEFAULT_PLAYER = "Pete Crow-Armstrong"

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
MODELS_DIR = PROJECT_ROOT / "models"
