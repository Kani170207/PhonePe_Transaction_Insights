import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px

# ---------------- PAGE CONFIG (MUST BE FIRST) ----------------
st.set_page_config(
    page_title="PhonePe Transaction Insights",
    layout="wide"
)

# ---------------- TITLE ----------------
st.title("📊 PhonePe Transaction Insights")
st.write("DEBUG: App reached this point")


# ---------------- DATABASE CONNECTION ----------------
@st.cache_data
def load_data():
    conn = sqlite3.connect("data/phonepe_transaction_insights.db")
    df = pd.read_sql("SELECT * FROM aggregated_transaction", conn)
    conn.close()
    return df

df = load_data()

# ---------------- SIDEBAR FILTERS ----------------
st.sidebar.header("🔍 Filters")

year = st.sidebar.selectbox(
    "Select Year",
    sorted(df["Year"].unique())
)

filtered_df = df[df["Year"] == year]

# ---------------- KPI SECTION ----------------
col1, col2 = st.columns(2)

col1.metric(
    "💰 Total Transaction Amount",
    f"₹ {filtered_df['Transaction_Amount'].sum():,.0f}"
)

col2.metric(
    "🔢 Total Transactions",
    f"{filtered_df['Transaction_Count'].sum():,}"
)

# ---------------- DATA PREVIEW ----------------
st.subheader("📄 Data Preview")
st.dataframe(filtered_df.head())

# ---------------- BAR CHART ----------------
st.subheader("📍 State-wise Transactions")

fig = px.bar(
    filtered_df,
    x="State",
    y="Transaction_Amount",
    title="State-wise Transaction Amount",
    labels={"Transaction_Amount": "Transaction Amount (₹)"},
)

st.plotly_chart(fig, use_container_width=True)

