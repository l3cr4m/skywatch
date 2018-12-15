from django.db import models

# Create your models here.

class Herec(models.Model):
    title = models.CharField(max_length=100, blank=True, unique=True)
    slug = models.CharField(max_length=100, blank=True)

    fotografie = models.ImageField(default='DiCaprio.png', blank=True)
    narozeniny = models.DateField(blank=True)
    misto_narozeni = models.CharField(max_length=300,blank=True)

    ziv = models.TextField(blank=True)

    def __str__(self):
        return self.title

    def po(self):
        return self.ziv[:950]
