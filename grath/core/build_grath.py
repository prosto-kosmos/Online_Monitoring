import requests
import json
import pandas as pd
from datetime import datetime
from .models import Data
from .actives import actives

def get_context_grath(param, active):
    all_data = Data.objects.all()
    active_list = list(set(x['code'] for x in list(Data.objects.values('code'))))
    dt, ds = [],[],
    opyl, opys, opfl, opfs = [],[],[],[]
    cpyl, cpys, cpfl, cpfs = [],[],[],[]
    if len(all_data) > 0:
        for line in all_data:
            if line.code == active:
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
            'actives': actives,
            'active_list':active_list,
        }

        if param == 'gr_data_op':
            context.update({
                'data_1':opyl[::-1],
                'data_2':opys[::-1],
                'data_3':opfl[::-1],
                'data_4':opfs[::-1],
                'main_title':f'Открытые позиции. Актив «{active}»',
            })
        elif param == 'gr_data_np':
            context.update({
                'data_1':cpyl[::-1],
                'data_2':cpys[::-1],
                'data_3':cpfl[::-1],
                'data_4':cpfs[::-1],
                'main_title':f'Количество лиц. Актив «{active}»',
            })
        return context
    else: 
        context = {
            'dt':[],
            'data_1': [],
            'data_2': [],
            'data_3': [],
            'data_4': [],
            'title_1':'',
            'title_2':'',
            'title_3':'',
            'title_4':'',
            'all_date': [],
            'weekends': [],
            'actives': actives,
            'active_list':active_list,
        }
        return context  