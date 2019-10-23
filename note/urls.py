from django.urls import path
from . import views
app_name = 'note'

urlpatterns = [
    path('', views.index, name='index'),
    path('ww/', views.ww, name='ww'),
    path('ww2/', views.ww2, name='ww2'),
    path('init_ww/', views.init_ww, name='init_ww'),
    path('work/', views.work, name='work'),
    path('work2/', views.work2, name='work2'),
    path('work3/', views.work3, name='work3'),
]