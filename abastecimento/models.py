from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models
from datetime import datetime

class Veiculos(models.Model):
    nome_veiculo = models.CharField(max_length=200)
    placa = models.CharField(max_length=200)
    marca = models.CharField(max_length=200)
    modelo = models.CharField(max_length=200)
    chassi= models.CharField(max_length=200)
    renavam = models.CharField(max_length=200)
    tipo = models.CharField(max_length=200)
    ano = models.CharField(max_length=200)
    cor = models.CharField(max_length=200)
    setor = models.CharField(max_length=200)   
    data_criacao = models.DateTimeField(default = datetime.now, blank = True)
    
   

class Veiculo(models.Model):
    nome_veiculo = models.CharField(max_length=200)
    placa = models.CharField(max_length=200)
    marca = models.CharField(max_length=200)
    modelo = models.CharField(max_length=200)
    chassi= models.CharField(max_length=200)
    renavam = models.CharField(max_length=200)
    tipo = models.CharField(max_length=200)
    ano = models.CharField(max_length=200)
    cor = models.CharField(max_length=200)
    setor = models.CharField(max_length=200)   
    data_criacao = models.DateTimeField(default = datetime.now, blank = True)
    ativo = models.BooleanField(default=False)
    foto = models.ImageField(upload_to = 'fotos/%d/%m/%Y/', blank = True)