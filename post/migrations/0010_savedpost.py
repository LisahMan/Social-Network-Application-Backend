# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-11-21 16:06
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('post', '0009_auto_20171114_0112'),
    ]

    operations = [
        migrations.CreateModel(
            name='SavedPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='saved_post', to='post.Post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='saved_post_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
