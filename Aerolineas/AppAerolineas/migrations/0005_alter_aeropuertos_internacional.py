# Generated by Django 4.0.4 on 2022-05-31 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppAerolineas', '0004_alter_vuelos_vuelo_numero'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aeropuertos',
            name='internacional',
            field=models.CharField(max_length=5),
        ),
    ]
