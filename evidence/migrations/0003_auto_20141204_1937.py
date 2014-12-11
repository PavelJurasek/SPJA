# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('evidence', '0002_auto_20141204_1931'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ride',
            old_name='odometer_end',
            new_name='final',
        ),
        migrations.RenameField(
            model_name='ride',
            old_name='odometer_start',
            new_name='initial',
        ),
    ]
