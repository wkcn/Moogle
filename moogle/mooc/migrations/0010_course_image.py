# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-16 15:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mooc', '0009_auto_20161115_1555'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='image',
            field=models.CharField(default='http://ogqprkml5.bkt.clouddn.com/public/16-11-16/90666112.jpg-square', max_length=256),
        ),
    ]
