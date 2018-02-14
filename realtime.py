# DATA698  Crypto Project
# market_data.py
#This file pulls the realtime market data from cryptocompare.com with 15 sec sleep

import requests
import datetime
import pandas as pd
import time
import json

def price(symbol, comparison_symbols=['USD'], exchange=''):
    url = 'https://min-api.cryptocompare.com/data/price?fsym={}&tsyms={}'\
            .format(symbol.upper(), ','.join(comparison_symbols).upper())
    if exchange:
        url += '&e={}'.format(exchange)
    page = requests.get(url)
    data = page.json()
    return data

def main():
    while 1:
        tickj = (price('BTC', exchange='Coinbase'))
        print datetime.datetime.now(), tickj['USD']
        time.sleep(15)



if __name__ == '__main__':
    main()