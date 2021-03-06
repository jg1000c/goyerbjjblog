# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-09 17:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20180108_2051'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='technique_sub_type',
            field=models.CharField(default='de la riva', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='technique_type',
            field=models.CharField(default='guard', max_length=50),
            preserve_default=False,
        ),
    ]
