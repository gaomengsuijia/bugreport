# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2018-05-06 03:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mybugreport', '0005_bug_bugtemlate'),
    ]

    operations = [
        migrations.AddField(
            model_name='bug',
            name='bugtemlate',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='mybugreport.Bugtemlate'),
            preserve_default=False,
        ),
    ]