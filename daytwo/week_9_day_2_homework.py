# Python Collections and Drilling Telemetry

# Eight drilling observations

observations = [
    {"well_id": "WELL-07", "pressure_psi": 3150, "temperature_f": 186, "sensor_active": True, "field": "north"},
    {"well_id": "WELL-08", "pressure_psi": 2780, "temperature_f": 172, "sensor_active": True, "field": "south"},
    {"well_id": "WELL-09", "pressure_psi": 3325, "temperature_f": 195, "sensor_active": False, "field": "north"},
    {"well_id": "WELL-10", "pressure_psi": 2890, "temperature_f": 180, "sensor_active": True, "field": "east"},
    {"well_id": "WELL-11", "pressure_psi": 3040, "temperature_f": 188, "sensor_active": True, "field": "south"},
    {"well_id": "WELL-07", "pressure_psi": 3180, "temperature_f": 187, "sensor_active": True, "field": "north"},
    {"well_id": "WELL-12", "pressure_psi": 2510, "temperature_f": 166, "sensor_active": False, "field": "east"},
    {"well_id": "WELL-08", "pressure_psi": 2815, "temperature_f": 174, "sensor_active": True, "field": "south"}
]


# TASK 1: Print the first two and last observations

print("\nTASK 1: SELECTED OBSERVATIONS")

print("First two observations:")
print(observations[:2])

print("\nLast observation:")
print(observations[-1])


# TASK 2: Display sorted distinct well IDs and fields

print("\nTASK 2: UNIQUE WELL IDs AND FIELDS")

well_ids = sorted({item["well_id"] for item in observations})

fields = sorted({item["field"] for item in observations})

print("Distinct well IDs:", well_ids)
print("Distinct fields:", fields)


# TASK 3: Calculate total and average pressure

print("\nTASK 3: PRESSURE SUMMARY")

pressure_readings = [
    item["pressure_psi"] for item in observations
]

total_pressure = sum(pressure_readings)

average_pressure = total_pressure / len(pressure_readings)

print("Total pressure:", total_pressure, "psi")
print("Average pressure:", average_pressure, "psi")


# TASK 4: Count observations per well

print("\nTASK 4: OBSERVATIONS PER WELL")

observations_per_well = {}

for item in observations:
    well = item["well_id"]

    observations_per_well[well] = observations_per_well.get(well, 0) + 1

print(observations_per_well)


# TASK 5: Final drilling telemetry report

print("\nTask 5: DRILLING TELEMETRY REPORT =====")

print("Total observations:", len(observations))
print("Number of unique wells:", len(well_ids))
print("Total pressure:", total_pressure, "psi")
print("Average pressure:", average_pressure, "psi")
print("Observations per well:", observations_per_well)