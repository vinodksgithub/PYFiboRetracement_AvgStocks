import pandas as pd
import matplotlib.pyplot as plt


def print_close_high_low(df):
    high = df['Close'].max()
    low = df['Close'].min()
    print(f"Highest Close Price: {high}")
    print(f"Lowest Close Price: {low}")


# Load data from CSV file
stock_name= "ERIS"
df = pd.read_csv(f'C:\\PythonAutomation\\quant\\{stock_name}.csv')

# First try the 4-digit year
dt1 = pd.to_datetime(df['FormattedDate'], format='%d-%b-%Y', errors='coerce')

# For failed parses (NaT), try 2-digit year
dt2 = pd.to_datetime(df['FormattedDate'], format='%d-%b-%y', errors='coerce')

# Use whichever is not NaT
df['FormattedDate'] = dt1.combine_first(dt2)

# Calculate 50-day moving average for the 'Close' price
df['50_MA'] = df['Close'].rolling(window=50).mean()

# Plot closing price and 50-day moving average over time
print_close_high_low(df)
plt.figure(figsize=(12, 6))
plt.plot(df['FormattedDate'], df['Close'], linestyle='-', color='b', label='Close Price')
plt.plot(df['FormattedDate'], df['50_MA'], linestyle='--', color='orange', label='50-Day MA')
plt.title(' Stock Closing Price & 50-Day Moving Average Over Time')
plt.xlabel('Date')
plt.ylabel('Close Price')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()


