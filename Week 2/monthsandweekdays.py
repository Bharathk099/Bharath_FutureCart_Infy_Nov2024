import pandas as pd
import os

# Define the file path to your dataset
file_path = r'C:\Users\pm5cd\Documents\FutureCart Project\Week 2\cleaned_master_dataset.xlsx'

# Check if the input file exists
if not os.path.exists(file_path):
    print(f"Error: The file at {file_path} was not found. Please check the path.")
else:
    # Load the dataset
    df = pd.read_excel(file_path)

    # Convert 'Day Index' to datetime format
    df['Day Index'] = pd.to_datetime(df['Day Index'], errors='coerce')

    # Create 'Weekend' column
    df['Weekend'] = df['Day Index'].dt.weekday.isin([5, 6]).astype(int)

    # Create columns for each day of the week
    for day in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']:
        df[day] = (df['Day Index'].dt.day_name() == day).astype(int)

    # Create columns for each month by name (e.g., 'January', 'February', etc.)
    month_names = ['January', 'February', 'March', 'April', 'May', 'June', 
                   'July', 'August', 'September', 'October', 'November', 'December']
    
    for month_num, month_name in enumerate(month_names, start=1):
        df[month_name] = (df['Day Index'].dt.month == month_num).astype(int)

    # Define the output file path for saving the updated dataset
    output_file_path = r'C:\Users\pm5cd\Documents\FutureCart Project\Week 2\cleaned_master_dataset_updated.xlsx'

    # Ensure the output folder exists, if not create it
    output_folder = os.path.dirname(output_file_path)
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Save the updated DataFrame to a new Excel file
    df.to_excel(output_file_path, index=False)

    # Display the first few rows to verify the changes
    print(df.head())



