# Generated by Django 2.1.3 on 2018-12-02 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('novinky', '0006_novinka_thumb'),
    ]

    operations = [
        migrations.AlterField(
            model_name='novinka',
            name='title',
            field=models.CharField(max_length=300),
        ),
    ]