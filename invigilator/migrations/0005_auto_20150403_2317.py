# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invigilator', '0004_auto_20150403_2307'),
    ]

    operations = [
        migrations.AddField(
            model_name='invigilator',
            name='city',
            field=models.CharField(default=1, max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='invigilator',
            name='country',
            field=models.CharField(default=2, max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='invigilator',
            name='province',
            field=models.CharField(default=3, max_length=40, blank=True),
            preserve_default=False,
        ),
    ]
