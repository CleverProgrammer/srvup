# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-18 07:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0008_auto_20160618_0600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='category',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='videos.Category'),
            preserve_default=False,
        ),
    ]
