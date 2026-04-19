import pandas as pd
import numpy as np

np.random.seed(42)

n = 10000  # number of records

# Generate base signals
time = pd.date_range(start="2024-01-01", periods=n, freq="s")

speed = np.random.normal(60, 15, n).clip(0)          # km/h
throttle = np.random.uniform(0, 100, n)              # %
rpm = np.random.normal(3000, 700, n).clip(500)       # engine RPM

# Additional automotive signals (IMPORTANT for JD)
brake = np.random.choice([0, 1], size=n, p=[0.8, 0.2])
gear = np.random.randint(1, 6, size=n)
engine_temp = np.random.normal(90, 5, n)             # °C
fuel_rate = np.random.uniform(5, 15, n)              # L/hr

# Cruise control signal
GRA_FOC_ACTIVE = np.random.choice([0, 1], size=n, p=[0.7, 0.3])

# Create DataFrame
data = pd.DataFrame({
    "time": time,
    "speed": speed,
    "throttle": throttle,
    "rpm": rpm,
    "brake": brake,
    "gear": gear,
    "engine_temp": engine_temp,
    "fuel_rate": fuel_rate,
    "GRA_FOC_ACTIVE": GRA_FOC_ACTIVE
})
data["brake"] = np.random.choice([0, 1], size=n, p=[0.8, 0.2])
# Save to CSV
data.to_csv("data/vehicle_data.csv", index=False)

print("✅ Automotive dataset generated successfully!")