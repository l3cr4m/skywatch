import django_filters
from django import forms
from .models import Film
from .models import HerecFilm
from distutils.util import strtobool
from multiselectfield import MultiSelectField

BOOLEAN_CHOICES = (('false', 'False'), ('true', 'True'),)

class FilmFilter(django_filters.FilterSet):
    #name = django_filters.CharFilter(field_name='title', lookup_expr='iexatic')
    #my_field = MultiSelectField(choices=BOOLEAN_CHOICES)
    #uncategorized = django_filters.ModelMultipleChoiceFilter(queryset=Film.objects.all(),
    #    widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Film
        fields = {
            'title':  ['icontains']
        }
