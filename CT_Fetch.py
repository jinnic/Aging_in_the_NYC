import pandas as pd
import requests

# Load the CSV file
file_path = "data/nyc_aging_contracts_cleaned.csv"

# # Test with 10 rows
# data = pd.read_csv(file_path, nrows=10)
data = pd.read_csv(file_path)

# Combine address columns to form full address
data["FullAddress"] = (
    data["ProgramAddress"]
    + ", "
    + data["ProgramCity"]
    + ", "
    + data["ProgramState"]
    + " "
    + data["Postcode"].astype(str)
)


# Function to fetch Census Tract using Census Geocoder API
def get_census_tract(address):
    base_url = "https://geocoding.geo.census.gov/geocoder/geographies/address"
    params = {
        "street": address.split(",")[0],  # Extract street address
        "city": address.split(",")[1].strip(),  # Extract city
        "state": "NY",  # Fixed state in my case
        "benchmark": "Public_AR_Current",
        "vintage": "Current_Current",
        "format": "json",
    }
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()
        tract_info = data.get("result", {}).get("addressMatches", [])
        if tract_info:
            return tract_info[0]["geographies"]["Census Tracts"][0]["TRACT"]
        else:
            return None
    except Exception as e:
        print(f"Error fetching Census Tract for address {address}: {e}")
        return None


# Apply the function to each address
data["CensusTract_Fetched"] = data["FullAddress"].apply(
    lambda address: str(get_census_tract(address))
)

# Save the updated data to a new CSV
output_path = "data/updated_aging_contracts.csv"
data.to_csv(output_path, index=False)

print(f"Updated data with Fetched Census Tract codes saved to {output_path}")
