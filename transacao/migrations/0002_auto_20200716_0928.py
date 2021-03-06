# Generated by Django 3.0.7 on 2020-07-16 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transacao', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transacao',
            name='bairro',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='transacao',
            name='cidade',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='transacao',
            name='complemento',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='transacao',
            name='endereco',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='transacao',
            name='estado',
            field=models.CharField(choices=[('DF', 'DF'), ('RJ', 'RJ'), ('SP', 'SP')], default=0, max_length=3),
        ),
        migrations.AlterField(
            model_name='transacao',
            name='nomeCartao',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='transacao',
            name='pais',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='transacao',
            name='validadeCartao',
            field=models.CharField(max_length=10),
        ),
    ]
