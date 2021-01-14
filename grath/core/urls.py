from django.urls import path
from . import views

urlpatterns = [
    path('', views.Main_view.as_view(), name='main_url'),
    path('data/', views.Data_view.as_view(), name='data_url'),
    
    path('gropyl/', views.Gropyl_view.as_view(), name='gropyl'),
    path('gropys/', views.Gropys_view.as_view(), name='gropys'),
    path('gropfl/', views.Gropfl_view.as_view(), name='gropfl'),
    path('gropfs/', views.Gropfs_view.as_view(), name='gropfs'),

    path('grcpyl/', views.Grcpyl_view.as_view(), name='grcpyl'),
    path('grcpys/', views.Grcpys_view.as_view(), name='grcpys'),
    path('grcpfl/', views.Grcpfl_view.as_view(), name='grcpfl'),
    path('grcpfs/', views.Grcpfs_view.as_view(), name='grcpfs'),

    path('online_opyl/', views.Online_opyl_view.as_view(), name='online_opyl'),
    path('online_opys/', views.Online_opys_view.as_view(), name='online_opys'),
    path('online_opfl/', views.Online_opfl_view.as_view(), name='online_opfl'),
    path('online_opfs/', views.Online_opfs_view.as_view(), name='online_opfs'),

    path('online_cpyl/', views.Online_cpyl_view.as_view(), name='online_cpyl'),
    path('online_cpys/', views.Online_cpys_view.as_view(), name='online_cpys'),
    path('online_cpfl/', views.Online_cpfl_view.as_view(), name='online_cpfl'),
    path('online_cpfs/', views.Online_cpfs_view.as_view(), name='online_cpfs'),
]
