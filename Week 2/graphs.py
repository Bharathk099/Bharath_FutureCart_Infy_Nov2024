import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Set plot style
sns.set(style="whitegrid")

# Define the file path and check if it exists
file_path = r'C:\Users\pm5cd\Documents\FutureCart Project\Week 2\cleaned_master_dataset_updated.xlsx'

if not os.path.exists(file_path):
    print(f"Error: The file at {file_path} was not found. Please check the path.")
else:
    # Load the dataset
    df = pd.read_excel(file_path)

    # Ensure 'Day Index' is in datetime format
    df['Day Index'] = pd.to_datetime(df['Day Index'], errors='coerce')

    # Monthly Sales Plot
    monthly_sales = df.groupby(df['Day Index'].dt.month_name())['Quantity'].sum().reindex(
        ["January", "February", "March", "April", "May", "June", 
         "July", "August", "September", "October", "November", "December"]
    )

    plt.figure(figsize=(12, 6))
    sns.barplot(x=monthly_sales.index, y=monthly_sales.values, palette="viridis")
    plt.title("Monthly Sales")
    plt.xlabel("Month")
    plt.ylabel("Total Sales Quantity")
    plt.xticks(rotation=45)
    plt.show()

    # Weekend vs. Weekday Sales Plot
    df['Is_Weekend'] = df['Weekend'] == 1
    weekend_weekday_sales = df.groupby('Is_Weekend')['Quantity'].sum()
    weekend_weekday_sales.index = ['Weekday', 'Weekend']

    plt.figure(figsize=(8, 5))
    sns.barplot(x=weekend_weekday_sales.index, y=weekend_weekday_sales.values, palette="coolwarm")
    plt.title("Weekend vs. Weekday Sales")
    plt.xlabel("Day Type")
    plt.ylabel("Total Sales Quantity")
    plt.show()

    # Weekday Sales Plot
    weekday_sales = df.groupby(df['Day Index'].dt.day_name())['Quantity'].sum().reindex(
        ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    )

    plt.figure(figsize=(10, 5))
    sns.barplot(x=weekday_sales.index, y=weekday_sales.values, palette="magma")
    plt.title("Sales by Day of the Week")
    plt.xlabel("Day of the Week")
    plt.ylabel("Total Sales Quantity")
    plt.xticks(rotation=45)
    plt.show()

