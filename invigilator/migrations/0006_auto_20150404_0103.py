# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invigilator', '0005_auto_20150403_2317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invigilator',
            name='details',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
    ]
