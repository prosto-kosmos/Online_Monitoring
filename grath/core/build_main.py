from time import sleep
from .get_all_data import get_data_moex, push_data, get_date_list
from .models import Data


def get_context_main(date_begin, date_end, login, password, active):
    # очищаем таблицу со старыми данными
    Data.objects.all().delete()

    date_list = get_date_list(date_begin, date_end)

    all_data = list()
    for i in range(len(date_list)):
        try:
            all_data.append(get_data_moex(date_list[i], active, login, password))
        except Exception:
            return {
                'login': login, 
                'password': password,
                'date': date_begin, 
                'active': active,
                'message':'Ошибка загрузки данных с сайта moex.com',
            }


    for i in range(len(all_data)):
        data = all_data[i][0]
        dop_data = all_data[i][1]
        push_data(data, dop_data)

    context = {
        'login': login, 
        'password': password,
        'date': date_begin, 
        'active': active,
    }

    if str(date_begin) == str(date_end)[:10]:
        context.update({'message':f'Данные за {date_begin} получены с сайта moex.com и добавлены в базу данных'})
    else:
        context.update({'message':f'Данные с {date_begin} по {str(date_end)[:10]} получены с сайта moex.com и добавлены в базу данных'})
    return context