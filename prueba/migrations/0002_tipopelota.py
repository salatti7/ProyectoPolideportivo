# Generated by Django 3.1.5 on 2021-01-29 17:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('prueba', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoPelota',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=25)),
                ('tipo_pelota_deporte', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prueba.deporte')),
            ],
        ),
    ]
