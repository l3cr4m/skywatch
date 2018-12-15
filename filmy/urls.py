# coding: utf-8
from django.urls import path, re_path, include
from . import views

app_name = 'filmy'

urlpatterns = [
    path('', views.filmy, name = 'filmy'),
    path('zebricky/nejoblibenejsi', views.nejoblibenejsi, name = 'nejoblibenejsi'),
    path('zebricky/nejneoblibenejsi', views.nejneoblibenejsi, name = 'nejneoblibenejsi'),
    path('zebricky/nejlepsi', views.nejlepsi, name = 'nejlepsi'),
    path('zebricky/nejhorsi', views.nejhorsi, name = 'nejhorsi'),
    re_path('(?P<slug>[\w-]+)', views.film, name = 'film'),
]
