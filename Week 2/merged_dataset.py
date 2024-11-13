import pandas as pd
from io import BytesIO
import matplotlib.pyplot as plt

# File paths for the three Excel files
data_file_path = r"C:\Users\pm5cd\Downloads\ProductA.xlsx"
data_file_path1 = r"C:\Users\pm5cd\Downloads\ProductA_google_clicks.xlsx"
data_file_path2 = r"C:\Users\pm5cd\Downloads\ProductA_fb_impressions.xlsx"

# Read each Excel file separately
df_quantity = pd.read_excel(data_file_path)
df_google_clicks = pd.read_excel(data_file_path1)
df_fb_impressions = pd.read_excel(data_file_path2)

# Display the columns to verify their names
print("Columns in df_quantity:", df_quantity.columns)
print("Columns in df_google_clicks:", df_google_clicks.columns)
print("Columns in df_fb_impressions:", df_fb_impressions.columns)

# Rename columns to avoid conflicts and for clarity
df_google_clicks = df_google_clicks.rename(columns={'Clicks': 'Google Clicks'})
df_fb_impressions = df_fb_impressions.rename(columns={'Impressions': 'FB Impressions'})

# Merge DataFrames on "Day Index" using outer joins to retain all Day Index values from df_quantity
master_dataset = df_quantity.merge(df_google_clicks, on="Day Index", how="left") \
                            .merge(df_fb_impressions, on="Day Index", how="left")

# Output path for the Excel file
output = r"C:\Users\pm5cd\Documents\FutureCart Project\master_dataset.xlsx"

# Save the merged dataset to an Excel file
master_dataset.to_excel(output, index=False)

# Print a confirmation message
print("Merged dataset saved to:", output)

# Create a boxplot for each numerical column in the merged dataset
plt.figure(figsize=(10, 6))
master_dataset.boxplot(column=['Quantity', 'Google Clicks', 'FB Impressions'])
plt.title("Boxplot of Quantity, Google Clicks, and FB Impressions")
plt.ylabel("Values")
plt.xticks(rotation=65)
plt.show()



