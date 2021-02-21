import time
from datetime import datetime
import pandas as pd
import json

from django.shortcuts import render
from django.views import View
from .models import Data
from django.http import HttpResponse

from .build_grath import get_context_grath
from .build_online import get_context_online
from .build_online import get_new_points
from .build_main import get_context_main
from .actives import actives

class Main_view(View):
    def post(self, request):
        date_begin = request.POST.get('date')
        date_end = datetime.now().date()
        login = request.POST.get('login')
        password = request.POST.get('password')
        active_list = []
        for ac in actives:
            if ac in request.POST.keys():
                active_list.append(ac)
        context = get_context_main(date_begin, date_end, login, password, active_list)
        response = render(request, 'core/main.html', context=context)
        response.set_cookie('login', login)
        response.set_cookie('password', password)
        response.set_cookie('date_begin', date_begin)
        response.set_cookie('active_list', json.dumps(active_list))

        return response

    def get(self, request):
        try:
            login = request.COOKIES["login"]
            password = request.COOKIES["password"]
            date_begin = request.COOKIES["date_begin"]
            active_list = json.loads(request.COOKIES["active_list"])
        except KeyError:
            login = ''
            password = ''
            date_begin = str(datetime.now().date())
            active_list = []
        
        context={
            'login': login, 
            'password': password, 
            'date': date_begin, 
            'message': '',
            'active_list': active_list,
            'actives': actives,
        }
        return render(request, 'core/main.html',context=context)


class Data_view(View):
    def get(self, request):
        all_data = Data.objects.all()
        active_list = list(set(x['code'] for x in list(Data.objects.values('code'))))
        context={
            'data': all_data, 
            'actives': actives,
            'active_list': active_list,
        }
        return render(request, 'core/data.html', context=context)

class GrDataOP_view(View):
    def get(self, request):
        context = get_context_grath('gr_data_op', request.GET.get('active'))
        return render(request, 'core/grath.html', context=context)

class GrDataNP_view(View):
    def get(self, request):
        context = get_context_grath('gr_data_np', request.GET.get('active'))
        return render(request, 'core/grath.html', context=context)

class GrOnlineOP_view(View):
    def get(self, request):
        get_active = request.GET.get('active')
        context = get_context_online('gr_online_op', get_active, request)
        return render(request, 'core/online.html', context=context)

class GrOnlineNP_view(View):
    def get(self, request):
        get_active = request.GET.get('active')
        context = get_context_online('gr_online_np', get_active, request)
        return render(request, 'core/online.html', context=context) 

class GetNewPoints_view(View):
    def post(self, request):
        count_points = int(json.loads(request.POST.get('text')))
        param = request.POST.get('param')
        get_active = request.POST.get('active')
        new_points = get_new_points(count_points, get_active, request, param)
        return HttpResponse(new_points)