# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-15 07:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mooc', '0008_auto_20161115_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='classification',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course', to='mooc.Classification'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lesson', to='mooc.Course'),
        ),
    ]