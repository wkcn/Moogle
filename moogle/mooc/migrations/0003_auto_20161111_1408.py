# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-11 06:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mooc', '0002_auto_20161110_2108'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, unique=True)),
                ('description', models.CharField(blank=True, max_length=1024)),
                ('teacher', models.CharField(blank=True, max_length=128)),
                ('school', models.CharField(blank=True, max_length=256)),
                ('mtime', models.DateTimeField(auto_now=True)),
                ('ctime', models.DateTimeField(auto_now_add=True)),
                ('mark_num', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
