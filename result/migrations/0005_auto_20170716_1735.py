# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-16 12:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0004_remove_semester_branchsem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='batch',
            name='branch',
        ),
        migrations.AddField(
            model_name='semester',
            name='branch',
            field=models.CharField(default='pavan', max_length=20),
            preserve_default=False,
        ),
    ]
