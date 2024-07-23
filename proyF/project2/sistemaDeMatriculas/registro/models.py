from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Curso(models.Model):
    codigo=models.CharField(primary_key=True,max_length=6)
    nombre=models.CharField(max_length=50)
    creditos=models.PositiveSmallIntegerField()
    cupos=models.PositiveSmallIntegerField()

    def __str__(self):
        texto ="{0} ({1})"
        return texto.format(self.nombre, self.creditos)


class CustomUser(AbstractUser):
    es_estudiante=models.BooleanField(default=True)
    es_admin = models.BooleanField(default=False)
    

class Estudiante(models.Model):
    user=models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    codigo = models.CharField(max_length=10)
    nombre = models.CharField(max_length=100)
    cursos = models.ManyToManyField(Curso, blank=True)
    creditos_maximos = models.PositiveSmallIntegerField(default=30)
    creditos_usados = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return f"{self.nombre} ({self.codigo})"
