# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-05 22:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0003_auto_20180505_2259'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='boards',
            field=models.ManyToManyField(related_name='my_boards', to='boards.Board'),
        ),
    ]
