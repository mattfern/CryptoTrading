import csv
import json
import urllib.request
import pandas as pd

# Get Symbols from binance api
def get_symbols():
    url = "https://www.binance.com/api/v1/exchangeInfo"

    data = json.load(urllib.request.urlopen(url))

    symbols = data['symbols']

    with open('Binance_Symbols.csv', 'w', newline='') as csvfile:
        fieldnames = ['Symbol']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for s in symbols:
            symb = s['symbol']
            writer.writerow({'Symbol': symb})
            print(s['symbol'])

# get_symbols()

# Load Binance_Symbols.csv into pandas dataframe

def make_df():
    ReadCSV = pd.read_csv('Binance_Symbols.csv')
    df = pd.DataFrame(ReadCSV)
    print(df[1])

make_df() 