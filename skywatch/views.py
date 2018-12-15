# coding: utf-8
from django.shortcuts import render
from filmy.models import Film
from osobnosti.models import Herec
from novinky.models import Novinka


def homepage(request):
    filmy = Film.objects.all()
    herec = Herec.objects.get(id=3)
    novinky = Novinka.objects.all()

    return render(request, 'homepage.html',{'filmy':filmy,'herec':herec, 'novinky':novinky})
