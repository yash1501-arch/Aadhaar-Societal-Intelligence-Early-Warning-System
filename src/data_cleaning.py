import pandas as pd
import os

# Absolute paths (works from anywhere)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RAW_PATH = os.path.join(BASE_DIR, "..", "data", "raw")
PROCESSED_PATH = os.path.join(BASE_DIR, "..", "data", "processed")

files = [
    "api_data_aadhar_demographic_0_500000.csv",
    "api_data_aadhar_demographic_500000_1000000.csv",
    "api_data_aadhar_demographic_1000000_1500000.csv",
    "api_data_aadhar_demographic_1500000_2000000.csv",
    "api_data_aadhar_demographic_2000000_2071700.csv"
]

# Load and merge
df_list = []
for f in files:
    file_path = os.path.join(RAW_PATH, f)
    print("Loading:", file_path)
    df_list.append(pd.read_csv(file_path))

df = pd.concat(df_list, ignore_index=True)
print("Initial rows:", df.shape[0])

# Remove duplicates
df = df.drop_duplicates()
print("Rows after duplicate removal:", df.shape[0])

# Normalize columns
df.columns = df.columns.str.strip().str.lower()

# Rename broken column
df = df.rename(columns={"demo_age_17_": "demo_age_18_plus"})

# Convert date
df["date"] = pd.to_datetime(df["date"], format="%d-%m-%Y", errors="coerce")

# Clean text
df["state"] = df["state"].str.strip().str.title()
df["district"] = df["district"].str.strip().str.title()

# Pincode as string
df["pincode"] = df["pincode"].astype(str)

# Drop invalid rows
df = df.dropna(subset=["date", "state", "district"])

# Feature engineering
df["total_demographic_updates"] = df["demo_age_5_17"] + df["demo_age_18_plus"]
df["youth_update_ratio"] = df["demo_age_5_17"] / df["total_demographic_updates"]

# Save output
os.makedirs(PROCESSED_PATH, exist_ok=True)
output_file = os.path.join(PROCESSED_PATH, "cleaned_demographic_daily.csv")
df.to_csv(output_file, index=False)

print("\n✅ CLEANED DATA SAVED SUCCESSFULLY")
print(df.head())
print("\nData types:\n", df.dtypes)
