import os
import glob
import pandas as pd


def average_csv_close(folder_path, column_name='Close'):
    # Get all CSV files in the folder
    csv_files = glob.glob(os.path.join(folder_path, '*.csv'))

    if not csv_files:
        print("No CSV files found in the given folder.")
        return

    dataframes = []

    # Read only 'Close' column from each file
    for file in csv_files:
        try:
            df = pd.read_csv(file, usecols=[column_name])
            dataframes.append(df)
        except Exception as e:
            print(f"Skipping {file}: {e}")

    if not dataframes:
        print("No valid data read from CSV files.")
        return

    # Combine 'Close' columns and calculate row-wise mean
    combined_df = pd.concat(dataframes, axis=1)
    average_series = combined_df.mean(axis=1, skipna=True)

    # Read the date column from the first CSV file
    try:
        date_df = pd.read_csv(csv_files[0], usecols=['FormattedDate'])
    except Exception as e:
        print(f"Error reading 'Date' from {csv_files[0]}: {e}")
        return

    # Create final dataframe with 'Date' and averaged 'Close' column
    result_df = pd.DataFrame({
        'FormattedDate': date_df['FormattedDate'],
        column_name: average_series
    })

    # Save as average_file.csv
    output_file = os.path.join(folder_path, 'average_file.csv')
    result_df.to_csv(output_file, index=False)

    print(f"Average 'Close' values with 'Date' written to {output_file}")

# Example usage:
average_csv_close("C:/PythonAutomation/quant")
