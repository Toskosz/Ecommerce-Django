# Generated by Django 3.0.7 on 2020-07-16 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0004_auto_20200716_0828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='nome',
            field=models.CharField(default=None, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='sobrenome',
            field=models.CharField(default=None, max_length=200, null=True),
        ),
    ]
