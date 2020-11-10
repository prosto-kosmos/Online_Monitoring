from time import sleep
from celery.contrib.abortable import AbortableTask
from .get_all_data import get_data_moex, push_data, get_date_list
from .models import Data
from celery import shared_task
from celery_progress.backend import ProgressRecorder

from grath.celery import app


@app.task(bind=True, base=AbortableTask)
def get_data_celery(self, date_begin, date_end, login, password, active):
    # очищаем таблицу со старыми данными
    Data.objects.all().delete()
    progress_recoder = ProgressRecorder(self)
    date_list = get_date_list(date_begin, date_end)

    all_data = list()
    for i in range(len(date_list)):
        if self.is_aborted():
            return 'Задача была прервана пользователем'
        # получаем данные за конкретную дату и добавляем в список
        all_data.append(get_data_moex(date_list[i], active, login, password))
        message = f'Идет процесс получения данных с moex.com за {date_list[i]}. ' \
                  f'Повторный запрос данных до завершения всех операций нежелателен!'
        progress_recoder.set_progress(i + 1, len(date_list), message)

    count = 0
    count_all = 0
    for i in all_data:
        count_all += len(i[0]) / 2

    for i in range(len(all_data)):
        if self.is_aborted():
            return 'Задача была прервана пользователем'
        # заполняем таблицу новыми данными
        data = all_data[i][0]
        dop_data = all_data[i][1]
        count = push_data(data, dop_data, count, count_all, progress_recoder)
    if str(date_begin) == str(date_end[:10]):
        return f'Данные за {date_begin} получены с сайта moex.com и добавлены в базу данных'
    else:
        return f'Данные с {date_begin} по {date_end[:10]} получены с сайта moex.com и добавлены в базу данных'

# @shared_task(bind=True)
# def go_to_sleep(self, duration):
#     progress_recoder = ProgressRecorder(self)
#     for i in range(5):
#         sleep(duration)
#         progress_recoder.set_progress(i + 1, 5, f'On iteration {i}')
#     return 'Done'
