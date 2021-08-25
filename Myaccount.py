from Myobject import *

with open('APIKey.txt') as f:
    lines = f.readlines()
    api_key = lines[0].strip()
    secret = lines[1].strip()

binance = ccxt.binance(config={
    'apiKey': api_key,
    'secret': secret
})

# balance = binance.fetch_balance()                               # 현물 지갑
balance = binance.fetch_balance(params={'type':'future'})       # 선물 지갑
pprint.pprint(balance['USDT'])