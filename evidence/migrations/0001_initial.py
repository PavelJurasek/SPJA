# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('manufacturer', models.CharField(max_length=80)),
                ('model', models.CharField(max_length=50)),
                ('production_year', models.IntegerField(max_length=4)),
                ('consumption', models.FloatField(verbose_name=b'Fuel consumption per 100 km')),
                ('fuel', models.CharField(default=b'Diesel', max_length=20)),
                ('odometer_init', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=120)),
                ('license_since', models.DateField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Refuel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount', models.FloatField()),
                ('price', models.FloatField()),
                ('total_price', models.FloatField()),
                ('odometer', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Ride',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('odometer_start', models.IntegerField()),
                ('odometer_end', models.IntegerField()),
                ('date_start', models.DateField()),
                ('date_end', models.DateField()),
                ('car', models.ForeignKey(to='evidence.Car')),
                ('driver', models.ForeignKey(to='evidence.Driver')),
                ('refuel', models.ForeignKey(blank=True, to='evidence.Refuel', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
