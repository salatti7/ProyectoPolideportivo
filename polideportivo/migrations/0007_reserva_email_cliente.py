# Generated by Django 3.1.5 on 2021-05-31 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polideportivo', '0006_auto_20210531_1734'),
    ]

    operations = [
        migrations.AddField(
            model_name='reserva',
            name='email_cliente',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
