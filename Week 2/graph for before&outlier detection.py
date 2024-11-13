# Let's load the newly uploaded dataset, perform outlier detection, and generate the requested time series plots.

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the new dataset
file_path = r'C:\Users\pm5cd\Documents\FutureCart Project\Week 2\master_dataset.xlsx'
df = pd.read_excel(file_path)

# Convert 'Day Index' to datetime format and set as index
df['Day Index'] = pd.to_datetime(df['Day Index'], errors='coerce')
df = df.set_index('Day Index').sort_index()

# Plot Sales over Time Before Outlier Removal
plt.figure(figsize=(12, 6))
plt.plot(df.index, df['Quantity'], label="Original Sales (with Outliers)", color='blue')
plt.title("Sales Over Time - Before Outlier Removal")
plt.xlabel("Date")
plt.ylabel("Sales Quantity")
plt.legend()
plt.show()

# Detect and Remove Outliers using IQR
Q1 = df['Quantity'].quantile(0.25)
Q3 = df['Quantity'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
df_no_outliers = df[(df['Quantity'] >= lower_bound) & (df['Quantity'] <= upper_bound)]

# Plot Sales over Time After Outlier Removal
plt.figure(figsize=(12, 6))
plt.plot(df_no_outliers.index, df_no_outliers['Quantity'], label="Cleaned Sales (without Outliers)", color='green')
plt.title("Sales Over Time - After Outlier Removal")
plt.xlabel("Date")
plt.ylabel("Sales Quantity")
plt.legend()
plt.show()


