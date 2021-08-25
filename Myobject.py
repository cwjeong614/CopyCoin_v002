import asyncio
import json

from msg_telegram import *
import ccxt
import pprint
import pandas as pd
import sqlite3
from Mylog import log
from binance.client import Client
from binance.client import AsyncClient

class MyObject():
    def __init__(self):
        with open('APIKey.txt') as f:
            lines = f.readlines()
            self.api_key = lines[0].strip()
            self.secret = lines[1].strip()

    async def main(self):
        self.client = await AsyncClient.create(self.api_key, self.secret, testnet=False)

        # self.res = await self.client.get_exchange_info()
        self.res = await self.client.get_account_snapshot(type='FUTURES')

        print(json.dumps(self.res, indent=2))

        await self.client.close_connection()

if __name__ == '__main__':
    obj = MyObject()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(obj.main())