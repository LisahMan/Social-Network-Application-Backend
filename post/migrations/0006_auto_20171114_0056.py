# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-11-13 19:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0005_auto_20171110_2246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
    ]
