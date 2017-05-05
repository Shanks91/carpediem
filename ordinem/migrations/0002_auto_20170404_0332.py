# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-04-03 22:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ordinem', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='gallery/')),
                ('time_stamp', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AlterField(
            model_name='ngo',
            name='creation_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='ngo',
            name='name',
            field=models.CharField(max_length=300),
        ),
        migrations.AddField(
            model_name='gallery',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ordinem.Ngo'),
        ),
    ]
