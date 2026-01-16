import pandas as pd
import os

# Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "..", "data", "processed")
OUTPUT_PATH = os.path.join(BASE_DIR, "..", "outputs")

os.makedirs(OUTPUT_PATH, exist_ok=True)

# Load cleaned data
df = pd.read_csv(
    os.path.join(DATA_PATH, "cleaned_demographic_daily.csv"),
    parse_dates=["date"]
)

print("Loaded cleaned data:", df.shape)

# -------------------------------
# STEP 1: Monthly Aggregation
# -------------------------------

df["year_month"] = df["date"].dt.to_period("M")

monthly_df = (
    df.groupby(["state", "district", "year_month"])
      .agg(
          monthly_updates=("total_demographic_updates", "sum"),
          avg_youth_ratio=("youth_update_ratio", "mean")
      )
      .reset_index()
)

monthly_df["year_month"] = monthly_df["year_month"].astype(str)

print("Monthly aggregation complete:", monthly_df.shape)

# -------------------------------
# STEP 2: Migration Spike Score
# -------------------------------

monthly_df["rolling_6m_avg"] = (
    monthly_df
    .groupby(["state", "district"])["monthly_updates"]
    .transform(lambda x: x.rolling(6, min_periods=1).mean())
)

monthly_df["migration_spike_score"] = (
    monthly_df["monthly_updates"] / monthly_df["rolling_6m_avg"]
)

# -------------------------------
# STEP 3: Flag anomalies
# -------------------------------

monthly_df["spike_flag"] = monthly_df["migration_spike_score"].apply(
    lambda x: "HIGH_SPIKE" if x >= 1.5 else "NORMAL"
)

# -------------------------------
# Save outputs
# -------------------------------

monthly_df.to_csv(
    os.path.join(OUTPUT_PATH, "monthly_migration_trends.csv"),
    index=False
)

print("\n✅ Monthly migration trends saved")
print(monthly_df.head())
