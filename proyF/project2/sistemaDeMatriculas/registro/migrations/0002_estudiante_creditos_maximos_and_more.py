# Generated by Django 5.0.7 on 2024-07-21 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='estudiante',
            name='creditos_maximos',
            field=models.PositiveSmallIntegerField(default=30),
        ),
        migrations.AddField(
            model_name='estudiante',
            name='creditos_usados',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]