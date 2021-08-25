import ccxt

binance = ccxt.binance()
markets = binance.load_markets()

# print(type(markets))
# print(markets.keys())

# for mkt in markets.keys():
#     print(mkt)
#
# print(len(markets))

for market in markets.keys():
    if market.endswith('USDT'):     # ex. BTC/USDT
        print(market)