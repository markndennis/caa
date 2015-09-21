# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0002_auto_20150525_1925'),
    ]

    operations = [
        migrations.AddField(
            model_name='questions',
            name='examtype',
            field=models.CharField(default=datetime.datetime(2015, 8, 30, 16, 22, 30, 806842, tzinfo=utc), max_length=2),
            preserve_default=False,
        ),
    ]
