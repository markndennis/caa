# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0002_auto_20150525_1925'),
        ('invigilator', '0006_auto_20150404_0103'),
    ]

    operations = [
        migrations.CreateModel(
            name='Examinee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=40)),
                ('last_name', models.CharField(max_length=40)),
                ('regnum', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=75)),
                ('dob', models.DateField(blank=True)),
                ('intended', models.DateField(blank=True)),
                ('approved', models.BooleanField(default=False)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('exam_type', models.ForeignKey(to='exams.ExamType')),
                ('invigilator', models.ForeignKey(to='invigilator.Invigilator')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ExamInstance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start_time', models.DateTimeField(blank=True)),
                ('elapsed_time', models.DateTimeField(blank=True)),
                ('end_time', models.DateTimeField(blank=True)),
                ('ques_sequence', models.CharField(max_length=100)),
                ('examinee', models.ForeignKey(to='examinee.Examinee')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ExamResults',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ques_number', models.IntegerField()),
                ('ques_response', models.CharField(max_length=2)),
                ('examinee', models.ForeignKey(to='examinee.ExamInstance')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
