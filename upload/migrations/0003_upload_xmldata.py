# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-04-07 10:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0002_auto_20180330_2229'),
    ]

    operations = [
        migrations.AddField(
            model_name='upload',
            name='xmldata',
            field=models.TextField(blank=True),
        ),
    ]