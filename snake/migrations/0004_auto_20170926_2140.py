# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-26 19:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('snake', '0003_auto_20170926_2036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='snake',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='snakesg', related_query_name='snakeg', to='snake.Snake'),
        ),
    ]