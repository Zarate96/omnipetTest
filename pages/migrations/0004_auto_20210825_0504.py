# Generated by Django 3.0.7 on 2021-08-25 05:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_remove_distancias_categoria'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ciudades',
            options={'verbose_name_plural': 'Ciudades'},
        ),
        migrations.AlterModelOptions(
            name='distancias',
            options={'verbose_name_plural': 'Distancias'},
        ),
        migrations.AlterModelOptions(
            name='zonas',
            options={'verbose_name_plural': 'Zonas'},
        ),
    ]
