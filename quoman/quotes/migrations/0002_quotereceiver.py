# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-03 16:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuoteReceiver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(blank=True, max_length=64, verbose_name='Nombres')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('quote', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quotes.Quote', verbose_name='')),
            ],
            options={
                'verbose_name_plural': 'Destinatarios de la cotización',
                'verbose_name': 'Destinatario de la cotización',
            },
        ),
    ]
