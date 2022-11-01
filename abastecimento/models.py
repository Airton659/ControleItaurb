from email.policy import default
from random import choices
from unittest.util import _MAX_LENGTH
from django.db import models
from django.urls import reverse
from datetime import datetime
from django.contrib.auth.models import User

 

class Veiculo(models.Model):
    nome_veiculo = models.CharField(max_length=200)
    placa = models.CharField(max_length=200)
    marca = models.CharField(max_length=200)
    modelo = models.CharField(max_length=200)
    # chassi= models.CharField(max_length=200)
    # renavam = models.CharField(max_length=200)
    tipo = models.CharField(max_length=200)
    ano = models.CharField(max_length=200)
    cor = models.CharField(max_length=200)
    setor = models.CharField(max_length=200)   
    data_criacao = models.DateTimeField(default = datetime.now, blank = True)
    ativo = models.BooleanField(default=False)
    foto = models.ImageField(upload_to = 'fotos/%d/%m/%Y/', blank = True)
    def __str__(self):
        return self.placa



class Abastecimento(models.Model):
    placa = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
    data_registro = models.DateTimeField(default = datetime.now, blank = False)    
    km = models.CharField(max_length=200)
    litros = models.CharField(max_length=200)
    valor = models.CharField(max_length=200)
    posto = models.CharField(max_length=200)
    motorista = models.CharField(max_length=200)
    combustivel = models.CharField(max_length=200)
    data_abastecimento = models.DateField(default = datetime.now, blank = False)  
    usuario_de_criacao = models.ForeignKey(User, on_delete=models.CASCADE)

class Manutencao(models.Model):    
    placa = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
    data_manutencao= models.DateField(default = datetime.now, blank = False)
    km = models.FloatField()
    itens = models.TextField()
    usuario_de_criacao = models.ForeignKey(User, on_delete=models.CASCADE)
    data_registro = models.DateTimeField(default = datetime.now, blank = False)  




    
