# coding: utf-8
from django.db import models
from django.utils import timezone


# Create your models here.
class Novinka(models.Model):
    title = models.CharField(max_length=300)
    body = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    thumb = models.ImageField(default='default.jpg', blank=True)

    def __str__(self):
        return self.title

    def od(self):
        return self.body[400:]

    def do(self):
        return self.body[:400]
