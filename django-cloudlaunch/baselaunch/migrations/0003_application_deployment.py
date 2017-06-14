# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-16 10:13
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('baselaunch', '0002_application_version_cloud_config'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicationDeployment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=60)),
                ('instance_type', models.TextField(blank=True, help_text='Instance Type for this deployment', max_length=256)),
                ('placement_zone', models.TextField(blank=True, help_text='Placement zone in which this deployment was made.', max_length=256, null=True)),
                ('keypair_name', models.TextField(blank=True, help_text='Keypair names for this virtual machine.', max_length=256, null=True)),
                ('network', models.TextField(blank=True, help_text='Network for this virtual machine.', max_length=256, null=True)),
                ('subnet', models.TextField(blank=True, help_text='Network for this virtual machine.', max_length=256, null=True)),
                ('provider_settings', models.TextField(blank=True, help_text='Cloud provider specific settings used for this launch.', max_length=16384, null=True)),
                ('application_config', models.TextField(blank=True, help_text='Application configuration data used for this launch.', max_length=16384, null=True)),
                ('application_version', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='baselaunch.ApplicationVersion')),
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('target_cloud', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='baselaunch.Cloud')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='applicationversioncloudconfig',
            name='image',
            field=smart_selects.db_fields.ChainedForeignKey(chained_field='cloud', chained_model_field='cloud', on_delete=django.db.models.deletion.CASCADE, to='baselaunch.CloudImage'),
        ),
    ]
