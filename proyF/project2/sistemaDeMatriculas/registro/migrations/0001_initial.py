# Generated by Django 5.0.7 on 2024-07-21 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('codigo', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('creditos', models.PositiveSmallIntegerField()),
                ('cupos', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('codigo', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('cursos', models.ManyToManyField(blank=True, to='registro.curso')),
            ],
        ),
    ]