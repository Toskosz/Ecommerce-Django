# Generated by Django 3.0.7 on 2020-07-23 11:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('transacao', '0006_transacao_transacao_id'),
        ('carrinho', '0009_auto_20200702_0809'),
    ]

    operations = [
        migrations.AddField(
            model_name='compra',
            name='transacao',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='transacao.Transacao'),
        ),
    ]
