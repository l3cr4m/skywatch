# Generated by Django 2.1.3 on 2018-12-08 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('osobnosti', '0006_remove_herec_jmeno'),
    ]

    operations = [
        migrations.AlterField(
            model_name='herec',
            name='slug',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='herec',
            name='title',
            field=models.CharField(blank=True, max_length=100, unique=True),
        ),
    ]
