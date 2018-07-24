import csv
import json
import urllib.request
import pandas as pd
import os

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

get_symbols_data('BTC.csv')
get_symbols_data('ETH.csv')
get_symbols_data('USDT.csv')
get_symbols_data('BNB.csv')
