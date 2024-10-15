import yfinance as yf
from pprint import pprint
import json

source = input("Source currency (default 'USD'): ") or "USD"
target = input("Target currency (default 'LBP'):") or "LBP"
period = input("Period (default '1d'):") or "1d"
# '1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max'
# Fetch the USD to EUR exchange rate
res = yf.Ticker(f"{source}{target}=X")

# Get the latest market data
res_data = res.history(period=period)

# Extract and print the last close price (this is the exchange rate)
print(f"Rates for Curr: {target}")
pprint(res_data)