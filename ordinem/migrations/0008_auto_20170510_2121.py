# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-05-10 15:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordinem', '0007_ngo_bio'),
    ]

    operations = [
        migrations.AddField(
            model_name='ngo',
            name='likes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='ngo',
            name='rating',
            field=models.FloatField(default=0.0),
        ),
    ]