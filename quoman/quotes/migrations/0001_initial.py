# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-02 14:36
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_de_creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('estado', models.CharField(blank=True, choices=[('PENDIENTE', 'PENDIENTE'), ('APROBADA', 'APROBADA'), ('DENEGADA', 'DENEGADA'), ('CANCELADA', 'CANCELADA')], default='PENDIENTE', max_length=24, verbose_name='Estado')),
                ('codigo', models.CharField(max_length=12, verbose_name='Código')),
                ('ruc', models.CharField(blank=True, max_length=12, verbose_name='RUC')),
                ('representante', models.CharField(blank=True, max_length=96, verbose_name='Representante')),
                ('tiempo_de_entrega', models.CharField(blank=True, max_length=96, verbose_name='Tiempo de Entrega')),
                ('valida_hasta', models.DateTimeField(blank=True, null=True, verbose_name='Válida hasta')),
                ('forma_de_pago', models.TextField(max_length=120, verbose_name='Forma de pago')),
                ('costo_de_envio', models.DecimalField(decimal_places=2, default=0, max_digits=6, verbose_name='Costo de envío')),
                ('propietario_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Propietario')),
            ],
            options={
                'verbose_name_plural': 'Cotizaciones',
                'verbose_name': 'Cotización',
                'ordering': ['fecha_de_creacion'],
            },
        ),
    ]
