# Generated by Django 2.1.3 on 2018-12-07 23:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('filmy', '0005_auto_20181208_0013'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recenze',
            name='film',
        ),
        migrations.DeleteModel(
            name='Recenze',
        ),
    ]