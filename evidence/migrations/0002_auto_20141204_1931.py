# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('evidence', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ride',
            name='refuel',
        ),
        migrations.AddField(
            model_name='refuel',
            name='ride',
            field=models.ForeignKey(default=1, to='evidence.Ride'),
            preserve_default=False,
        ),
    ]
