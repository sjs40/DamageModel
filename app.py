"""Streamlit entry point for the DamageModel dashboard."""

import streamlit as st

from src.config import APP_SUBTITLE, APP_TITLE, DEFAULT_PLAYER
from src.dashboard_helpers import render_placeholder_section
from src.player_lookup import get_default_player, get_player_options


PLACEHOLDER_SECTIONS = [
    "Player Skill Profile",
    "Pitch Type Matchup Matrix",
    "Location Heatmaps",
    "Movement Profile Map",
    "Matchup Simulator",
    "Model Evaluation",
]


def main() -> None:
    """Render the initial Streamlit dashboard skeleton."""
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
        help="Initial placeholder selector for future player-specific model views.",
    )

    st.caption(
        "This v0.1 skeleton does not download data or build models yet. "
        f"Current player context: {selected_player or DEFAULT_PLAYER}."
    )

    st.divider()

    for section in PLACEHOLDER_SECTIONS:
        render_placeholder_section(section, selected_player)


if __name__ == "__main__":
    main()
