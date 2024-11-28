import pandas as pd

# Specify the path to your Excel file
file_path = "data/nyc_aging_contracts_cleaned.csv"

# Read the Excel file
data = pd.read_csv(file_path)

# Display the first few rows
# print(data.head())
# print(data["Census Tract"].head(20))

"""
Cleaning the data
1. remove leading single quotes from 'DFTA ID' column
2. check for missing values in 'Census Tract' column - two white plains contractor found
3. convert 'Census Tract' column to integer then string
"""
# # Remove leading single quotes from 'DFTA ID' column
# data["DFTA ID"] = data["DFTA ID"].str.lstrip("'")
# print("cleaned:", data["DFTA ID"].head(20))

# # Check for missing value in the 'Census Tract' column
missing_values_count = data["Census Tract"].isnull().sum()
missing_rows = data[data["DFTA ID"].isnull()]
print(f"Number of missing values in 'Census Tract' column: {missing_values_count}")
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

# Handle missing values (if any)
data["Census Tract"] = data["Census Tract"].fillna(0)

data["CensusTractFormatted"] = data["Census Tract"].apply(
    lambda x: f"{int(x):04d}.00" if x < 1000 else x
)

print(data["CensusTractFormatted"].head())


# # Convert float to integer first, then to string
# data["Census Tract"] = data["Census Tract"].apply(
#     lambda x: str(int(x)) if x != "" else x
# )

# data["Census Tract"] = data["Census Tract"].astype(str)

# Verify the change
print(data["Census Tract"].dtype)

print(data["Census Tract"].head())

# # Save the cleaned data back to a new file
# cleaned_file_path = "data/nyc_aging_contracts_cleaned.csv"
# data.to_csv(cleaned_file_path, index=False)
