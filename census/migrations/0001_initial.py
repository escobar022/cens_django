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
            name='CensusEntry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('census_entry', models.CharField(max_length=200)),
                ('api_view_id', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('choice_text', models.CharField(max_length=200)),
                ('votes', models.IntegerField(default=0)),
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
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question_text', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
            ],
        ),
        migrations.AddField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(to='census.Question'),
        ),
    ]
