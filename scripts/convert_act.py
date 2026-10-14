
import json
from pathlib import Path

# Locate the project data folder
data_folder = Path(__file__).resolve().parent.parent / "data"

# Load ACT playground GeoJSON
with open(data_folder / "ACTGOV_Playground_Assets_20260926.geojson", encoding="utf-8") as f:
    act_data = json.load(f)

# Inspect the dataset
features = act_data["features"]

# Extract playground information
playgrounds = []

for feature in features:
    properties = feature["properties"]
    geometry = feature["geometry"]

    # Skip playgrounds without geometry or not active
    if geometry is None or properties.get("operational_state") != "ACTIVE":
        continue

    # Extract coordinates from all polygon rings
    coordinates = []

    for polygon in geometry["coordinates"]:
        for ring in polygon:
            coordinates.extend(ring)

    if not coordinates:
        continue

    longitude = sum(point[0] for point in coordinates) / len(coordinates)
    latitude = sum(point[1] for point in coordinates) / len(coordinates)

    playgrounds.append({
        "council": "ACT",
        "name": properties.get("asset_name", ""),
        "longitude": longitude,
        "latitude": latitude,
        "suburb": properties.get("suburb", ""),
        "classification": properties.get("asset_sub_type", ""),
        "surface_area": properties.get("surface_area", "")
    })


import csv

# Existing combined dataset
input_file = data_folder / "playgrounds_combined_manningham.csv"

# New combined dataset
output_file = data_folder / "playgrounds_combined_act.csv"

# Read existing playgrounds
with open(input_file, "r", encoding="utf-8-sig", newline="") as f:
    reader = csv.DictReader(f)
    existing_playgrounds = list(reader)
    for playground in existing_playgrounds:
        playground["surface_area"] = ""
    columns = reader.fieldnames + ["surface_area"]

# Combine existing playgrounds with ACT playgrounds
combined_playgrounds = existing_playgrounds + playgrounds

# Write the new CSV
with open(output_file, "w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=columns)
    writer.writeheader()
    writer.writerows(combined_playgrounds)

print("Total combined playgrounds:", len(combined_playgrounds))
print("Saved to:", output_file)

