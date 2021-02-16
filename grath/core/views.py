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


login = ''
password = ''
active = ''
date_begin = str(datetime.now().date())

class Main_view(View):
    def post(self, request):
        global date_begin, login, password, active
        date_begin = request.POST.get('date')
        date_end = datetime.now().date()
        login = request.POST.get('login')
        password = request.POST.get('password')
        active = request.POST.get('active')

        context = get_context_main(date_begin, date_end, login, password, active)

        response = render(request, 'core/main.html', context=context)
        response.set_cookie('login', login)
        response.set_cookie('password', password)
        response.set_cookie('active', active)

        return response

    def get(self, request):
        global date_begin, login, password, active
        context={
            'login': login, 
            'password': password, 
            'date': date_begin, 
            'active': active,
            'message': '',
        }
        return render(request, 'core/main.html',context=context)


class Data_view(View):
    def get(self, request):
        all_data = Data.objects.all()
        return render(request, 'core/data.html', context={'data': all_data})





class GrDataOP_view(View):
    def get(self, request):
        context = get_context_grath('gr_data_op')
        return render(request, 'core/grath.html', context=context)

class GrDataNP_view(View):
    def get(self, request):
        context = get_context_grath('gr_data_np')
        return render(request, 'core/grath.html', context=context)

class GrOnlineOP_view(View):
    def get(self, request):
        context = get_context_online('gr_online_op', request)
        return render(request, 'core/online.html', context=context)

class GrOnlineNP_view(View):
    def get(self, request):
        context = get_context_online('gr_online_np', request)
        return render(request, 'core/online.html', context=context) 

class GetNewPoints_view(View):
    def post(self, request):
        count_points = int(json.loads(request.POST.get('text')))
        param = request.POST.get('param')
        new_points = get_new_points(count_points, request, param)
        return HttpResponse(new_points)