#Testing with Yahoo Finance API

# install the yahoo finance API package with !pip install yfinance

# Import necessary packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
import yfinance as yf

msft = yf.Ticker("MSFT")
msft.info

# Define the ticker symbols for Facebook and Microsoft
tickers = ["META", "MSFT"]

# Fetch the stock data
start_date = '2021-04-01'
data = yf.download(tickers, start=start_date, end=None)

# Plot the closing prices
plt.figure(figsize=(10, 5))
plt.plot(data['Close']['META'], label='Facebook (META)')
plt.plot(data['Close']['MSFT'], label='Microsoft (MSFT)')
plt.title('Facebook (Meta) and Microsoft Closing Prices Over the Past Year')
plt.xlabel('Date')
plt.ylabel('Closing Price (USD)')
plt.legend()
plt.grid(True)
plt.show()

# Calculate moving averages
moving_averages = {
    '30 Day MA': data['Close'].rolling(window=30).mean(),
    '90 Day MA': data['Close'].rolling(window=90).mean(),
    '180 Day MA': data['Close'].rolling(window=180).mean()
}

# Visualize the moving averages
plt.figure(figsize=(14, 7))
for label, ma in moving_averages.items():
    plt.plot(ma['META'], label=f'META {label}')
    plt.plot(ma['MSFT'], label=f'MSFT {label}')
plt.title('Moving Averages for META and MSFT')
plt.xlabel('Date')
plt.ylabel('Closing Price (USD)')
plt.legend()
plt.grid(True)
plt.show()
