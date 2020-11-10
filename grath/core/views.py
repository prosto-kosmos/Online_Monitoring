import time
from datetime import datetime

from celery.contrib.abortable import AbortableAsyncResult

from django.shortcuts import render
from django.views import View
from .models import Data
from .tasks import get_data_celery
from grath.celery import get_inspect, revoke_task

login = ''
password = ''
active = ''
date_begin = str(datetime.now().date())
task_id = None


class Main_view(View):
    def post(self, request):
        global date_begin, login, password, active
        date_begin = request.POST.get('date')
        date_end = datetime.now().date()
        login = request.POST.get('login')
        password = request.POST.get('password')
        active = request.POST.get('active')

        for desktop in get_inspect().active().values():
            for task in desktop:
                del_task = AbortableAsyncResult(task['id'])
                while not str(del_task.status) == 'SUCCESS':
                    del_task.abort()
                    time.sleep(1)

        task = get_data_celery.delay(date_begin, date_end, login, password, active)

        global task_id
        task_id = task.task_id

        return render(request, 'core/main.html',
                      context={'login': login, 'password': password, 'date': date_begin, 'active': active,
                               'task_id': task_id})

    def get(self, request):
        global date_begin, login, password, active
        return render(request, 'core/main.html',
                      context={'login': login, 'password': password, 'date': date_begin, 'active': active,
                               'task_id': task_id})


class Data_view(View):
    def get(self, request):
        all_data = Data.objects.all()
        return render(request, 'core/data.html', context={'data': all_data})
