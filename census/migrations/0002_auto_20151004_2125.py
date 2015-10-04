# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('census', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apisetting',
            name='state_selected',
            field=models.CharField(default=b'', max_length=2, choices=[(b'', b'Select a State'), (b'01', b'Alabama'), (b'02', b'Alaska'), (b'04', b'Arizona'), (b'05', b'Arkansas'), (b'06', b'California'), (b'08', b'Colorado'), (b'09', b'Connecticut'), (b'10', b'Delaware'), (b'11', b'Washington, D.C.'), (b'12', b'Florida'), (b'13', b'Georgia'), (b'15', b'Hawaii'), (b'16', b'Idaho'), (b'17', b'Illinois'), (b'18', b'Indiana'), (b'19', b'Iowa'), (b'20', b'Kansas'), (b'21', b'Kentucky'), (b'22', b'Louisiana'), (b'23', b'Maine'), (b'24', b'Maryland'), (b'25', b'Massachusetts'), (b'26', b'Michigan'), (b'27', b'Minnesota'), (b'28', b'Mississippi'), (b'29', b'Missouri'), (b'30', b'Montana'), (b'31', b'Nebraska'), (b'32', b'Nevada'), (b'33', b'New Hampshire'), (b'34', b'New Jersey'), (b'35', b'New Mexico'), (b'36', b'New York'), (b'37', b'North Carolina'), (b'38', b'North Dakota'), (b'39', b'Ohio'), (b'40', b'Oklahoma'), (b'41', b'Oregon'), (b'42', b'Pennsylvania'), (b'44', b'Rhode Island'), (b'45', b'South Carolina'), (b'46', b'South Dakota'), (b'47', b'Tennessee'), (b'48', b'Texas'), (b'49', b'Utah'), (b'50', b'Vermont'), (b'51', b'Virginia'), (b'53', b'Washington'), (b'54', b'West Virginia'), (b'55', b'Wisconsin'), (b'56', b'Wyoming'), (b'60', b'American Samoa'), (b'66', b'Guam'), (b'72', b'Puerto Rico'), (b'78', b'Virgin Islands')]),
        ),
    ]
