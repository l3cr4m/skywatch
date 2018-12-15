from django.shortcuts import render
from .models import Herec
from filmy.models import HerecFilm
# Create your views here.

def herec(request, slug):
    herec = Herec.objects.get(slug=slug)
    herecfilm = HerecFilm.objects.all()
    return render(request, 'osobnosti/herec.html', {'herec':herec, 'herecfilm':herecfilm})

def herci(request):
    herci = Herec.objects.all()
    return render(request, 'osobnosti/osobnosti.html', {'herci':herci})
