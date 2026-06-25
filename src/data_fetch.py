"""Data fetch placeholders for future pitch-level baseball data ingestion.

No data is downloaded in the v0.1 skeleton.
"""

from pathlib import Path

from src.config import RAW_DATA_DIR


def get_raw_data_dir() -> Path:
    """Return the relative project raw data directory path."""
    return RAW_DATA_DIR


def data_download_enabled() -> bool:
    """Indicate whether this version performs remote data downloads."""
    return False
