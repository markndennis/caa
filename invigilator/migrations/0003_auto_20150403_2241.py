# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invigilator', '0002_auto_20150402_1542'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='institution',
            name='details',
        ),
        migrations.AddField(
            model_name='invigilator',
            name='details',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
