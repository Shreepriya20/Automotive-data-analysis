# src/utils.py

import pandas as pd

# ---------------- DATA HELPERS ----------------
def load_data(file_path):
    return pd.read_csv(file_path, parse_dates=["time"])


def save_data(df, file_path):
    df.to_csv(file_path, index=False)


# ---------------- VALIDATION ----------------
def validate_columns(df, required_columns):
    missing = [col for col in required_columns if col not in df.columns]
    if missing:
        raise ValueError(f"Missing columns: {missing}")


# ---------------- NORMALIZATION ----------------
def normalize_column(df, column):
    df[column] = (df[column] - df[column].min()) / (
        df[column].max() - df[column].min()
    )
    return df


# ---------------- TIME FEATURES ----------------
def extract_time_features(df):
    df["hour"] = df["time"].dt.hour
    df["minute"] = df["time"].dt.minute
    return df