# Generated by Django 3.2.16 on 2022-10-27 15:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('abastecimento', '0009_abastecimento_manutencao'),
    ]

    operations = [
        migrations.RenameField(
            model_name='manutencao',
            old_name='data',
            new_name='data_manutencao',
        ),
        migrations.AddField(
            model_name='abastecimento',
            name='data_registro',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='manutencao',
            name='data_registro',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
