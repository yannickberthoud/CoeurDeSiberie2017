# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-26 13:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('snake', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snake',
            name='flex_price',
            field=models.FloatField(blank=True, null=True, verbose_name='Prix à discuter'),
        ),
        migrations.RemoveField(
            model_name='snake',
            name='mutation',
        ),
        migrations.AddField(
            model_name='snake',
            name='mutation',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='snake.Mutation'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='snake',
            name='parent_f',
            field=models.CharField(blank=True, max_length=256, verbose_name='Reproductrice'),
        ),
        migrations.AlterField(
            model_name='snake',
            name='parent_m',
            field=models.CharField(blank=True, max_length=256, verbose_name='Reproducteur'),
        ),
        migrations.AlterField(
            model_name='snake',
            name='price_cpl',
            field=models.FloatField(blank=True, null=True, verbose_name='Prix de couple'),
        ),
        migrations.AlterField(
            model_name='snake',
            name='price_sale',
            field=models.FloatField(blank=True, null=True, verbose_name='Prix de vente'),
        ),
    ]
