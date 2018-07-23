import csv
import json
import urllib.request
import pandas as pd

# Get Symbols from binance api
def get_symbols():
    url = "https://www.binance.com/api/v1/exchangeInfo"

    data = json.load(urllib.request.urlopen(url))

    symbols = data['symbols']

    with open('Binance_Symbols_Sorted.csv', 'w', newline='') as csvfile:
        fieldnames = ['Symbol', 'BTC', 'ETH', 'USDT', 'BNB']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for s in symbols:
            symb = s['symbol']
            length = len(symb)
            estring = symb[(length-3):length]
            # writer.writerow({'Symbol': symb})
            if estring == 'BTC':
                writer.writerow({'Symbol': symb, 'BTC': symb, 'ETH':'', 'USDT':'', 'BNB':''})
            elif estring == 'ETH':
                writer.writerow({'Symbol': symb, 'BTC': '', 'ETH': symb, 'USDT':'', 'BNB':''})
            elif estring == 'SDT':
                writer.writerow({'Symbol': symb, 'BTC': '', 'ETH':'', 'USDT': symb, 'BNB':''})
            elif estring == 'BNB':
                writer.writerow({'Symbol': symb, 'BTC':'', 'ETH':'', 'USDT':'', 'BNB': symb})
            else:
                writer.writerow({'Symbol': symb, 'BTC':'', 'ETH':'', 'USDT':'', 'BNB':''})
            
            #print(estring)

get_symbols()

