# coding: utf-8
from django.shortcuts import render
from .models import Film, Recenze, HerecFilm
from django.core.paginator import Paginator
from .filters import FilmFilter

# Create your views here.
def filmy(request):
    filmy = Film.objects.all()
    filter = FilmFilter(request.GET, queryset=filmy)

    paginator = Paginator(filter.qs, 24)
    page = request.GET.get('page')
    filmy = paginator.get_page(page)
    filter__content = request.GET['title__icontains']


    return render(request, 'filmy/filmy.html', {'filmy':filmy, 'filter':filter, 'filter__content': filter__content})


def film(request, slug):
    film = Film.objects.get(slug=slug)
    recenze = Recenze.objects.all()
    herecfilm = HerecFilm.objects.all()

    paginator = Paginator(recenze, 10)
    page = request.GET.get('page')
    recenze = paginator.get_page(page)

    return render(request, 'filmy/film.html', {'film':film, 'recenze':recenze, 'herecfilm':herecfilm})


def nejoblibenejsi(request):
    filmy = Film.objects.all().order_by('-hodnoceno')
    return render(request, 'filmy/zebricky.html', {'filmy':filmy})

def nejneoblibenejsi(request):
    filmy = Film.objects.all().order_by('hodnoceno')
    return render(request, 'filmy/zebricky.html', {'filmy':filmy})

def nejlepsi(request):
    filmy = Film.objects.all().order_by('-hodnoceni')
    return render(request, 'filmy/zebricky.html', {'filmy':filmy})

def nejhorsi(request):
    filmy = Film.objects.all().order_by('hodnoceni')
    return render(request, 'filmy/zebricky.html', {'filmy':filmy})
