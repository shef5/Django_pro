# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-04-04 20:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_auto_20160405_0131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='api',
            name='da',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='api',
            name='pa',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
    ]
