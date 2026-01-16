import streamlit as st
import pandas as pd
import os
import plotly.express as px

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Aadhaar Societal Intelligence Dashboard",
    layout="wide"
)

st.title("🧠 Aadhaar Societal Intelligence & Early-Warning System")
st.markdown("""
This dashboard uncovers **societal trends, migration signals, and system stress**
from Aadhaar demographic update data to support **data-driven decision-making**.
""")

# -----------------------------
# Paths
# -----------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "..", "data", "processed")
OUTPUT_PATH = os.path.join(BASE_DIR, "..", "outputs")

# -----------------------------
# Load Data
# -----------------------------
@st.cache_data
def load_data():
    daily = pd.read_csv(
        os.path.join(DATA_PATH, "cleaned_demographic_daily.csv"),
        parse_dates=["date"]
    )
    monthly = pd.read_csv(
        os.path.join(OUTPUT_PATH, "monthly_migration_trends.csv")
    )
    stress = pd.read_csv(
        os.path.join(OUTPUT_PATH, "top_10_stress_districts.csv")
    )
    return daily, monthly, stress

daily_df, monthly_df, stress_df = load_data()

# -----------------------------
# Sidebar Filters
# -----------------------------
st.sidebar.header("🔍 Filters")

states = sorted(daily_df["state"].unique())
selected_state = st.sidebar.selectbox("Select State", ["All"] + states)

if selected_state != "All":
    monthly_df = monthly_df[monthly_df["state"] == selected_state]

# -----------------------------
# KPI Section
# -----------------------------
st.subheader("📊 Key Indicators")

col1, col2, col3 = st.columns(3)

col1.metric(
    "Total Demographic Updates",
    f"{daily_df['total_demographic_updates'].sum():,}"
)

col2.metric(
    "Districts with Spikes",
    monthly_df[monthly_df["spike_flag"] == "HIGH_SPIKE"]["district"].nunique()
)

col3.metric(
    "Highest Spike Score",
    round(monthly_df["migration_spike_score"].max(), 2)
)

# -----------------------------
# Trend Chart
# -----------------------------
st.subheader("📈 Monthly Demographic Update Trends")

trend_df = (
    monthly_df.groupby("year_month")["monthly_updates"]
    .sum()
    .reset_index()
)

fig_trend = px.line(
    trend_df,
    x="year_month",
    y="monthly_updates",
    markers=True,
    title="India-wide Monthly Demographic Updates"
)

st.plotly_chart(fig_trend, use_container_width=True)

# -----------------------------
# Migration Spike Heat
# -----------------------------
st.subheader("🚨 Migration Spike Analysis")

spike_df = monthly_df[monthly_df["spike_flag"] == "HIGH_SPIKE"]

fig_spike = px.scatter(
    spike_df,
    x="year_month",
    y="monthly_updates",
    color="state",
    size="migration_spike_score",
    hover_data=["district", "migration_spike_score"],
    title="High Migration Spike Events"
)

st.plotly_chart(fig_spike, use_container_width=True)

# -----------------------------
# Top Stress Districts
# -----------------------------
st.subheader("🏆 Top 10 High-Stress Districts")

st.dataframe(
    stress_df.style.format({
        "avg_spike_score": "{:.2f}",
        "max_spike_score": "{:.2f}",
        "stress_index": "{:.2f}"
    }),
    use_container_width=True
)

# -----------------------------
# Policy Recommendations
# -----------------------------
st.subheader("🧾 Policy Recommendations")

st.markdown("""
Based on the observed demographic churn and migration spikes:

- 📍 **Deploy mobile Aadhaar units** in top stress districts  
- 🏢 **Scale Aadhaar Seva Kendra capacity** in urban migration hubs  
- 📊 **Monitor spike-prone districts monthly** as early-warning zones  
- 🔁 **Run targeted data correction drives** in high youth-update areas  
- 🧠 **Integrate predictive alerts** into UIDAI planning workflows  

This enables a shift from **reactive** to **proactive governance**.
""")

st.markdown("---")
st.caption("UIDAI Hackathon 2026 • Solo Submission • Data-driven Governance")
