# Generated by Django 3.2.16 on 2022-10-24 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('abastecimento', '0002_veiculo'),
    ]

    operations = [
        migrations.AddField(
            model_name='veiculo',
            name='ativo',
            field=models.BooleanField(default=False),
        ),
    ]
