import requests
import pandas as pd


def get_census_tract(
    address, city, state="NY", benchmark="Public_AR_Current", vintage="Current_Current"
):
    """
    Fetch Census Tract information for a given address using the Census Bureau Geocoder API.

    Args:
        address (str): Street address (e.g., "1600 Pennsylvania Ave NW").
        city (str): City (e.g., "Washington").
        state (str): State abbreviation (e.g., "NY"). Default is "NY".
        benchmark (str): Geocoder benchmark version. Default is "Public_AR_Current".
        vintage (str): Geocoder vintage version. Default is "Current_Current".

    Returns:
        str: Census Tract code if found, or None if not found.
    """
    base_url = "https://geocoding.geo.census.gov/geocoder/geographies/address"
    params = {
        "street": address,
        "city": city,
        "state": state,
        "benchmark": benchmark,
        "vintage": vintage,
        "format": "json",
    }
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()
        address_matches = data.get("result", {}).get("addressMatches", [])
        if address_matches:
            return address_matches[0]["geographies"]["Census Tracts"][0]["TRACT"]
        return None
    except Exception as e:
        print(f"Error fetching Census Tract for {address}, {city}, {state}: {e}")
        return None


def fetch_census_tracts(
    data,
    address_column,
    city_column,
    state_column="ProgramState",
    new_column="CensusTract_Fetched",
):
    """
    Apply Census Tract fetching for each row in a DataFrame.

    Args:
        data (pd.DataFrame): The input DataFrame with address data.
        address_column (str): Column name containing street addresses.
        city_column (str): Column name containing city names.
        state_column (str): Column name containing state abbreviations. Default is "ProgramState".
        new_column (str): Name of the new column to store fetched Census Tracts.

    Returns:
        pd.DataFrame: DataFrame with the new column added.
    """
    # Standardize the state column to uppercase (if it exists)
    if state_column in data.columns:
        data[state_column] = data[state_column].str.upper()

    # Fetch Census Tracts for each row
    data[new_column] = data.apply(
        lambda row: get_census_tract(
            address=row[address_column],
            city=row[city_column],
            state=row[state_column] if state_column in row else "NY",
        ),
        axis=1,
    )
    return data
