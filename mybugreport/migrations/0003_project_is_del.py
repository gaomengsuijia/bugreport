# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-05-05 06:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mybugreport', '0002_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='is_del',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
    ]
