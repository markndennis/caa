# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='exam_type',
            field=models.ForeignKey(to='exams.ExamType'),
            preserve_default=True,
        ),
    ]
