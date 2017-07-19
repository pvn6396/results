# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-11 18:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0002_batch_branch'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='semester',
            name='batchy',
        ),
        migrations.AddField(
            model_name='semester',
            name='batchyear',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='batchyear', to='result.batch'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='semester',
            name='branchsem',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='branchsem', to='result.batch'),
            preserve_default=False,
        ),
    ]