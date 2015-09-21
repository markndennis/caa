# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('examinee', '0002_auto_20150602_1352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examinstance',
            name='elapsed_time',
            field=models.DateTimeField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
