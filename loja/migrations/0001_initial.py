# Generated by Django 3.0.7 on 2020-06-10 13:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_produto', models.CharField(max_length=200)),
                ('descricao', models.TextField()),
                ('categoria', models.CharField(max_length=100)),
                ('date_produto', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('publicado', models.BooleanField(default=False)),
                ('foto_produto', models.ImageField(blank=True, upload_to='fotos/%d/%m/%Y/')),
                ('preco', models.IntegerField()),
                ('disponibilidade', models.BooleanField(default=True)),
                ('tamanho_pequeno', models.IntegerField()),
                ('tamanho_medio', models.IntegerField()),
                ('tamanho_grande', models.IntegerField()),
            ],
        ),
    ]
