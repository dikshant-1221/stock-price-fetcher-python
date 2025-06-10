import yfinance as yf
import pandas as pd

ticker = "TCS.NS"
data = yf.download(ticker, period="30d")
data.to_csv(f"{ticker}_data.csv")
print(f"{ticker} data saved to CSV successfully!")
