# Generated by Django 3.0.7 on 2020-06-16 11:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('loja', '0002_auto_20200616_0850'),
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemCompra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_de_adicionamento', models.DateTimeField(auto_now=True)),
                ('data_de_compra', models.DateTimeField(null=True)),
                ('tamanho', models.CharField(max_length=2)),
                ('quantidade', models.IntegerField()),
                ('produto', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='loja.Produto')),
            ],
        ),
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_de_referencia', models.CharField(max_length=15)),
                ('finalizada', models.BooleanField(default=False)),
                ('data_de_compra', models.DateTimeField(auto_now=True)),
                ('comprador', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='clientes.Cliente')),
                ('itens', models.ManyToManyField(to='carrinho.ItemCompra')),
            ],
        ),
    ]
