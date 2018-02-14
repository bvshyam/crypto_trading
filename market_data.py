# DATA698  Crypto Project
# market_data.py
#This file pulls the historical market data from cryptocompare.com

import sys
import requests
import datetime
import pandas as pd
import matplotlib.pyplot as plt

def arg_check():
    if len(arg) != 3:
        print ("Usage: Crypto BaseCurrency candle_size")

def daily_price_historical(symbol, comparison_symbol, all_data=True, limit=1, aggregate=1, exchange=''):
    url = 'https://min-api.cryptocompare.com/data/histoday?fsym={}&tsym={}&limit={}&aggregate={}'\
            .format(symbol.upper(), comparison_symbol.upper(), limit, aggregate)
    if exchange:
        url += '&e={}'.format(exchange)
    if all_data:
        url += '&allData=true'
    page = requests.get(url)
    data = page.json()['Data']
    df = pd.DataFrame(data)
    df['timestamp'] = [datetime.datetime.fromtimestamp(d) for d in df.time]
    return df


def hourly_price_historical(symbol, comparison_symbol, limit, aggregate, exchange=''):
    url = 'https://min-api.cryptocompare.com/data/histohour?fsym={}&tsym={}&limit={}&aggregate={}'\
            .format(symbol.upper(), comparison_symbol.upper(), limit, aggregate)
    if exchange:
        url += '&e={}'.format(exchange)
    page = requests.get(url)
    data = page.json()['Data']
    df = pd.DataFrame(data)
    df['timestamp'] = [datetime.datetime.fromtimestamp(d) for d in df.time]
    return df


def minute_price_historical(symbol, comparison_symbol, limit, aggregate, exchange=''):
    url = 'https://min-api.cryptocompare.com/data/histominute?fsym={}&tsym={}&limit={}&aggregate={}'\
            .format(symbol.upper(), comparison_symbol.upper(), limit, aggregate)
    if exchange:
        url += '&e={}'.format(exchange)
    page = requests.get(url)
    data = page.json()['Data']
    df = pd.DataFrame(data)
    df['timestamp'] = [datetime.datetime.fromtimestamp(d) for d in df.time]
    return df


def writecsv(df, filename):
    df.to_csv(filename)
    print(filename, "saved")


def main():
    daily = daily_price_historical('BTC', 'USD')
    writecsv(daily, 'BTC_daily.csv')
    hourly = hourly_price_historical('BTC', 'USD', 9999, 24)
    writecsv(hourly, 'BTC_hourly.csv')
    minute = minute_price_historical('BTC', 'USD', 9999, 1)
    writecsv(minute, 'BTC_minute.csv')



if  __name__ =='__main__':
    main()