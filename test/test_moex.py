from api_securities import moex



if __name__ == '__main__':


    periods = ['1Min', '5Min', '15Min', '30Min', '60Min']
    data = moex.get_data_from_moix(periods[0])
    print(data)