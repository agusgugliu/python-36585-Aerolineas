# Generated by Django 4.0.4 on 2022-05-29 21:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppAerolineas', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vuelos',
            name='aerolinea_nombre',
        ),
        migrations.RemoveField(
            model_name='vuelos',
            name='vuelo_siglas',
        ),
    ]
