from xml.parsers.expat import model
from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length= 200)
    email = models.CharField(max_length= 200)
    chapa = models.IntegerField()
    setor = models.CharField(max_length= 200)
