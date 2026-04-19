import pandas as pd

class VehicleDataAnalyzer:

    def __init__(self, file_path):
        self.df = pd.read_csv(file_path, parse_dates=["time"])

    # ---------------- CLEANING ----------------
    def clean_data(self):
        self.df = self.df.dropna()

    # ---------------- FEATURE ENGINEERING ----------------
    def add_features(self):
        self.df["acceleration"] = self.df["speed"].diff().fillna(0)

    # ---------------- BASIC ANALYSIS ----------------
    def get_summary(self):
        return self.df.describe()

    def throttle_speed_correlation(self):
        return self.df[["throttle", "speed"]].corr()

    # ---------------- ANOMALY DETECTION ----------------
    def detect_high_speed(self, threshold=100):
        return self.df[self.df["speed"] > threshold]

    def detect_hard_acceleration(self, threshold=10):
        return self.df[self.df["acceleration"] > threshold]

    def detect_idle_engine(self):
        return self.df[(self.df["speed"] < 5) & (self.df["rpm"] > 1000)]

    def detect_over_revving(self):
        return self.df[self.df["rpm"] > 5000]

    def detect_overheating(self):
        return self.df[self.df["engine_temp"] > 100]

    def detect_inefficient_driving(self):
        return self.df[(self.df["throttle"] > 70) & (self.df["speed"] < 40)]

    # ---------------- DRIVING BEHAVIOR ----------------
    def classify_driving(self):
        conditions = []

        for _, row in self.df.iterrows():
            if row["acceleration"] > 8:
                conditions.append("Aggressive")
            elif row["brake"] == 1:
                conditions.append("Braking")
            else:
                conditions.append("Normal")

        self.df["driving_pattern"] = conditions
        return self.df["driving_pattern"].value_counts()

    # ---------------- AUTOMOTIVE ANALYSIS ----------------
    def cruise_control_analysis(self):
        return self.df.groupby("GRA_FOC_ACTIVE")["speed"].mean()

    def fuel_efficiency(self):
        return (self.df["speed"] / self.df["fuel_rate"]).mean()