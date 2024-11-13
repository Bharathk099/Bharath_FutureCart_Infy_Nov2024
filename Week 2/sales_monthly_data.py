import pandas as pd

# Load the dataset from your Excel file
file_path = r'C:\Users\pm5cd\Documents\FutureCart Project\master_dataset.xlsx'
df = pd.read_excel(file_path)

# Display column names to confirm the correct date column name
print("Column names in the dataset:", df.columns)

# Convert the 'Day Index' column to datetime format
df['Day Index'] = pd.to_datetime(df['Day Index'], errors='coerce')

# Verify conversion by displaying the first few rows of 'Day Index'
print("First few entries in 'Day Index' after conversion:\n", df['Day Index'].head())

# Check for any NaT values
if df['Day Index'].isnull().sum() > 0:
    print(f"There are {df['Day Index'].isnull().sum()} unconvertible dates in 'Day Index' column.")
else:
    print("All entries in 'Day Index' converted successfully.")

# Create a copy of the data to avoid modifying the original DataFrame
df_resampled = df.copy()

# Set the 'Day Index' column as the index in the copy
df_resampled.set_index('Day Index', inplace=True)

# Resample data to a monthly frequency (using 'ME' for month-end) and calculate sums for each month
df_monthly = df_resampled.resample('ME').sum()  # 'ME' for month-end, 'W' for week, 'D' for day

# Save the resampled data to a new Excel file without modifying the original data
output_file_path = r'C:\Users\pm5cd\Documents\FutureCart Project\sales_monthly_data.xlsx'
df_monthly.to_excel(output_file_path)




