import requests
from datetime import datetime
import pandas
from .constant import *


def get_df_by_stick(curr_id, perion='15Min'):
    '''Получает df текуших значений акции'''
    url.format(curr_id)

    params['interval'] = periods[perion]
    req = requests.get(url.format(curr_id), params)

    if req.status_code != 200:
        raise ConnectionError(f"ERR#0015: error {req.status_code}, try again later.")

    data = req.json()
    data = data['data']
    results = []
    for elements_ in data:
        result = {
            'Date': datetime.strptime(str(datetime.fromtimestamp(elements_[0] / 1000.0)), '%Y-%m-%d %H:%M:%S'),
            'Open': float(elements_[2]),
            'High': float(elements_[4]),
            'Low': float(elements_[3]),
            'Close': float(elements_[1])
        }
        results.append(result)
    df = pandas.DataFrame(results)
    df.index = df['Date']
    del df['Date']
    return df



if __name__ == '__main__':
    curr_id = 8830
    df = get_df_by_stick(curr_id)
    print(df)