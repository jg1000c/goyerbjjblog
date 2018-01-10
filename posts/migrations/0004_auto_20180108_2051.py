# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-08 20:51
from __future__ import unicode_literals

from django.db import migrations
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20180108_2048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='video',
            field=embed_video.fields.EmbedVideoField(blank=True, help_text='This is a help text', verbose_name='My video'),
        ),
    ]
