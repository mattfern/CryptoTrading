import csv
import json
import urllib.request
import pandas as pd

# Get Symbols from coinmarket cap api
def get_symbols():
    url = "https://api.coinmarketcap.com/v2/listings/"

    data = json.load(urllib.request.urlopen(url))
    data = data['data']
    # print(data['data'][0])

    # for d in data['data']:
    #     print(d['name'], d['symbol'])

    df = pd.DataFrame(data)
    df.reset_index(inplace=True)
    df.set_index("id", inplace=True)
    df = df.drop("website_slug", axis=1)
    df = df.drop("index", axis=1)
    df.to_csv('Crypto_Symobols.csv')

get_symbols()