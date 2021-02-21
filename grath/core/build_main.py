from time import sleep
from .data_processing import get_data_moex, push_data, get_date_list
from .models import Data
from .actives import actives


def get_context_main(date_begin, date_end, login, password, active_list):
    # очищаем таблицу со старыми данными
    Data.objects.all().delete()

    # получаем данные с сайта посуточно
    date_list = get_date_list(date_begin, date_end)
    all_data = list()
    for i in range(len(date_list)):
        try:
            all_data.append(get_data_moex(date_list[i], login, password, active_list))
        except Exception as e:
            print(e)
            return {
                'login': login, 
                'password': password,
                'date': date_begin, 
                'message':'Ошибка загрузки данных с сайта moex.com',
                'active_list': active_list,
                'actives': actives,
            }

    # посуточно заносим данные в БД
    for i in range(len(all_data)):
        data = all_data[i]
        push_data(data)

    context = {
        'login': login, 
        'password': password,
        'date': date_begin, 
        'active_list':active_list,
        'actives': actives,
    }

    if str(date_begin) == str(date_end)[:10]:
        context.update({'message':f'Данные за {date_begin} получены с сайта moex.com и добавлены в базу данных'})
    else:
        context.update({'message':f'Данные с {date_begin} по {str(date_end)[:10]} получены с сайта moex.com и добавлены в базу данных'})
    return context