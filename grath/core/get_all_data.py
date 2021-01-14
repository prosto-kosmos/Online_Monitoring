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


def get_data_moex(date, active, login, password):
    s = requests.Session()

    s.get('https://passport.moex.com/authenticate', auth=(login, password))
    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:66.0) Gecko/20100101Firefox/66.0"}
    cookies = {'MicexPassportCert': s.cookies['MicexPassportCert']}

    url = "https://iss.moex.com/iss/analyticalproducts/futoi/securities/" + active[0:2] + ".json?from=" + date + "&till=" + date
    url2 = "http://iss.moex.com/iss/history/engines/futures/markets/forts/boards/RFUD/securities/" + active + ".json?from=" + date + "&till=" + date
    req = requests.get(url, headers=headers, cookies=cookies)
    req2 = requests.get(url2, headers=headers, cookies=cookies)

    data = json.loads(req.text)['futoi']['data']
    data_dop = json.loads(req2.text)['history']['data']
    try:
        list_dop = [str(data_dop[0][2]), float(data_dop[0][6]), int(data_dop[0][9]), int(data_dop[0][10])]
    except Exception:
        list_dop = [None, None, None, None]
    all_data_on_one_day = [data, list_dop]
    return all_data_on_one_day


def push_data(data, dop_data, count, count_all, progress_recoder):
    for i in range(0, len(data) - 1, 2):
        try:
            Data.objects.create(
                datetime=data[i][2] + ' ' + data[i][3],
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
                close=dop_data[1],
                capacity_control=dop_data[2],
                open_pos_control=dop_data[3],
                short_code=dop_data[0]
            )
        except Exception as err:
            print(err)
            continue
        finally:
            progress_recoder.set_progress(count, count_all, f'Идет процесс добавления данных в таблицу. Повторный '
                                                            f'запрос данных до завершения всех операций нежелателен!')
            count += 1
    return count
