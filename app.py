import streamlit as st
import pandas as pd
from src.analyzer import VehicleDataAnalyzer

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Automotive Data Dashboard", layout="wide")

st.title("🚗 Automotive Data Analysis Dashboard")

# ---------------- LOAD DATA ----------------
analyzer = VehicleDataAnalyzer("data/vehicle_data.csv")
analyzer.clean_data()
analyzer.add_features()
analyzer.classify_driving()

df = analyzer.df

# ---------------- SIDEBAR FILTERS ----------------
st.sidebar.header("Filters")

speed_threshold = st.sidebar.slider("Speed Threshold", 0, 150, 100)
temp_threshold = st.sidebar.slider("Engine Temp Threshold", 80, 120, 100)

# ---------------- SUMMARY ----------------
st.subheader("📊 Data Summary")
st.write(analyzer.get_summary())

# ---------------- FILTERED DATA ----------------
st.subheader("🚨 High Speed Events")
high_speed_df = analyzer.detect_high_speed(speed_threshold)
st.write(high_speed_df.head())

# ---------------- CHARTS ----------------

# Speed over time
st.subheader("📈 Speed Over Time")
st.line_chart(df.set_index("time")["speed"])

# Throttle vs Speed
st.subheader("📉 Throttle vs Speed")
st.scatter_chart(df[["throttle", "speed"]])

# Driving pattern distribution
st.subheader("🚦 Driving Pattern Distribution")
st.bar_chart(df["driving_pattern"].value_counts())

# Engine temperature
st.subheader("🌡 Engine Temperature")
st.line_chart(df.set_index("time")["engine_temp"])

# ---------------- ANALYTICS ----------------

st.subheader("⚙️ Cruise Control Analysis")
st.write(analyzer.cruise_control_analysis())

st.subheader("⛽ Fuel Efficiency")
st.write(analyzer.fuel_efficiency())

st.subheader("🔥 Overheating Detection")
overheat_df = df[df["engine_temp"] > temp_threshold]
st.write(overheat_df.head())

st.subheader("🚫 Inefficient Driving")
st.write(analyzer.detect_inefficient_driving().head())