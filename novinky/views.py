# coding: utf-8
from django.shortcuts import render
from .models import Novinka
from django.core.paginator import Paginator

# Create your views here.

def novinky(request):
    novinky = Novinka.objects.all().order_by('date')

    paginator = Paginator(novinky, 6)

    page = request.GET.get('page')

    novinky = paginator.get_page(page)

    return render(request, 'novinky/novinky.html', {'novinky':novinky})
