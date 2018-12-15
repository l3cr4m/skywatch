# coding: utf-8
from django.contrib import admin
from .models import Film
from .models import Recenze
from .models import HerecFilm

# Register your models here.
admin.site.register(Film)
admin.site.register(Recenze)
admin.site.register(HerecFilm)
