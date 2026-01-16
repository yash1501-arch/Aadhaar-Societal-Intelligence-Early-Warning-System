<<<<<<< HEAD
import pandas as pd
import os

# Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_PATH = os.path.join(BASE_DIR, "..", "outputs")
OUTPUT_PATH = os.path.join(BASE_DIR, "..", "outputs")

# Load monthly trends
df = pd.read_csv(
    os.path.join(INPUT_PATH, "monthly_migration_trends.csv")
)

print("Loaded monthly trends:", df.shape)

# -----------------------------------
# Clean invalid state/district values
# -----------------------------------
df = df[~df["state"].astype(str).str.isnumeric()]
df = df[~df["district"].astype(str).str.isnumeric()]

# -----------------------------------
# District Stress Metrics
# -----------------------------------

district_stress = (
    df.groupby(["state", "district"])
      .agg(
          total_months=("year_month", "count"),
          spike_months=("spike_flag", lambda x: (x == "HIGH_SPIKE").sum()),
          avg_spike_score=("migration_spike_score", "mean"),
          max_spike_score=("migration_spike_score", "max"),
          avg_monthly_updates=("monthly_updates", "mean")
      )
      .reset_index()
)

# -----------------------------------
# Stress Index (Composite Score)
# -----------------------------------

district_stress["stress_index"] = (
    (district_stress["spike_months"] / district_stress["total_months"]) * 0.5 +
    (district_stress["avg_spike_score"] / district_stress["avg_spike_score"].max()) * 0.3 +
    (district_stress["avg_monthly_updates"] / district_stress["avg_monthly_updates"].max()) * 0.2
)

# -----------------------------------
# Rank districts
# -----------------------------------

district_stress = district_stress.sort_values(
    by="stress_index", ascending=False
)

# -----------------------------------
# Save Top 10 Stress Districts
# -----------------------------------

top_10 = district_stress.head(10)

top_10.to_csv(
    os.path.join(OUTPUT_PATH, "top_10_stress_districts.csv"),
    index=False
)

print("\n✅ TOP 10 STRESS DISTRICTS IDENTIFIED")
print(top_10)
=======
import pandas as pd
import os

# Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_PATH = os.path.join(BASE_DIR, "..", "outputs")
OUTPUT_PATH = os.path.join(BASE_DIR, "..", "outputs")

# Load monthly trends
df = pd.read_csv(
    os.path.join(INPUT_PATH, "monthly_migration_trends.csv")
)

print("Loaded monthly trends:", df.shape)

# -----------------------------------
# Clean invalid state/district values
# -----------------------------------
df = df[~df["state"].astype(str).str.isnumeric()]
df = df[~df["district"].astype(str).str.isnumeric()]

# -----------------------------------
# District Stress Metrics
# -----------------------------------

district_stress = (
    df.groupby(["state", "district"])
      .agg(
          total_months=("year_month", "count"),
          spike_months=("spike_flag", lambda x: (x == "HIGH_SPIKE").sum()),
          avg_spike_score=("migration_spike_score", "mean"),
          max_spike_score=("migration_spike_score", "max"),
          avg_monthly_updates=("monthly_updates", "mean")
      )
      .reset_index()
)

# -----------------------------------
# Stress Index (Composite Score)
# -----------------------------------

district_stress["stress_index"] = (
    (district_stress["spike_months"] / district_stress["total_months"]) * 0.5 +
    (district_stress["avg_spike_score"] / district_stress["avg_spike_score"].max()) * 0.3 +
    (district_stress["avg_monthly_updates"] / district_stress["avg_monthly_updates"].max()) * 0.2
)

# -----------------------------------
# Rank districts
# -----------------------------------

district_stress = district_stress.sort_values(
    by="stress_index", ascending=False
)

# -----------------------------------
# Save Top 10 Stress Districts
# -----------------------------------

top_10 = district_stress.head(10)

top_10.to_csv(
    os.path.join(OUTPUT_PATH, "top_10_stress_districts.csv"),
    index=False
)

print("\n✅ TOP 10 STRESS DISTRICTS IDENTIFIED")
print(top_10)
>>>>>>> 825d192ee9dc8ff5db09dc33fc2b47a479077e75
