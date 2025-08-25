import pandas as pd
import datetime
import glob
import os


# First file to run...

def format_dates_in_csvs(folder_path):
    # Find all CSV files in the given folder
    csv_files = glob.glob(os.path.join(folder_path, "*.csv"))

    for file in csv_files:
        # Read CSV
        df = pd.read_csv(file)

        # Convert Date column to desired format
        def format_date(date_str):
            # Example date_str: 'Thu Sep 19 2024 00:00:00 GMT+0530 (India Standard Time)'
            try:
                dt = datetime.datetime.strptime(date_str.split(' GMT')[0], "%a %b %d %Y %H:%M:%S")
                # Format as 'dd-MMM-yy'
                return dt.strftime('%d-%b-%y')
            except Exception as e:
                return None  # or handle error appropriately

        df['FormattedDate'] = df['Date'].apply(format_date)

        # Save the updated CSV (optional)
        df.to_csv(file, index=False)

        print(f"Processed file: {file}")
        print(df[['Date', 'FormattedDate']].head())  # Show result sample


# Usage:
format_dates_in_csvs("C:\\PythonAutomation\\quant\\raw")
