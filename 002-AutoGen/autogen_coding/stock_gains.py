# filename: stock_gains.py
import matplotlib.pyplot as plt
import yfinance as yf

# Define the ticker symbols for TSLA and META
tickers = ['TSLA', 'META']

# Download the historical stock price data
data = yf.download(tickers, start='2024-01-01', end='2024-03-21')

# Calculate the cumulative gains YTD for each stock
gains = data['Close'].pct_change().cumsum()

# Plot the gains
plt.plot(gains.index, gains['TSLA'], label='TSLA')
plt.plot(gains.index, gains['META'], label='META')
plt.xlabel('Date')
plt.ylabel('Cumulative Gain YTD')
plt.legend()

# Save the plot to a file
plt.savefig('stock_gains.png')
plt.close()