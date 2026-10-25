import json
import pandas as pd
from shapely.geometry import shape, Point

# Load Manningham playgrounds
playgrounds = pd.read_csv("data/playgrounds_combined_manningham.csv")
playgrounds = playgrounds[playgrounds["council"] == "Manningham"].copy()

# Load Manningham open spaces
with open("data/manningham_open_space.geojson", encoding="utf-8") as f:
    open_spaces = json.load(f)

# Categories relevant to recreational open space
included_categories = {
    "Parks and gardens",
    "Natural and semi-natural open space",
    "Sportsfields and organised recreation",
    "Conservation reserves",
    "Recreation corridor"
}

# Keep accessible recreational open spaces
open_space_features = [
    feature
    for feature in open_spaces["features"]
    if feature["properties"].get("OS_CATEGOR") in included_categories
    and feature["properties"].get("OS_ACCESS") == "Open"
]

print(f"Manningham playgrounds: {len(playgrounds)}")
print(f"Eligible open-space polygons: {len(open_space_features)}")

# Convert eligible open-space polygons into Shapely geometries
open_space_geometries = [
    shape(feature["geometry"])
    for feature in open_space_features
]

# Determine whether each playground lies within an open space
def check_open_space(row):
    point = Point(row["longitude"], row["latitude"])

    return any(
        polygon.covers(point)
        for polygon in open_space_geometries
    )

playgrounds["within_open_space"] = playgrounds.apply(
    check_open_space,
    axis=1
)

# Display results
print("\nPlayground locations:")
print(playgrounds["within_open_space"].value_counts())

percentage = 100 * playgrounds["within_open_space"].mean()
print(f"\nPercentage within open space: {percentage:.1f}%")

playgrounds["open_space_status"] = playgrounds["within_open_space"].map({
    True: "Within mapped open space",
    False: "Outside mapped open space"
})

playgrounds.to_csv(
    "data/manningham_playground_open_space.csv",
    index=False
)

print("Exported Manningham playground open-space data.")