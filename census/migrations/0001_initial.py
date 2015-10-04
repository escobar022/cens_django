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
                ('state_selected', models.CharField(default=b'', max_length=2, choices=[(b'', b'Select a State'), (b'1', b'Alabama'), (b'2', b'Alaska'), (b'3', b'Arizona'), (b'4', b'Arkansas'), (b'5', b'California'), (b'6', b'Colorado'), (b'7', b'Connecticut'), (b'8', b'Delaware'), (b'9', b'Florida'), (b'10', b'Georgia'), (b'11', b'Hawaii'), (b'12', b'Idaho'), (b'13', b'Illinois'), (b'14', b'Indiana'), (b'15', b'Iowa'), (b'16', b'Kansas'), (b'17', b'Kentucky'), (b'18', b'Louisiana'), (b'19', b'Maine'), (b'20', b'Maryland'), (b'21', b'Massachusetts'), (b'22', b'Michigan'), (b'23', b'Minnesota'), (b'24', b'Mississippi'), (b'25', b'Missouri'), (b'26', b'Montana'), (b'27', b'Nebraska'), (b'28', b'Nevada'), (b'29', b'New Hampshire'), (b'30', b'New Jersey'), (b'31', b'New Mexico'), (b'32', b'New York'), (b'33', b'North Carolina'), (b'34', b'North Dakota'), (b'35', b'Ohio'), (b'36', b'Oklahoma'), (b'37', b'Oregon'), (b'38', b'Pennsylvania'), (b'39', b'Rhode Island'), (b'40', b'South Carolina'), (b'41', b'South Dakota'), (b'42', b'Tennessee'), (b'43', b'Texas'), (b'44', b'Utah'), (b'45', b'Vermont'), (b'46', b'Virginia'), (b'47', b'Washington'), (b'48', b'West Virginia'), (b'49', b'Wisconsin'), (b'50', b'Wyoming')])),
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
