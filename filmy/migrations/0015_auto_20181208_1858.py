# Generated by Django 2.1.3 on 2018-12-08 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmy', '0014_auto_20181208_1856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='title',
            field=models.CharField(blank=True, max_length=100, unique=True),
        ),
    ]
