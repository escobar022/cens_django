# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('census', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CensusEntry',
            new_name='CensusInfo',
        ),
        migrations.RenameField(
            model_name='censusinfo',
            old_name='census_entry',
            new_name='census_info',
        ),
    ]
