
import json
from pyproj import Transformer


from shapely.geometry import shape, mapping
from shapely.ops import transform



# Load Victorian open-space polygons
with open("data/VPA_Draft_Open_Space_Data.geojson", encoding="utf-8") as f:
    open_spaces = json.load(f)

# Keep only Manningham features
manningham_features = [
    feature
    for feature in open_spaces["features"]
    if "MANNINGHAM" in str(
        feature["properties"].get("LGA", "")
    ).upper()
]

# Create a smaller GeoJSON
manningham = {
    "type": "FeatureCollection",
    "features": manningham_features
}

# Convert Web Mercator coordinates to WGS84 longitude/latitude
transformer = Transformer.from_crs(
    "EPSG:3857",
    "EPSG:4326",
    always_xy=True
)

for feature in manningham_features:
    geometry = shape(feature["geometry"])

    converted_geometry = transform(
        transformer.transform,
        geometry
    )

    feature["geometry"] = mapping(converted_geometry)


# Save the filtered data
with open("data/manningham_open_space.geojson", "w", encoding="utf-8") as f:
    json.dump(manningham, f)

print(f"Saved {len(manningham_features)} Manningham open-space features.")


from collections import Counter

# Count open-space categories and access types
categories = Counter(
    feature["properties"].get("OS_CATEGOR")
    for feature in manningham_features
)

access_types = Counter(
    feature["properties"].get("OS_ACCESS")
    for feature in manningham_features
)

print("\nOpen-space categories:")
for category, count in categories.most_common():
    print(f"{category}: {count}")

print("\nAccess types:")
for access, count in access_types.most_common():
    print(f"{access}: {count}")
