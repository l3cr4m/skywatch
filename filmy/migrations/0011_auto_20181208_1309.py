# Generated by Django 2.1.3 on 2018-12-08 12:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('osobnosti', '0006_remove_herec_jmeno'),
        ('filmy', '0010_film_hraji'),
    ]

    operations = [
        migrations.CreateModel(
            name='HerecAutor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='film',
            name='hraji',
        ),
        migrations.AddField(
            model_name='herecautor',
            name='film',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='filmy.Film'),
        ),
        migrations.AddField(
            model_name='herecautor',
            name='herec',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='osobnosti.Herec'),
        ),
    ]
