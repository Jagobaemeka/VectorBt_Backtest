import numpy as np
import pandas as pd
import vectorbt as vbt

# Assuming btc_price is loaded correctly and contains the 'Close' column
btc_price = pd.read_csv("BTC-USD.csv")[["Date", "Close"]]
btc_price['Close'] = pd.to_numeric(btc_price['Close'], errors='coerce')
btc_price.dropna(inplace=True)

# Calculate RSI
rsi = vbt.RSI.run(btc_price['Close'], window=14)

# Find where RSI crossed below 30
rsi_below_30 = rsi.rsi < 30
entries = rsi_below_30.vbt.crossed_below(True)

print(entries)

