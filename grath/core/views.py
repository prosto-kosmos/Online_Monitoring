import time
from datetime import datetime
import pandas as pd

from django.shortcuts import render
from django.views import View
from .models import Data

from .build_grath import get_context_grath
from .build_online import get_context_online
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





class Gropyl_view(View):
    def get(self, request):
        context = get_context_grath('opyl')
        return render(request, 'core/grath.html', context=context)

class Gropys_view(View):
    def get(self, request):
        context = get_context_grath('opys')
        return render(request, 'core/grath.html', context=context)

class Gropfl_view(View):
    def get(self, request):
        context = get_context_grath('opfl')
        return render(request, 'core/grath.html', context=context)

class Gropfs_view(View):
    def get(self, request):
        context = get_context_grath('opfs')
        return render(request, 'core/grath.html', context=context)       

class Grcpyl_view(View):
    def get(self, request):
        context = get_context_grath('cpyl')
        return render(request, 'core/grath.html', context=context)

class Grcpys_view(View):
    def get(self, request):
        context = get_context_grath('cpys')
        return render(request, 'core/grath.html', context=context)

class Grcpfl_view(View):
    def get(self, request):
        context = get_context_grath('cpfl')
        return render(request, 'core/grath.html', context=context)

class Grcpfs_view(View):
    def get(self, request):
        context = get_context_grath('cpfs')
        return render(request, 'core/grath.html', context=context) 





class Online_opyl_view(View):
    def get(self, request):
        context = get_context_online('opyl', request) 
        return render(request, 'core/online.html', context)     

class Online_opys_view(View):
    def get(self, request):
        context = get_context_online('opys', request)
        return render(request, 'core/online.html', context) 

class Online_opfl_view(View):
    def get(self, request):
        context = get_context_online('opfl', request)
        return render(request, 'core/online.html', context) 

class Online_opfs_view(View):
    def get(self, request):
        context = get_context_online('opfs', request)
        return render(request, 'core/online.html', context)

class Online_cpyl_view(View):
    def get(self, request):
        context = get_context_online('cpyl', request)
        return render(request, 'core/online.html', context)

class Online_cpys_view(View):
    def get(self, request):
        context = get_context_online('cpys', request)
        return render(request, 'core/online.html', context)

class Online_cpfl_view(View):
    def get(self, request):
        context = get_context_online('cpfl', request)
        return render(request, 'core/online.html', context) 

class Online_cpfs_view(View):
    def get(self, request):
        context = get_context_online('cpfs', request)
        return render(request, 'core/online.html', context) 