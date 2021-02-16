from django.urls import path
from . import views

urlpatterns = [
    path('', views.Main_view.as_view(), name='main_url'),
    path('data/', views.Data_view.as_view(), name='data_url'),

    path('gr_data_op_pos/', views.GrDataOP_view.as_view(), name='gr_data_op'),
    path('gr_data_num_per/', views.GrDataNP_view.as_view(), name='gr_data_np'),
    path('gr_online_op_pos/', views.GrOnlineOP_view.as_view(), name='gr_online_op'),
    path('gr_online_num_per/', views.GrOnlineNP_view.as_view(), name='gr_online_np'),
    path('get_new_points_ajax/', views.GetNewPoints_view.as_view(), name='get_new_points'),
]
