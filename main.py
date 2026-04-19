from src.analyzer import VehicleDataAnalyzer
from src.visualizer import (
    plot_speed,
    plot_throttle_vs_speed,
    plot_driving_pattern,
    plot_engine_temp
)

# Initialize
analyzer = VehicleDataAnalyzer("data/vehicle_data.csv")

# Run pipeline
analyzer.clean_data()
analyzer.add_features()

print("========== SUMMARY ==========")
print(analyzer.get_summary())

print("\n========== HIGH SPEED EVENTS ==========")
print(analyzer.detect_high_speed().head())

print("\n========== HARD ACCELERATION ==========")
print(analyzer.detect_hard_acceleration().head())

print("\n========== IDLE ENGINE ==========")
print(analyzer.detect_idle_engine().head())

print("\n========== OVER-REVVING ==========")
print(analyzer.detect_over_revving().head())

print("\n========== OVERHEATING ==========")
print(analyzer.detect_overheating().head())

print("\n========== INEFFICIENT DRIVING ==========")
print(analyzer.detect_inefficient_driving().head())

print("\n========== THROTTLE vs SPEED CORRELATION ==========")
print(analyzer.throttle_speed_correlation())

print("\n========== DRIVING PATTERN ==========")
print(analyzer.classify_driving())

print("\n========== CRUISE CONTROL ANALYSIS ==========")
print(analyzer.cruise_control_analysis())

print("\n========== FUEL EFFICIENCY ==========")
print(analyzer.fuel_efficiency())

# ---------------- VISUALIZATION ----------------
df = analyzer.df

plot_speed(df)
plot_throttle_vs_speed(df)
plot_driving_pattern(df)
plot_engine_temp(df)