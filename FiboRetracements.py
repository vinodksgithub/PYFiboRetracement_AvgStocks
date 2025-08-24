import pandas as pd
import matplotlib.pyplot as plt


#Calulate the high and low for fibo retracement
def print_close_high_low(df):
    high = df['Close'].max()
    low = df['Close'].min()
    print(f"Highest Close Price: {high}")
    print(f"Lowest Close Price: {low}")
    return high, low

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

# Get high and low close prices
high, low = print_close_high_low(df)

# Fibonacci levels between high and low (0% for high, 100% for low)
fib_levels = [0, 0.236, 0.382, 0.5, 0.618, 0.786, 1.0]
fib_prices = [high - (high - low) * level for level in fib_levels]

# Plot closing price and 50-day moving average over time
plt.figure(figsize=(12, 6))
plt.plot(df['FormattedDate'], df['Close'], linestyle='-', color='b', label='Close Price')
plt.plot(df['FormattedDate'], df['50_MA'], linestyle='--', color='orange', label='50-Day MA')

# Draw Fibonacci retracement dotted lines with different colors, no legend labels
colors = ['red', 'purple', 'green', 'blue', 'brown', 'gray', 'black']
for price, color, level in zip(fib_prices, colors, fib_levels):
    plt.axhline(price, linestyle=':', color=color)
    # Place retracement % and value on right side
    plt.text(df['FormattedDate'].iloc[-1], price, f'{int(level*100)}% ({price:.2f})',
             color=color, va='center', ha='left', fontsize=9, fontweight='bold')

plt.title('Stock Closing Price & 50-Day Moving Average Over Time with Fibonacci Retracements')
plt.xlabel('Date')
plt.ylabel('Close Price')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
