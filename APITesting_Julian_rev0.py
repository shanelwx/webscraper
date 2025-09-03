#Testing with Yahoo Finance API

# install the yahoo finance API package with !pip install yfinance

# Import necessary packages
import pandas as pd
import numpy as np
import matplotlib as plt
from datetime import datetime
import yfinance as yf

msft = yf.Ticker("MSFT")
info = msft.get_info()
print(info)
