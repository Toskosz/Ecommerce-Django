# Generated by Django 3.0.7 on 2020-07-16 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transacao', '0003_auto_20200716_0934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transacao',
            name='complemento',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
