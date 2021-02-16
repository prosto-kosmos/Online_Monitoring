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
            'dt': dt[::-1],
            'islogin': True,
            'message':'',
        }
        
        if param == 'gr_online_op':
            context.update({
                'data_1':opyl[::-1],
                'data_2':opys[::-1],
                'data_3':opfl[::-1],
                'data_4':opfs[::-1],
                'title_1':'Онлайн-график «Открытые позиции. Юридические лица (Длинные)»',
                'title_2':'Онлайн-график «Открытые позиции. Юридические лица (Короткие)»',
                'title_3':'Онлайн-график «Открытые позиции. Физические лица (Длинные)»',
                'title_4':'Онлайн-график «Открытые позиции. Физические лица (Короткие)»',
                'param':'open_pos',
            })
        elif param == 'gr_online_np':
            context.update({
                'data_1':cpyl[::-1],
                'data_2':cpys[::-1],
                'data_3':cpfl[::-1],
                'data_4':cpfs[::-1],
                'title_1':'Онлайн-график «Количество лиц. Юридические лица (Длинные)»',
                'title_2':'Онлайн-график «Количество лиц. Юридические лица (Короткие)»',
                'title_3':'Онлайн-график «Количество лиц. Физические лица (Длинные)»',
                'title_4':'Онлайн-график «Количество лиц. Физические лица (Короткие)»',
                'param':'num_pers',
            })
        return context


def get_new_points(count_points, request, param):
    try:
        login = request.COOKIES["login"]
        password = request.COOKIES["password"]
        active = request.COOKIES["active"]
    except KeyError:
        return json.dumps({
            'x':[],
            'y1':[],
            'y2':[],
            'y3':[],
            'y4':[],
        })
        
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
            return json.dumps({
                'x':[],
                'y1':[],
                'y2':[],
                'y3':[],
                'y4':[],
            })

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
        
        if len(dt)==count_points:
            return json.dumps({
                'x':[],
                'y1':[],
                'y2':[],
                'y3':[],
                'y4':[],
            })
        else:
            dt = dt[:(len(dt)-count_points)]
            opyl = opyl[:(len(opyl)-count_points)]
            opys = opys[:(len(opys)-count_points)]
            opfl = opfl[:(len(opfl)-count_points)]
            opfs = opfs[:(len(opfs)-count_points)]
            cpyl = cpyl[:(len(cpyl)-count_points)]
            cpys = cpys[:(len(cpys)-count_points)]
            cpfl = cpfl[:(len(cpfl)-count_points)]
            cpfs = cpfs[:(len(cpfs)-count_points)]

        if param == 'open_pos':
            return json.dumps({
                'x':dt[::-1],
                'y1':opyl[::-1],
                'y2':opys[::-1],
                'y3':opfl[::-1],
                'y4':opfs[::-1],
            })
        elif param == 'num_pers':
            return json.dumps({
                'x':dt[::-1],
                'y1':cpyl[::-1],
                'y2':cpys[::-1],
                'y3':cpfl[::-1],
                'y4':cpfs[::-1],
            })