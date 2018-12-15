# coding: utf-8
from django.db import models
from osobnosti.models import Herec

# Create your models here.

#class filmy(model.Models):
class Film(models.Model):
    title = models.CharField(max_length=100, blank=True, unique=True)
    slug = models.CharField(max_length=100, blank=True)

    poster = models.ImageField(default='poster.jpg', blank=True)
    hodnoceni = models.BigIntegerField(default=0)
    hodnoceno = models.BigIntegerField(default=0)

    zanr = models.CharField(max_length=300,blank=True)

    zeme = models.CharField(max_length=300,blank=True)
    rok = models.BigIntegerField(default=0)
    delka = models.BigIntegerField(default=0)

    rezije = models.CharField(max_length=300,blank=True)
    scenar = models.CharField(max_length=300,blank=True)


    obsah = models.TextField(blank=True)

    def __str__(self):
        return self.title

class Recenze(models.Model):
    jmeno = models.CharField(max_length=300)
    recenz = models.TextField()

    film = models.ForeignKey(Film, on_delete=models.PROTECT)

    def __str__(self):
        return self.jmeno

class HerecFilm(models.Model):
    film = models.ForeignKey(Film, on_delete=models.PROTECT)
    herec = models.ForeignKey(Herec, on_delete=models.PROTECT)

    def __str__(self):
        return self.film.title
