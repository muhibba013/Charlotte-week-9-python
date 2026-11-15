"""Week 9 Class 5: complete the TODOs; do not import instructor solutions."""
import csv
from pathlib import Path

PSI_TO_KPA = 6.8947572932


def convert_pressure(value, unit):
    """Return pressure in kPa; reject unsupported units."""
    try:
        pressure = float(value)
    except (TypeError, ValueError) as exc:
        raise ValueError("pressure must be numeric") from exc

    unit = unit.strip().lower()
    if unit == "psi":
        return pressure * PSI_TO_KPA
    if unit == "kpa":
        return pressure
    raise ValueError(f"unsupported pressure unit: {unit}")


def convert_temperature(value, unit):
    """Return temperature in degrees Celsius."""
    try:
        temperature = float(value)
    except (TypeError, ValueError) as exc:
        raise ValueError("temperature must be numeric") from exc

    unit = unit.strip().lower()
    if unit in ("c", "°c", "celsius"):
        return temperature
    if unit in ("f", "°f", "fahrenheit"):
        return (temperature - 32) * 5 / 9
    raise ValueError(f"unsupported temperature unit: {unit}")


def parse_record(raw_line):
    """Return normalized dictionary; raise ValueError for malformed records."""
    try:
        fields = next(csv.reader([raw_line], skipinitialspace=True))
    except (csv.Error, StopIteration) as exc:
        raise ValueError("malformed CSV row") from exc

    if len(fields) != 7:
        raise ValueError(f"expected 7 fields, got {len(fields)}")

    (
        well_id,
        timestamp,
        pressure,
        pressure_unit,
        temperature,
        temperature_unit,
        status,
    ) = (field.strip() for field in fields)

    if not well_id or not timestamp:
        raise ValueError("well ID and timestamp are required")
    if not status:
        raise ValueError("status is required")

    pressure_kpa = convert_pressure(pressure, pressure_unit)
    temperature_c = convert_temperature(temperature, temperature_unit)

    return {
        "well_id": well_id,
        "timestamp": timestamp,
        "pressure_kpa": round(pressure_kpa, 2),
        "temperature_c": round(temperature_c, 2),
        "status": status.upper(),
    }


def process_lines(lines):
    """Return (accepted_records, rejected_records) preserving source line numbers."""
    accepted = []
    rejected = []

    for line_number, raw_line in enumerate(lines, start=1):
        if not raw_line.strip():
            continue

        try:
            record = parse_record(raw_line)
            record["source_line"] = line_number
            accepted.append(record)
        except ValueError as exc:
            rejected.append({
                "source_line": line_number,
                "raw_record": raw_line.rstrip("\r\n"),
                "reason": str(exc),
            })

    return accepted, rejected


def summarize_by_well(records):
    """Average pressure for ACTIVE records, sorted by well ID."""
    grouped = {}

    for record in records:
        if record.get("status", "").upper() == "ACTIVE":
            grouped.setdefault(record["well_id"], []).append(
                float(record["pressure_kpa"])
            )

    return [
        {
            "well_id": well_id,
            "average_pressure_kpa": round(sum(values) / len(values), 2),
        }
        for well_id, values in sorted(grouped.items())
    ]


def write_csv(path, fieldnames, records):
    """Create output CSV with a header row."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)

    with path.open("w", newline="", encoding="utf-8") as output:
        writer = csv.DictWriter(
            output,
            fieldnames=fieldnames,
            extrasaction="ignore",
        )
        writer.writeheader()
        writer.writerows(records)


def run(input_path, output_dir):
    """Generate cleaned_telemetry.csv, rejected_records.csv, well_summary.csv."""
    with Path(input_path).open(
        "r", newline="", encoding="utf-8-sig"
    ) as source:
        accepted, rejected = process_lines(source)

    output_dir = Path(output_dir)

    write_csv(
        output_dir / "cleaned_telemetry.csv",
        [
            "well_id",
            "timestamp",
            "pressure_kpa",
            "temperature_c",
            "status",
            "source_line",
        ],
        accepted,
    )

    write_csv(
        output_dir / "rejected_records.csv",
        ["source_line", "raw_record", "reason"],
        rejected,
    )

    write_csv(
        output_dir / "well_summary.csv",
        ["well_id", "average_pressure_kpa"],
        summarize_by_well(accepted),
    )

    return accepted, rejected


if __name__ == "__main__":
    input_file = input("Enter input file path: ")
    output_dir = input("Enter output directory path: ")
    run(input_file, output_dir)