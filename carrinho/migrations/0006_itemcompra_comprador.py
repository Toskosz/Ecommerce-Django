# Generated by Django 3.0.7 on 2020-07-01 12:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0003_auto_20200630_0850'),
        ('carrinho', '0005_auto_20200701_0828'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemcompra',
            name='comprador',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='clientes.Cliente'),
        ),
    ]
