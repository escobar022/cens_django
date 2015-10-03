# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='APISetting',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('api_description', models.CharField(max_length=200)),
                ('api_key', models.CharField(max_length=200)),
                ('api_used', models.CharField(default=b'false', max_length=200)),
                ('state_selected', models.CharField(default=b'', max_length=2, choices=[(b'', b'Select a State'), (b'36', b'New York'), (b'37', b'New Jersey')])),
            ],
        ),
        migrations.CreateModel(
            name='CensusInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('census_info', models.CharField(max_length=200)),
                ('api_view_id', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='HousingVariable',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('housing_variable', models.CharField(max_length=200)),
                ('view_housing_variables', models.ForeignKey(to='census.APISetting')),
            ],
        ),
    ]
