# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('examinee', '0003_auto_20150905_0218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examinstance',
            name='end_time',
            field=models.DateTimeField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
