# src/visualizer.py

import matplotlib.pyplot as plt

# ---------------- LINE PLOT ----------------
def plot_speed(df):
    plt.figure()
    plt.plot(df["time"], df["speed"])
    plt.title("Speed over Time")
    plt.xlabel("Time")
    plt.ylabel("Speed")
    plt.show()


# ---------------- SCATTER ----------------
def plot_throttle_vs_speed(df):
    plt.figure()
    plt.scatter(df["throttle"], df["speed"])
    plt.title("Throttle vs Speed")
    plt.xlabel("Throttle")
    plt.ylabel("Speed")
    plt.show()


# ---------------- BAR CHART ----------------
def plot_driving_pattern(df):
    plt.figure()
    df["driving_pattern"].value_counts().plot(kind="bar")
    plt.title("Driving Pattern Distribution")
    plt.xlabel("Driving Type")
    plt.ylabel("Count")
    plt.show()


# ---------------- ENGINE TEMP ----------------
def plot_engine_temp(df):
    plt.figure()
    plt.plot(df["time"], df["engine_temp"])
    plt.title("Engine Temperature Over Time")
    plt.xlabel("Time")
    plt.ylabel("Temperature (°C)")
    plt.show()