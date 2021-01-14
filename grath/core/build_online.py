import requests
import json
import pandas
from datetime import datetime

from .models import Data



def get_date_list(self, date_first, date_second):
    date_pull = pandas.date_range(date_first, date_second, freq='D')
    out = []
    for i in date_pull:
        out.append(str(i.date()))
    return out[::-1]


def get_context_online(param, request):
    try:
        login = request.COOKIES["login"]
        password = request.COOKIES["password"]
        active = request.COOKIES["active"]
    except KeyError:
        return {
            'dt':[],
            'data':[],
            'islogin': False,
            'message':'',
        }
        
    else:
        date = str(datetime.now().date())
        s = requests.Session()
        try:
            s.get('https://passport.moex.com/authenticate', auth=(login, password))
            headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:66.0) Gecko/20100101Firefox/66.0"}
            cookies = {'MicexPassportCert': s.cookies['MicexPassportCert']}

            url = "https://iss.moex.com/iss/analyticalproducts/futoi/securities/" + active[0:2] + ".json?from=" + date + "&till=" + date
            url2 = "http://iss.moex.com/iss/history/engines/futures/markets/forts/boards/RFUD/securities/" + active + ".json?from=" + date + "&till=" + date
            req = requests.get(url, headers=headers, cookies=cookies)
            req2 = requests.get(url2, headers=headers, cookies=cookies)
        except:
            return {
                'dt':[],
                'data':[],
                'islogin': False,
                'message': 'Не удалось получить данные с сайта moex.com',
            }

        data = json.loads(req.text)['futoi']['data']
        data_dop = json.loads(req2.text)['history']['data']
        try:
            list_dop = [str(data_dop[0][2]), float(data_dop[0][6]), int(data_dop[0][9]), int(data_dop[0][10])]
        except Exception:
            list_dop = [None, None, None, None]

        dt = []
        opyl, opys, opfl, opfs = [],[],[],[]
        cpyl, cpys, cpfl, cpfs = [],[],[],[]

        for i in range(0, len(data) - 1, 2):
            dt.append(data[i][2] + ' ' + data[i][3])

            opyl.append(int(data[i][7]))
            opys.append(int(abs(data[i][8])))
            opfl.append(int(data[i + 1][7]))
            opfs.append(int(abs(data[i + 1][8])))
            
            cpyl.append(int(data[i][9]))
            cpys.append(int(data[i][10]))
            cpfl.append(int(data[i + 1][9]))
            cpfs.append(int(data[i + 1][10]))

        context = {
            'dt': dt,
            'islogin': True,
            'message':'',
        }
        
        if param == 'opyl':
            context.update({
                'data':opyl[::-1],
                'title':'Онлайн-график «Открытые позиции. Юридические лица (Длинные)» за ' + date,
            })
        elif param == 'opys':
            context.update({
                'data':opys[::-1],
                'title':'Онлайн-график «Открытые позиции. Юридические лица (Короткие)» за ' + date,
            })
        elif param == 'opfl':
            context.update({
                'data':opfl[::-1],
                'title':'Онлайн-график «Открытые позиции. Физические лица (Длинные)» за ' + date,
            })
        elif param == 'opfs':
            context.update({
                'data':opfs[::-1],
                'title':'Онлайн-график «Открытые позиции. Физические лица (Короткие)» за ' + date,
            })
        elif param == 'cpyl':
            context.update({
                'data':cpyl[::-1],
                'title':'Онлайн-график «Количество лиц. Юридические лица (Длинные)» за ' + date,
            })
        elif param == 'cpys':
            context.update({
                'data':cpys[::-1],
                'title':'Онлайн-график «Количество лиц. Юридические лица (Короткие)» за ' + date, 
            })
        elif param == 'cpfl':
            context.update({
                'data':cpfl[::-1],
                'title':'Онлайн-график «Количество лиц. Физические лица (Длинные)» за ' + date,
            })
        elif param == 'cpfs':
            context.update({
                'data':cpfs[::-1],
                'title':'Онлайн-график «Количество лиц. Физические лица (Короткие)» за ' + date,
            })
        return context