# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-17 04:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0009_auto_20170112_1822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='valida_hasta',
            field=models.DateField(blank=True, default=None, max_length=120, null=True, verbose_name='Válida hasta'),
        ),
    ]
