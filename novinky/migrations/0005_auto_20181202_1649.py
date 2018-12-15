# Generated by Django 2.1.3 on 2018-12-02 15:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('novinky', '0004_novinka_thumb'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='novinka',
            name='thumb',
        ),
        migrations.AddField(
            model_name='novinka',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]