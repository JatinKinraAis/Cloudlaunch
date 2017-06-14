# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-01-11 04:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('baselaunch', '0013_usage'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='default_version',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='baselaunch.ApplicationVersion'),
        ),
        migrations.AddField(
            model_name='applicationversion',
            name='default_cloud',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='baselaunch.Cloud'),
        ),
    ]
