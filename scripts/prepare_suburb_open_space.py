import pandas as pd

# Load the results from Chart 9
df = pd.read_csv("data/manningham_playground_open_space.csv")

# Count playgrounds by suburb and open-space status
summary = (
    df.groupby(["suburb", "open_space_status"])
    .size()
    .unstack(fill_value=0)
)

# Calculate totals and percentages
summary["total"] = summary.sum(axis=1)

summary["within_pct"] = (
    100 * summary.get("Within mapped open space", 0)
    / summary["total"]
)

summary["outside_pct"] = (
    100 * summary.get("Outside mapped open space", 0)
    / summary["total"]
)

# Sort by percentage outside mapped open space
summary = summary.sort_values("outside_pct", ascending=False)

print(summary.to_string())

# Export for Vega-Lite
summary.reset_index().to_csv(
    "data/manningham_suburb_open_space.csv",
    index=False
)

print("\nSaved suburb summary.")