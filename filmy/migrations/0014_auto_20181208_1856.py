# Generated by Django 2.1.3 on 2018-12-08 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmy', '0013_film_hodnoceno'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='slug',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='film',
            name='title',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
