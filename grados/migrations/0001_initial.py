# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-10-04 02:52
from __future__ import unicode_literals

import colorfield.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Escalafon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255, verbose_name='Nombre')),
            ],
            options={
                'verbose_name_plural': 'Escalafones',
                'verbose_name': 'Escalafón',
            },
        ),
        migrations.CreateModel(
            name='Grado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255, verbose_name='Nombre')),
                ('excepcion', models.BooleanField(default=False, verbose_name='Posee más de un grado superior')),
                ('escalafon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grados.Escalafon', verbose_name='Escalafón')),
                ('grado_superior', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='grados.Grado', verbose_name='Grado Superior')),
            ],
            options={
                'verbose_name_plural': 'Grados',
                'verbose_name': 'Grado',
            },
        ),
        migrations.CreateModel(
            name='Rango',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255, verbose_name='Nombre')),
                ('color', colorfield.fields.ColorField(default='#FF0000', max_length=10)),
            ],
            options={
                'verbose_name_plural': 'Rangos',
                'verbose_name': 'Rango',
            },
        ),
        migrations.AddField(
            model_name='escalafon',
            name='rango',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grados.Rango', verbose_name='Rango'),
        ),
    ]
