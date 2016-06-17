# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-17 16:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_auto_20160617_1057'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='plan_after_eight',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='plan_fifth_sixth',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='plan_first_second',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='plan_seventh_eight',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='plan_third_fourth',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]