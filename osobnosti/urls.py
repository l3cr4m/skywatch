from django.urls import path, re_path, include
from . import views

app_name = 'osobnosti'

urlpatterns = [
    #path('', views.tvurci, name = 'tvurci'),
    path('herci/', views.herci, name = 'herci'),
    re_path('herci/(?P<slug>[\w-]+)', views.herec, name = 'herec'),
]
