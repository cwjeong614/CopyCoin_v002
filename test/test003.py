# 분봉 조회

import ccxt
import pprint
import pandas as pd
import matplotlib.pyplot as plt

binance = ccxt.binance()

tickers = binance.fetch_tickers()
for k, v in tickers.items():
    print(k, v)

# # btc_ohlcv = binance.fetch_ohlcv('BTC/USDT')             # 1분봉
btc_ohlcv = binance.fetch_ohlcv('BTC/USDT', '1h')       # 일봉
#
df = pd.DataFrame(btc_ohlcv, columns=['datetime', 'open', 'high', 'low', 'close', 'volume'])
df['datetime'] = pd.to_datetime(df['datetime'], unit='ms')
df['pct_change'] = df['close'].pct_change()
df.set_index('datetime', inplace=True)
# df.to_excel('BTC_USDT.xlsx')

plt.hist(df['pct_change'], bins=30)
plt.show()
#
# # print(df)