from Myobject import *

class Main():
    def __init__(self):
        print(futures_wallet['USDT'])
        tickers = binance.fetch_tickers()

        for ticker in tickers:
            if ticker.endswith('USDT'):
                print(ticker)



if __name__ == '__main__':
    Main()