# Generated by Django 3.0.7 on 2020-07-02 11:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0003_auto_20200630_0850'),
        ('carrinho', '0008_auto_20200702_0805'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itemcompra',
            name='finalizado',
        ),
        migrations.AddField(
            model_name='itemcompra',
            name='cliente',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='clientes.Cliente'),
        ),
    ]
