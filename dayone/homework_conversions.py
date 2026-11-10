# WEEK 9 - CLASS 1 HOMEWORK
# Engineering Unit Conversion

# Question 9: Store the well information
well_id = "WELL-001"
pressure_psi = 2500.0
temperature_f = 140.0
sensor_active = True

# Convert pressure from PSI to kPa
pressure_kpa = pressure_psi * 6.894757

# Convert temperature from Fahrenheit to Celsius
temperature_c = (temperature_f - 32) * 5/9

# Display the results
print("QUESTION 9: ENGINEERING CONVERSION")
print("Well ID:", well_id)
print(f"Pressure: {pressure_kpa:.1f} kPa")
print(f"Temperature: {temperature_c:.1f} °C")
print("Sensor Status:", sensor_active)

# Question 10: New measurements

pressure_psi = 3000.0
temperature_f = 32.0

# Perform conversions
pressure_kpa = pressure_psi * 6.894757
temperature_c = (temperature_f - 32) * 5/9

# Display results
print("\nQUESTION 10: SECOND CONVERSION")
print(f"Pressure: {pressure_kpa:.1f} kPa")
print(f"Temperature: {temperature_c:.1f} °C")

# Question 11: Demonstrate type mismatch

raw_pressure = "3150"

# This line will cause a TypeError:
# pressure_kpa = raw_pressure * 6.894757

# Convert string to float
numeric_pressure = float(raw_pressure)

# Calculate converted pressure
pressure_kpa = numeric_pressure * 6.894757

# Display results
print("\nQUESTION 11: TYPE CONVERSION")
print("Raw Pressure:", raw_pressure)
print("Numeric Pressure:", numeric_pressure)
print(f"Converted Pressure: {pressure_kpa:.1f} kPa")