import pandas as pd


def standardize_borough(data, borough_column="Borough"):
    """
    Standardize the borough column to be case-insensitive and strip whitespace.
    """
    data[borough_column] = data[borough_column].str.strip()
    data[borough_column] = data[borough_column].str.upper()
    return data


def map_borough_codes(data, borough_column="Borough", code_column="BoroughCode"):
    """
    Map borough names to numeric codes.
    """
    borough_codes = {
        "MANHATTAN": 1,
        "BRONX": 2,
        "BROOKLYN": 3,
        "QUEENS": 4,
        "STATEN ISLAND": 5,
    }
    data[code_column] = data[borough_column].map(borough_codes)
    print(
        f"BoroughCode column : type = {data['BoroughCode'].dtype}\n"
        f"{data["BoroughCode"].head(10)}"
    )
    return data


def create_boroct(
    data,
    tract_column="CensusTract_Fetched",
    boro_code_column="BoroughCode",
    boroct_column="BoroCT",
):
    """
    Combine Borough Code and Census Tract into a BoroCT column.
    """
    # Ensure CensusTract_Fetched is a string and handle missing data
    data[tract_column] = data[tract_column].fillna("").astype(str)
    # Create the BoroCT column
    data[boroct_column] = data.apply(
        lambda row: (
            f"{row[boro_code_column]}{row[tract_column]}"
            if row[boro_code_column] and row[tract_column]
            else None
        ),
        axis=1,
    )
    return data


def process_boroct(
    data,
    borough_column="Borough",
    tract_column="CensusTract_Fetched",
    boroct_column="BoroCT",
):
    """
    Full pipeline to process BoroCT:
    1. Standardize Borough names.
    2. Map Borough Codes.
    3. Create BoroCT column.
    """
    data = standardize_borough(data, borough_column)
    data = map_borough_codes(data, borough_column)
    data = create_boroct(data, tract_column=tract_column, boroct_column=boroct_column)
    return data


def save_data(data, output_path):
    """
    Save the processed data to a CSV file.
    """
    data.to_csv(output_path, index=False)
    print(f"Processed data saved to {output_path}")
