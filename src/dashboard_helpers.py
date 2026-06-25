"""Reusable Streamlit rendering helpers for the dashboard skeleton."""

import streamlit as st


def render_placeholder_section(title: str, selected_player: str) -> None:
    """Render a named placeholder dashboard section."""
    with st.container(border=True):
        st.header(title)
        st.write(
            f"Placeholder for {selected_player}. This section will be populated "
            "after data ingestion, feature engineering, and model development are added."
        )
