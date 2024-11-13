import pandas as pd

# Load the dataset from your Excel file
file_path = r'C:\Users\pm5cd\Documents\FutureCart Project\master_dataset.xlsx'
df = pd.read_excel(file_path)

# Step 1: Inspect the Data
print("Initial Data Info:")
print(df.info())
print("\nSummary of Numerical Data:")
print(df.describe())

# Step 2: Handle Missing Values
# Option 1: Imputation - Fill missing values with mean/median/mode (example uses mean for numerical columns)
df.fillna(df.mean(), inplace=True)  # For numerical columns
# For categorical columns, fill with mode
for column in df.select_dtypes(include=['object']).columns:
    df[column].fillna(df[column].mode()[0], inplace=True)

# Step 3: Handle Outliers
# Define a function to remove outliers based on Z-score or IQR
def remove_outliers(df, columns):
    for column in columns:
        if df[column].dtype in ['float64', 'int64']:  # Apply only on numerical columns
            # Calculate Q1 (25th percentile) and Q3 (75th percentile)
            Q1 = df[column].quantile(0.25)
            Q3 = df[column].quantile(0.75)
            IQR = Q3 - Q1
            # Filter out rows with values outside of 1.5*IQR range
            df = df[(df[column] >= Q1 - 1.5 * IQR) & (df[column] <= Q3 + 1.5 * IQR)]
    return df

# Apply the outlier removal on relevant columns
numerical_columns = df.select_dtypes(include=['float64', 'int64']).columns
df = remove_outliers(df, numerical_columns)

# Step 4: Save Cleaned Data
output_file_path = r'C:\Users\pm5cd\Documents\FutureCart Project\cleaned_master_dataset.xlsx'
df.to_excel(output_file_path, index=False)
    






            