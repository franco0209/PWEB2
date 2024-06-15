from django.db import models

# Create your models here.

class Simple(models.Model):
    text=models.CharField(max_length=10)
    number=models.IntegerField(null=True)
    url=models.URLField(default="www.example.com")

    def __str__(self):
        return self.url


class NullExample(models.Model):
    col=models.CharField(max_length=10,blank=True, null=True)

class Language(models.Model):
    name=models.CharField(max_length=10)

    def _str_(self):
        return self.name

class Framework(models.Model):
    name=models.CharField(max_length=10)
    language=models.ForeignKey(Language, on_delete=models.CASCADE)
       
    def _str_(self):
        return self.name

class Movie(models.Model):
    name=models.CharField(max_length=10)
    def __str__(self):
        return self.name
    
class Character(models.Model):
    name=models.CharField(max_length=10)
    movies= models.ManyToManyField(Movie)

    def __str__(self):
        return self.name    
     