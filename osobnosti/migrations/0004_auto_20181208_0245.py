# Generated by Django 2.1.3 on 2018-12-08 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('osobnosti', '0003_auto_20181208_0238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='herec',
            name='narozeniny',
            field=models.DateTimeField(blank=True),
        ),
    ]
