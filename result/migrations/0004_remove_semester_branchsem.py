# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-11 19:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0003_auto_20170712_0022'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='semester',
            name='branchsem',
        ),
    ]