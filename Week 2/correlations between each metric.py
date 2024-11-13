# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = r'C:\Users\pm5cd\Documents\FutureCart Project\Week 2\cleaned_master_dataset.xlsx'
df = pd.read_excel(file_path, sheet_name='Sheet1')

# Convert 'Day Index' to datetime format for proper plotting
df['Day Index'] = pd.to_datetime(df['Day Index'])

# Plotting each metric individually over time
fig, axes = plt.subplots(nrows=3, ncols=1, figsize=(10, 12), sharex=True)

# Plot for Quantity (Sales)
axes[0].plot(df['Day Index'], df['Quantity'], color='blue', label='Quantity (Sales)')
axes[0].set_title('Quantity (Sales) over Time')
axes[0].set_xlabel('Date')
axes[0].set_ylabel('Quantity')
axes[0].legend()

# Plot for Google Clicks
axes[1].plot(df['Day Index'], df['Google Clicks'], color='green', label='Google Clicks')
axes[1].set_title('Google Clicks over Time')
axes[1].set_xlabel('Date')
axes[1].set_ylabel('Clicks')
axes[1].legend()

# Plot for FB Impressions
axes[2].plot(df['Day Index'], df['FB Impressions'], color='orange', label='FB Impressions')
axes[2].set_title('FB Impressions over Time')
axes[2].set_xlabel('Date')
axes[2].set_ylabel('Impressions')
axes[2].legend()

# Adjust layout and display the plots
plt.tight_layout()
plt.show()





