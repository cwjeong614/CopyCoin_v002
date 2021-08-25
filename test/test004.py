import pandas as pd

from Myobject import *

client = Client()
klines = client.get_historical_klines(
    'BTCUSDT',
    client.KLINE_INTERVAL_15MINUTE,
    "1 Jun, 2021"
)

print(klines[-1])

# df = pd.DataFrame(klines, columns=['datetime', 'open', 'high', 'low', 'close', 'volume'])
# df['datetime'] = pd.to_datetime(df['datetime'], unit='ms')
# df.set_index('datetime', unit='ms')
#
# print(df)