# DamageModel

DamageModel is a Streamlit dashboard for building a baseball pitch-level damage model and Chicago Cubs player views.

## Current Status

Version `v0.2` adds Statcast data ingestion and local parquet caching. It does **not** train models yet.

## Dashboard

The app displays:

- Title: **DamageModel**
- Subtitle: **Cubs Baseball Probability Engine**
- Default selected player: **Pete Crow-Armstrong**
- Statcast loading summary:
  - total pitches loaded
  - loaded date range
  - Pete Crow-Armstrong pitch count
  - first 20 Pete Crow-Armstrong rows
- Placeholder sections for future modeling views:
  1. Player Skill Profile
  2. Pitch Type Matchup Matrix
  3. Location Heatmaps
  4. Movement Profile Map
  5. Matchup Simulator
  6. Model Evaluation

## Statcast Data Cache

`src/data_fetch.py` uses `pybaseball` to pull pitch-level Statcast data for:

- 2025 regular season
- 2026 season-to-date

Raw Statcast data is cached in `data/raw/` as parquet files. If a matching cached parquet file already exists, the app loads from cache instead of downloading again.

Development sample mode is enabled by default so local, Codex, and Replit startup can run faster. In sample mode, each season pulls only the first configured regular-season dates. To fetch full configured season windows, set:

```bash
export DAMAGE_SAMPLE_MODE=false
```

Optional sample size override:

```bash
export DAMAGE_SAMPLE_DAYS_PER_SEASON=7
```

All data, model, and cache paths are relative to this repository. No absolute local paths are required.

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

4. For full Statcast pulls instead of sample mode:

   ```bash
   DAMAGE_SAMPLE_MODE=false streamlit run app.py
   ```

## Replit Import and Run

This repository is configured for Codex → GitHub → Replit import → live preview.

1. Import the GitHub repository into Replit.
2. Let Replit install dependencies from `requirements.txt`.
3. Start the app with the configured run command, or run manually:

   ```bash
   streamlit run app.py --server.port 8080 --server.address 0.0.0.0
   ```

The `.replit` file uses `app.py` as the Streamlit entry point and binds Streamlit to port `8080` on `0.0.0.0` for Replit preview compatibility. `replit.nix` provides Python and pip for the Replit environment.

## Future Work

Planned future phases include:

- Feature engineering for pitch type, location, and movement
- Damage probability modeling
- Cubs-focused matchup simulation and model evaluation views
