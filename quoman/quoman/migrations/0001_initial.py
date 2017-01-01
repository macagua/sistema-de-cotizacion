# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-01 21:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Config',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(blank=True, null=True, upload_to='config', verbose_name='Logo de la empresa')),
                ('ruc', models.CharField(blank=True, max_length=12, verbose_name='RUC')),
                ('direccion', models.CharField(blank=True, max_length=120, verbose_name='Dirección')),
                ('igv', models.DecimalField(decimal_places=1, default=18, max_digits=3, verbose_name='IGB')),
                ('detraccion_texto', models.TextField(blank=True, verbose_name='Texto en caso de detracción')),
            ],
            options={
                'verbose_name': 'Configuración',
                'verbose_name_plural': 'Configuración',
            },
        ),
    ]