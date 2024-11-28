import pandas as pd
from census_tract_fetcher import fetch_census_tracts
from boro_census_tract_processor import process_boroct

# Specify the path to your Excel file
file_path = "data/nyc_aging_contracts.csv"

# Read the Excel file
data = pd.read_csv(file_path)


def clean_data(data):
    """
    Perform data cleaning:
    1. Remove leading single quotes from 'DFTA ID' column.
    2. Handle missing values in the 'Census Tract' column.
    3. Format 'Census Tract' column to the desired string format.
    """
    # Remove leading single quotes from 'DFTA ID' column
    data["DFTA ID"] = data["DFTA ID"].str.lstrip("'")
    print("Cleaned 'DFTA ID':")
    print(data["DFTA ID"].head())

    # Check for missing values in the 'Census Tract' column
    missing_values_count = data["Census Tract"].isnull().sum()
    print(f"Number of missing values in 'Census Tract' column: {missing_values_count}")
    if missing_values_count > 0:
        missing_rows = data[data["Census Tract"].isnull()]
        print("Rows with missing values in 'Census Tract':")
        print(missing_rows)

    # try:
    #     # Check for missing values in the 'DFTA ID' column
    #     missing_rows = data[data["Census Tract"].isnull()]

    #     # Print out rows with missing values
    #     if not missing_rows.empty:
    #         print("Rows with missing values in 'Census Tract':")
    #         print(missing_rows)
    #     else:
    #         print("No missing values in 'Census Tract' column.")
    # except FileNotFoundError:
    #     print("File not found. Please upload the file and try again.")

    # # Handle missing values (fill with 0 or another placeholder)
    # data["Census Tract"] = data["Census Tract"].fillna("N/A")

    # Drop rows where 'Census Tract' is null
    initial_row_count = len(data)
    data = data.dropna(subset=["Census Tract"])
    final_row_count = len(data)
    print(
        f"Dropped {initial_row_count - final_row_count} rows with null 'Census Tract' values."
    )

    # # Format 'Census Tract' column as integer, then as string with formatting
    # data["CensusTractFormatted"] = data["Census Tract"].apply(
    #     lambda x: f"{int(x):04d}.00" if x < 1000 else f"{int(x)}.00"
    # )
    # print("Formatted 'Census Tract':")
    # print(data["CensusTractFormatted"].head())

    return data


def main():
    # Specify the path to your input file
    file_path = "data/nyc_aging_contracts.csv"
    output_path = "data/nyc_aging_contracts_processed.csv"

    # Load the data
    data = pd.read_csv(file_path)
    print("Original data loaded successfully.")

    # Clean the data
    data = clean_data(data)

    # Fetch Census Tract codes based on address data
    data = fetch_census_tracts(
        data=data,
        address_column="ProgramAddress",
        city_column="ProgramCity",
        state_column="ProgramState",
        new_column="CensusTract_Fetched",
    )

    # Process Borough Codes and create BoroCT column
    data = process_boroct(
        data,
        borough_column="Borough",
        tract_column="CensusTract_Fetched",
        boroct_column="BoroCT",
    )

    # Save the processed data
    save_data(data, output_path)


def save_data(data, output_path):
    """
    Save the updated DataFrame to a CSV file.

    Args:
        data (pd.DataFrame): The processed DataFrame.
        output_path (str): Path to save the CSV file.
    """
    data.to_csv(output_path, index=False)
    print(f"Processed data saved to {output_path}")


if __name__ == "__main__":
    main()
