# Generated by Django 3.2.16 on 2022-10-26 08:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('abastecimento', '0004_veiculo_foto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Abastecimento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_abastecimento', models.DateTimeField(default=datetime.datetime.now)),
                ('km', models.FloatField()),
                ('litros', models.FloatField()),
                ('valor', models.FloatField()),
                ('posto', models.CharField(max_length=200)),
                ('motorista', models.CharField(max_length=200)),
                ('combustivel', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Manutencao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField(default=datetime.datetime.now)),
                ('km', models.FloatField()),
                ('itens', models.BigIntegerField()),
            ],
        ),
    ]
