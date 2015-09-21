# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('examinee', '0005_auto_20150905_0252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examresults',
            name='ques_response',
            field=models.CharField(max_length=2, null=True),
            preserve_default=True,
        ),
    ]
