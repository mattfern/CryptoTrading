import csv
import time
import pandas as pd
import json
import urllib.request



with open('ETH.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for r in reader:
        symbol = r[0]
        length = len(symbol)
        fsym = symbol[:length-3]
        fsym = ''.join(['?fsym=', fsym])
        tsym = symbol[length-3:length]
        tsym = ''.join(['&tsym=',tsym])
        print(fsym, tsym)

        url = 'https://min-api.cryptocompare.com/data/histoday'

        data = json.load(urllib.request.urlopen(''.join([url,fsym,tsym])))
        data = data['Data']
        for d in data:
            print('Close: ', data[0]['close'])

