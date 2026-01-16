# Aadhaar Societal Intelligence & Early-Warning System

A Streamlit dashboard that analyzes Aadhaar demographic update data to surface migration signals, district stress scores, and policy recommendations.

**Repository layout**

- `dashboard/` — Streamlit app (`app.py`) that renders the dashboard.
- `data/processed/` — cleaned CSV data used by the dashboard.
  - `cleaned_demographic_daily.csv`
  - `cleaned_aadhar_data.csv`
- `data/raw/` — raw API dumps (kept for provenance).
- `outputs/` — generated CSV outputs used by the dashboard.
  - `monthly_migration_trends.csv`
  - `top_10_stress_districts.csv`
- `src/` — analysis and preprocessing scripts.

**Requirements**

- Python 3.10+ (Windows tested)
- Recommended packages: `streamlit`, `pandas`, `plotly`

Optional but useful dev tools: `venv` (builtin), `pip`.

Example minimal `requirements.txt` content:

```
streamlit>=1.20
pandas>=1.5
plotly>=5.0
```

**Installation (Windows)**

1. Create and activate virtual environment

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1   # PowerShell
# or .\.venv\Scripts\activate   # cmd.exe
```

2. Install dependencies

```powershell
pip install -r requirements.txt
# or install packages directly
pip install streamlit pandas plotly
```

**Run the dashboard**

python -m streamlit run dashboard/app.py

Recommended (Streamlit CLI):

```powershell
streamlit run dashboard/app.py
```

Alternative (direct Python run — may work but Streamlit CLI is preferred):

```powershell
python dashboard/app.py
```

Open `http://localhost:8501` in your browser if Streamlit doesn't open automatically.

**Data expectations**

The app expects these processed files (relative to repo root):

- `data/processed/cleaned_demographic_daily.csv` (parsed `date` column)
- `outputs/monthly_migration_trends.csv`
- `outputs/top_10_stress_districts.csv`

If any file is missing the app will raise a `FileNotFoundError` — ensure the `data/processed` and `outputs` folders contain the above CSVs.

**Notes & Troubleshooting**

- If Streamlit fails to import, ensure the venv is active and packages installed into that environment.
- When data is large, give pandas a moment to load; consider running preprocessing in `src/` to generate lighter `outputs/` files.

**Next steps I can do for you**

- Create a `requirements.txt` in the repo with pinned versions.
- Add a short `README` usage GIF or screenshots.
- Add a simple script to regenerate `outputs/` from `data/processed/`.

---

UIDAI Hackathon 2026 — Dashboard
=======
# Aadhaar Societal Intelligence & Early-Warning System

A Streamlit dashboard that analyzes Aadhaar demographic update data to surface migration signals, district stress scores, and policy recommendations.

**Repository layout**

- `dashboard/` — Streamlit app (`app.py`) that renders the dashboard.
- `data/processed/` — cleaned CSV data used by the dashboard.
  - `cleaned_demographic_daily.csv`
  - `cleaned_aadhar_data.csv`
- `data/raw/` — raw API dumps (kept for provenance).
- `outputs/` — generated CSV outputs used by the dashboard.
  - `monthly_migration_trends.csv`
  - `top_10_stress_districts.csv`
- `src/` — analysis and preprocessing scripts.

**Requirements**

- Python 3.10+ (Windows tested)
- Recommended packages: `streamlit`, `pandas`, `plotly`

Optional but useful dev tools: `venv` (builtin), `pip`.

Example minimal `requirements.txt` content:

```
streamlit>=1.20
pandas>=1.5
plotly>=5.0
```

**Installation (Windows)**

1. Create and activate virtual environment

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1   # PowerShell
# or .\.venv\Scripts\activate   # cmd.exe
```

2. Install dependencies

```powershell
pip install -r requirements.txt
# or install packages directly
pip install streamlit pandas plotly
```

**Run the dashboard**

python -m streamlit run dashboard/app.py

Recommended (Streamlit CLI):

```powershell
streamlit run dashboard/app.py
```

Alternative (direct Python run — may work but Streamlit CLI is preferred):

```powershell
python dashboard/app.py
```

Open `http://localhost:8501` in your browser if Streamlit doesn't open automatically.

**Data expectations**

The app expects these processed files (relative to repo root):

- `data/processed/cleaned_demographic_daily.csv` (parsed `date` column)
- `outputs/monthly_migration_trends.csv`
- `outputs/top_10_stress_districts.csv`

If any file is missing the app will raise a `FileNotFoundError` — ensure the `data/processed` and `outputs` folders contain the above CSVs.

**Notes & Troubleshooting**

- If Streamlit fails to import, ensure the venv is active and packages installed into that environment.
- When data is large, give pandas a moment to load; consider running preprocessing in `src/` to generate lighter `outputs/` files.

**Next steps I can do for you**

- Create a `requirements.txt` in the repo with pinned versions.
- Add a short `README` usage GIF or screenshots.
- Add a simple script to regenerate `outputs/` from `data/processed/`.

---

UIDAI Hackathon 2026 — Dashboard
825d192ee9dc8ff5db09dc33fc2b47a479077e75
