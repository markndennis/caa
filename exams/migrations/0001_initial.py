# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('exam_type', models.CharField(max_length=40)),
                ('sub_test', models.CharField(max_length=2)),
                ('exam_ques', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ExamType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('exam_type', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('qnum', models.IntegerField()),
                ('qtext', models.CharField(max_length=1024)),
                ('r1', models.CharField(max_length=256)),
                ('r2', models.CharField(max_length=256)),
                ('r3', models.CharField(max_length=256)),
                ('r4', models.CharField(max_length=256)),
                ('qtext_c', models.CharField(max_length=1024)),
                ('r1_c', models.CharField(max_length=256)),
                ('r2_c', models.CharField(max_length=256)),
                ('r3_c', models.CharField(max_length=256)),
                ('r4_c', models.CharField(max_length=256)),
                ('difficulty', models.CharField(max_length=10)),
                ('active', models.BooleanField(default=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('solution', models.CharField(max_length=2)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
