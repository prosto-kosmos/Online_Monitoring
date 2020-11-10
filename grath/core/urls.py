from django.urls import path
from . import views

urlpatterns = [
    path('', views.Main_view.as_view(), name='main_url'),
    path('data/', views.Data_view.as_view(), name='data_url'),
]
