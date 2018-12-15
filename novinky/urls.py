# coding: utf-8
from django.urls import path, include
from . import views

app_name = 'novinky'

urlpatterns = [

    path('', views.novinky, name='novinky'),
]
