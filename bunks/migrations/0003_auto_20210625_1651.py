# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2021-06-25 16:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bunks', '0002_auto_20210625_1641'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bunk',
            old_name='time',
            new_name='bunk_time',
        ),
    ]