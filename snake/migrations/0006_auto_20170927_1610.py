# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-27 14:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snake', '0005_auto_20170927_1132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snake',
            name='birthday',
            field=models.CharField(max_length=10, verbose_name='Né le'),
        ),
    ]
