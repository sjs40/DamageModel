"""Streamlit entry point for the DamageModel dashboard."""

from __future__ import annotations

import pandas as pd
import streamlit as st

from src.config import APP_SUBTITLE, APP_TITLE, DEFAULT_PLAYER, SAMPLE_MODE
from src.dashboard_helpers import render_placeholder_section
from src.data_fetch import filter_player_pitches, load_statcast_data
from src.player_lookup import get_default_player, get_player, get_player_options


PLACEHOLDER_SECTIONS = [
    "Player Skill Profile",
    "Pitch Type Matchup Matrix",
    "Location Heatmaps",
    "Movement Profile Map",
    "Matchup Simulator",
    "Model Evaluation",
]


def _date_range_label(data: pd.DataFrame) -> str:
    """Return a compact date range label for Statcast data."""
    if data.empty or "game_date" not in data.columns:
        return "No dates loaded"

    dates = pd.to_datetime(data["game_date"], errors="coerce").dropna()
    if dates.empty:
        return "No valid dates loaded"
    return f"{dates.min().date()} to {dates.max().date()}"


@st.cache_data(show_spinner="Loading Statcast data...")
def _load_data(sample_mode: bool) -> pd.DataFrame:
    """Streamlit-cached wrapper around the local parquet/pybaseball loader."""
    return load_statcast_data(sample_mode=sample_mode)


def main() -> None:
    """Render the Streamlit dashboard."""
    st.set_page_config(page_title=APP_TITLE, page_icon="⚾", layout="wide")

    st.title(APP_TITLE)
    st.subheader(APP_SUBTITLE)

    player_options = get_player_options()
    default_player = get_default_player()
    default_index = player_options.index(default_player) if default_player in player_options else 0

    selected_player = st.selectbox(
        "Selected player",
        options=player_options,
        index=default_index,
        help="Player-specific Statcast context for model development.",
    )
    player = get_player(selected_player or DEFAULT_PLAYER)

    st.caption(
        "Statcast pitch data is cached as parquet in data/raw/. "
        f"Sample mode is {'on' if SAMPLE_MODE else 'off'}; set DAMAGE_SAMPLE_MODE=false for full-season pulls."
    )

    try:
        statcast_data = _load_data(SAMPLE_MODE)
        player_pitches = filter_player_pitches(statcast_data, player)
    except Exception as exc:  # Show app-friendly data errors without hiding the traceback details.
        st.error("Unable to load Statcast data. Check dependencies, network access, or cached parquet files.")
        st.exception(exc)
        statcast_data = pd.DataFrame()
        player_pitches = pd.DataFrame()

    metric_cols = st.columns(3)
    metric_cols[0].metric("Total pitches loaded", f"{len(statcast_data):,}")
    metric_cols[1].metric("Date range", _date_range_label(statcast_data))
    metric_cols[2].metric(f"{player.name} pitches", f"{len(player_pitches):,}")

    st.subheader(f"First 20 rows for {player.name}")
    st.dataframe(player_pitches.head(20), use_container_width=True)

    st.divider()

    for section in PLACEHOLDER_SECTIONS:
        render_placeholder_section(section, selected_player)


if __name__ == "__main__":
    main()
