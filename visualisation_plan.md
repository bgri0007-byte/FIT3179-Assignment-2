| Dataset | Location | Classification | Facilities | Shade | Surface area |
|---|---|---|---|---|---|
| Manningham | Yes | Yes | To verify | No | No |
| Melbourne | Yes | No consistent size classification | Limited (to verify) | No | No |
| ACT | Yes | Yes | No | Yes | Yes |
| Greater Shepparton | Yes | Mixed facility types | No | No | No |
| Adelaide | Yes | No | No | No | No |
| Hobart | Yes | Park type | Yes (multiple amenities) | Yes (shade trees) | No |
| Greater Dandenong | Yes | No | No | No | Yes (area; units to verify) |

Research question: How do the characteristics and facilities of public playgrounds vary across selected Australian communities?

Design principle: Compare regions only where attributes have consistent definitions; otherwise use individual regional case studies.

## Proposed Visualisation Plan

**Project title:** Beyond the Playground: Exploring Australia's Public Play Spaces

**Research question:** How do the characteristics and facilities of public playgrounds vary across selected Australian communities?

**Target:** 12 visualisations, including at least 3 different map idioms.

### Chapter 1 — Australia's Play Spaces

*Introduce the geographic scope of our data and where public playgrounds are located.*

| # | Visualisation | Dataset | Idiom | Question answered |
|---|---|---|---|---|
| 1 | Australian playground coverage | All regions | Geographic coverage map | Which Australian communities are represented in our datasets? |
| 2 | Playground distribution | Manningham | Categorical point map | Where are different playground types located? |
| 3 | Playground concentration | Manningham | Density/hexbin map | Where are playgrounds geographically concentrated? |

### Chapter 2 — Not All Playgrounds Are Equal

*Explore how playground classifications and physical characteristics differ.*

| # | Visualisation | Dataset | Idiom | Question answered |
|---|---|---|---|---|
| 4 | Playground classification breakdown | Manningham | Bar chart | Which playground classifications are most common? |
| 5 | Playground classification composition | Manningham | Treemap | What proportion of playgrounds belongs to each classification? |
| 6 | Playground surface area | ACT | Proportional-symbol map | Where are larger and smaller playgrounds located? |
| 7 | Playground area distribution | ACT | Histogram | How does playground surface area vary? |

### Chapter 3 — What Makes a Great Playground?

*Investigate shade and the facilities available at public play spaces.*

| # | Visualisation | Dataset | Idiom | Question answered |
|---|---|---|---|---|
| 8 | Playground shade levels | ACT | Bar chart | How common are different recorded shade levels? |
| 9 | Shade by playground size | ACT | Heatmap | Are larger playgrounds more likely to have higher recorded shade levels? |
| 10 | Playground facilities | Hobart | Ranked bar chart | Which amenities are most commonly recorded at parks with play equipment? |
| 11 | Facility combinations | Hobart | Heatmap | Which amenities tend to occur together? |
| 12 | Facility availability profile | Hobart | Dot plot | How does the availability of individual amenities compare? |

### Map Idioms

1. Geographic coverage map
2. Categorical point map
3. Density/hexbin map
4. Proportional-symbol map

These provide four proposed geographic approaches. We will verify that at least three qualify as distinct map idioms under the assignment requirements.

### Implementation Priorities

- [ ] Validate playground records, fields and units used by each chart.
- [ ] Confirm the final map idioms.
- [ ] Retain and refine the existing Australia overview map.
- [ ] Develop the Manningham classification and density maps.
- [ ] Develop the ACT proportional-symbol map.
- [ ] Build the Manningham classification charts.
- [ ] Build the ACT area and shade charts.
- [ ] Build the Hobart facilities charts.
- [ ] Integrate all visualisations into the website.
- [ ] Add annotations, storytelling text and interactive features.
- [ ] Test the website and publish through GitHub Pages.

**Design principle:** Compare regions only where attributes have consistent definitions. Otherwise, present separate regional case studies.

**Important:** This is a provisional plan. Chart feasibility, data quality and idiom diversity must be checked before implementation.

Overview map coordinate methodology: Study-region markers use approximate geographic reference coordinates obtained from GeoNames (https://www.geonames.org/). Markers identify the general location of each study region and do not represent individual playgrounds or exact council centroids.