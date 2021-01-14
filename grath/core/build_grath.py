import requests
import json
import pandas as pd
from datetime import datetime
from .models import Data

def get_context_grath(param):
    all_data = Data.objects.all()
    dt, ds = [],[],
    opyl, opys, opfl, opfs = [],[],[],[]
    cpyl, cpys, cpfl, cpfs = [],[],[],[]
    if len(all_data) > 0:
        for line in all_data:
            dt.append(line.datetime)
            opyl.append(line.open_pos_yur_long)
            opys.append(line.open_pos_yur_short)
            opfl.append(line.open_pos_fiz_long)
            opfs.append(line.open_pos_fiz_short)
            cpyl.append(line.number_persons_yur_long)
            cpys.append(line.number_persons_yur_short)
            cpfl.append(line.number_persons_fiz_long)
            cpfs.append(line.number_persons_fiz_short)
            ds.append(line.datetime[0:10])
        ds = sorted(list(set(ds)))
        fs = pd.date_range(datetime.strptime(ds[0],'%Y-%m-%d'),
                datetime.strptime(ds[-1],'%Y-%m-%d')).strftime('%Y-%m-%d').tolist()
        weekend = sorted(list(set(fs)-set(ds)))

        context = {
            'dt': dt[::-1], 
            'all_date': ds,
            'weekends': weekend,
        }

        if param == 'opyl':
            context.update({
                'data':opyl[::-1],
                'title':'График «Открытые позиции. Юридические лица (Длинные)» с ',
            })
        elif param == 'opys':
            context.update({
                'data':opys[::-1],
                'title':'График «Открытые позиции. Юридические лица (Короткие)» с ',
            })
        elif param == 'opfl':
            context.update({
                'data':opfl[::-1],
                'title':'График «Открытые позиции. Физические лица (Длинные)» с ',
            })
        elif param == 'opfs':
            context.update({
                'data':opfs[::-1],
                'title':'График «Открытые позиции. Физические лица (Короткие)» с '
            })
        elif param == 'cpyl':
            context.update({
                'data':cpyl[::-1],
                'title':'График «Количество лиц. Юридические лица (Длинные)» с '
            })
        elif param == 'cpys':
            context.update({
                'data':cpys[::-1],
                'title':'График «Количество лиц. Юридические лица (Короткие)» с ',
            })
        elif param == 'cpfl':
            context.update({
                'data':cpfl[::-1],
                'title':'График «Количество лиц. Физические лица (Длинные)» с ',
            })
        elif param == 'cpfs':
            context.update({
                'data':cpfs[::-1],
                'title':'График «Количество лиц. Физические лица (Короткие)» с '
            })
        return context
    else: 
        context = {
            'dt':[],
            'data': [],
            'title':'',
            'all_date': [],
            'weekends': []
        }
        return context  