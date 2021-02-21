import requests
import json
import pandas

from .models import Data


def get_date_list(date_first, date_second):
    date_pull = pandas.date_range(date_first, date_second, freq='D')
    out = []
    for i in date_pull:
        out.append(str(i.date()))
    return out[::-1]


def get_data_moex(date, login, password, active_list):
    s = requests.Session()

    s.get('https://passport.moex.com/authenticate', auth=(login, password))
    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:66.0) Gecko/20100101Firefox/66.0"}
    cookies = {'MicexPassportCert': s.cookies['MicexPassportCert']}

    all_data = []
    for active in active_list:
        url = "https://iss.moex.com/iss/analyticalproducts/futoi/securities/" + active[0:2] + ".json?from=" + date + "&till=" + date
        print(url)
        req = requests.get(url, headers=headers, cookies=cookies)
        all_data += json.loads(req.text)['futoi']['data']
    return all_data


def push_data(data):
    for i in range(0, len(data) - 1, 2):
        try:
            Data.objects.create(
                datetime=data[i][2] + ' ' + data[i][3],
                code = data[i][4],
                open_pos_yur_long=int(data[i][7]),
                open_pos_yur_short=int(abs(data[i][8])),
                open_pos_fiz_long=int(data[i + 1][7]),
                open_pos_fiz_short=int(abs(data[i + 1][8])),
                open_pos_all=int(data[i][7]) + int(abs(data[i][8])) + int(data[i + 1][7]) + int(
                    abs(data[i + 1][8])),
                number_persons_yur_long=int(data[i][9]),
                number_persons_yur_short=int(data[i][10]),
                number_persons_fiz_long=int(data[i + 1][9]),
                number_persons_fiz_short=int(data[i + 1][10]),
                number_persons_all=int(data[i][9]) + int(data[i][10]) + int(data[i + 1][9]) + int(
                    data[i + 1][10]),
            )
        except Exception as err:
            print(err)
            continue
