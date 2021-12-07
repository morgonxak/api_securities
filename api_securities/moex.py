'''
Модуль для работы с московской биржей
'''
import pandas
import requests
from requests.auth import HTTPBasicAuth
import json
import os
from datetime import datetime

login = os.getenv('MOEX_LOGIN')
password = os.getenv('MOEX_PASSWORD')

engine = 'futures'
market = 'forts'
board = 'RFUD'
security = 'GDZ1'
boardgroups = 45

request_url = f"https://iss.moex.com/cs/engines/{engine}/markets/{market}/boardgroups/{boardgroups}/securities/{security}.json?interval=1&candles=500&s1.type=candles"

def split_by_period(df, period):
    '''
    Разбиваем данные на нужный периуд
    period: 1Min, 5Min, 15Min, 30Min, 60Min
    '''
    return df.asfreq(period).dropna()

def get_data_from_moix(period):
    session = requests.get(request_url, auth=HTTPBasicAuth(login, password))
    data = session.json()['zones'][0]['series'][0]['candles']
    data_value = session.json()['zones'][1]['series'][0]['candles']

    res_data = []
    for i in data:
        i['open_time'] = datetime.fromtimestamp(i['open_time'] / 1000.0)
        i['close_time'] = datetime.fromtimestamp(i['close_time'] / 1000.0)
        res_data.append(i)

    df = pandas.DataFrame(res_data)
    df.set_index('open_time', inplace=True)

    value = [i['value'] for i in data_value]

    df['value'] = value
    df = df.loc[:, ['open', 'close', 'high', 'low', 'value']]
    return split_by_period(df, period)


