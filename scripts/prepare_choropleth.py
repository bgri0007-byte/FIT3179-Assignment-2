
import json
from collections import Counter

# Load ACT suburb boundaries
with open("data/act_boundaries.json", encoding="utf-8") as f:
    boundaries = json.load(f)

# Load ACT playground polygons
with open("data/ACTGOV_Playground_Assets_20260926.geojson", encoding="utf-8") as f:
    playgrounds = json.load(f)

# Extract boundary suburb names
boundary_suburbs = {
    feature["properties"]["DIVISION_NAME"].strip().upper()
    for feature in boundaries["features"]
    if feature["properties"].get("DIVISION_NAME")
}

# Extract playground suburb names
playground_suburbs = {
    feature["properties"]["suburb"].strip().upper()
    for feature in playgrounds["features"]
    if feature["properties"].get("suburb")
}

# Find unmatched suburbs
unmatched = playground_suburbs - boundary_suburbs

print("Boundary suburbs:", len(boundary_suburbs))
print("Playground suburbs:", len(playground_suburbs))
print("Unmatched suburbs:", sorted(unmatched))

for feature in boundaries["features"][:5]:
    props = feature["properties"]
    print(props["DIVISION_NAME"], props["Shape__Area"])

# Count playgrounds in each suburb
playground_counts = Counter(
    feature["properties"]["suburb"].strip().upper()
    for feature in playgrounds["features"]
    if feature["properties"].get("suburb")
)

# Display the five suburbs with the most playgrounds
print("\nTop 5 suburbs by playground count:")
for suburb, count in playground_counts.most_common(5):
    print(f"{suburb}: {count}")


# Calculate playground density for each suburb
for feature in boundaries["features"]:
    props = feature["properties"]

    suburb = props["DIVISION_NAME"].strip().upper()
    area_km2 = props["Shape__Area"] / 1_000_000

    count = playground_counts.get(suburb, 0)
    density = count / area_km2 if area_km2 > 0 else 0

    props["playground_count"] = count
    props["area_km2"] = area_km2
    props["playground_density"] = density

# Display the five highest-density suburbs
ranked = sorted(
    boundaries["features"],
    key=lambda f: f["properties"]["playground_density"],
    reverse=True
)

print("\nTop 5 suburbs by playground density:")
for feature in ranked[:5]:
    props = feature["properties"]
    print(
        f'{props["DIVISION_NAME"]}: '
        f'{props["playground_density"]:.2f} playgrounds/km² '
        f'({props["playground_count"]} playgrounds)'
    )


# Export ACT suburbs with playground density
output_path = "data/act_playground_density.geojson"

with open(output_path, "w", encoding="utf-8") as f:
    json.dump(boundaries, f)

print(f"\nSaved choropleth data to {output_path}")


# Inspect available ACT districts
with open("data/act_districts.json", encoding="utf-8") as f:
    districts = json.load(f)

# List available ACT district names
with open("data/act_districts.json", encoding="utf-8") as f:
    districts = json.load(f)

district_names = sorted({
    feature["properties"]["DISTRICT_NAME"]
    for feature in districts["features"]
})

print("\nAvailable ACT districts:")
for name in district_names:
    print(name)

print("\nDistricts potentially covering eastern Canberra:")
for name in district_names:
    if any(term in name for term in ["CANBERRA", "MAJURA", "JERRABOMBERRA"]):
        print(name)


