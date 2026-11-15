"""Write your own unittest cases; do not import the instructor solution."""
import unittest
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from telemetry_capstone import convert_pressure, convert_temperature


class TelemetryCapstoneTests(unittest.TestCase):
    def test_pressure_known_value(self):
        self.assertAlmostEqual(
            convert_pressure(100, "psi"),
            689.47572932,
        )

    def test_temperature_known_value(self):
        self.assertAlmostEqual(
            convert_temperature(212, "F"),
            100,
        )


if __name__ == "__main__":
    unittest.main()
