import csv
import json
import urllib.request
import pandas as pd
import os
import datetime

# Get Symbols from binance api
def get_symbols():
    url = "https://www.binance.com/api/v1/exchangeInfo"

    data = json.load(urllib.request.urlopen(url))

    symbols = data['symbols']

    if not os.path.exists('BTC_Symbols'):
        os.makedirs('BTC_Symbols')
    elif not os.path.exists('ETH_Symbols'):
        os.makedirs('ETH_Symbols')
    elif not os.path.exists('USDT_Symbols'):
        os.makedirs('USDT_Symbols')
    elif not os.path.exists('BNB_Symbols'):
        os.makedirs('BNB_Symobols')
    else:
        print('Dirs Exist')

    for s in symbols:
        symb = s['symbol']
        length = len(symb)
        estring = symb[(length-3):length]
        string = str(symb)

        if estring == 'BTC':
            with open('BTC.csv', 'a', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([string])

        elif estring == 'ETH':
            with open('ETH.csv', 'a', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([string])

        elif estring == 'SDT':
            with open('USDT.csv', 'a', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([string])

        elif estring == 'BNB':
            with open('BNB.csv', 'a', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([string])

# get_symbols()

def get_symbols_data(denominator):
    with open(denominator, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            print(' '.join(row))

# get_symbols_data('BTC.csv')
# get_symbols_data('ETH.csv')
# get_symbols_data('USDT.csv')
# get_symbols_data('BNB.csv')

# interval - one of (1m, 3m, 5m, 15m, 30m, 1h, 2h, 4h, 6h, 8h, 12h, 1d, 3d, 1w, 1M)
def get_price_data(denominator, interval):
    with open(''.join([denominator, '.csv']), newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            symbol = ''.join(row)
            url = "https://www.binance.com/api/v1/klines"
            symbolQ = ''.join(['?symbol=', symbol])
            intervalQ = ''.join(['&interval=', interval])
            #limitQ = ''.join(['&limit=', limit])
            query = ''.join([url, symbolQ, intervalQ])
            data = json.load(urllib.request.urlopen(query))
            # print(data[0][6])
            for d in data:    
                closetime = d[6]
                closetime = datetime.datetime.fromtimestamp(closetime/1000.0)
                closetime = closetime.strftime('%Y-%m-%d')
                print(closetime, symbol, d[1])

get_price_data('BTC', '1d')
