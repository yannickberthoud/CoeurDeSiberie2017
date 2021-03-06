# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-27 09:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snake', '0004_auto_20170926_2140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='image',
            field=models.ImageField(upload_to='snakes', verbose_name='Nom'),
        ),
        migrations.AlterField(
            model_name='snake',
            name='flex_price',
            field=models.BooleanField(default=False, verbose_name='Prix à discuter'),
            preserve_default=False,
        ),
    ]
