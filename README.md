# DamageModel

DamageModel is an initial Streamlit skeleton for a baseball pitch-level damage model and Chicago Cubs dashboard.

## Current Status

Version `v0.1` is intentionally a project scaffold only. It includes a runnable Streamlit app with placeholder dashboard sections, but it does **not** download data or build models yet.

## Dashboard

The app currently displays:

- Title: **DamageModel**
- Subtitle: **Cubs Baseball Probability Engine**
- Default selected player: **Pete Crow-Armstrong**
- Placeholder sections:
  1. Player Skill Profile
  2. Pitch Type Matchup Matrix
  3. Location Heatmaps
  4. Movement Profile Map
  5. Matchup Simulator
  6. Model Evaluation

## Project Structure

```text
.
├── app.py
├── requirements.txt
├── README.md
├── .replit
├── replit.nix
├── src/
│   ├── config.py
│   ├── data_fetch.py
│   ├── player_lookup.py
│   └── dashboard_helpers.py
├── data/
│   ├── raw/
│   └── processed/
└── models/
```

All data, model, and cache locations are represented by relative project paths. The `data/raw/`, `data/processed/`, and `models/` directories are present for future development and currently contain only `.gitkeep` files.

## Local Setup

1. Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

   On Windows PowerShell:

   ```powershell
   python -m venv .venv
   .venv\Scripts\Activate.ps1
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the app locally:

   ```bash
   streamlit run app.py
   ```

## Replit Import and Run

This repository is configured for Codex → GitHub → Replit import → live preview.

1. Import the GitHub repository into Replit.
2. Let Replit install dependencies from `requirements.txt`.
3. Start the app with the configured run command, or run manually:

   ```bash
   streamlit run app.py --server.port 8080 --server.address 0.0.0.0
   ```

The `.replit` file uses `app.py` as the Streamlit entry point and binds Streamlit to port `8080` on `0.0.0.0` for Replit preview compatibility.

## Future Work

Planned future phases include:

- Data ingestion for pitch-level MLB data
- Player lookup and roster enrichment
- Feature engineering for pitch type, location, and movement
- Damage probability modeling
- Cubs-focused matchup simulation and model evaluation views
