# Aging in the City: Understanding NYC’s Older Population and Their Access to Services

This project explores the demographic distribution and service accessibility for NYC's older population using Census data and senior services datasets. By combining geospatial and demographic analysis, the project aims to identify gaps in service coverage and provide actionable insights for stakeholders.

---

## Project Overview

### Research Questions

1. **Who is the older population in NYC right now, and how has that changed (increased/decreased, socioeconomic) in recent decades?**
2. **Where are older adults living? Are there pockets of concentrated older adult populations?**
3. **What city services are available to older New Yorkers, and how are they distributed compared to where older adult populations are concentrated?**

This project provides data-driven insights for community boards, local leaders, policymakers, and NYC residents who wish to improve services for the city's aging population.

---

## Data Sources

1. **2020 Census Data**

   - **Source**: [NYC Department of City Planning](https://s-media.nyc.gov/agencies/dcp/assets/files/excel/data-tools/census/census2020/nyc_decennialcensusdata_2010_2020_change-core-geographies.xlsx)
   - Provides census tracts and higher-level geographic data to analyze population trends.

2. **NYC Aging - All Contracted Providers**

   - **Source**: [Open Data NYC](https://data.cityofnewyork.us/Social-Services/Department-for-the-Aging-NYC-Aging-All-Contracted-/cqc8-am9x/about_data) - NYC Department for the Aging
   - Includes details about senior services and their locations for 2024.

3. **CT_Fetch.py Script**
   - Custom Python script to fetch accurate Census Tract codes using the [Census Bureau Geocoder API](https://geocoding.geo.census.gov/geocoder/).
   - Ensures alignment between senior service locations and Census data.

---

## Features

- **Automated Geocoding**

  - Uses `CT_Fetch.py` to fetch Census Tract codes for senior service locations.
  - Resolves mismatches between service addresses and Census tract data.

- **Visualization**
  - **Population Pyramid**: Age and gender distribution of NYC residents aged 60 and older.
  - **Bar Chart with Line Overlay**: Changes in older populations between 2010 and 2020, segmented by 5-year age groups.
  - **Choropleth Map with Overlay**: Highlights concentrations of older adults and overlays service locations.

---
