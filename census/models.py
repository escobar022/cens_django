from django.db import models
import json


class APISetting(models.Model):
    api_description = models.CharField(max_length=200)
    api_key = models.CharField(max_length=200)
    api_used = models.CharField(max_length=200, default='false')

    STATES = (
        ('', 'Select a State'),
        ('01', 'Alabama'),
        ('02', 'Alaska'),
        ('04', 'Arizona'),
        ('05', 'Arkansas'),
        ('06', 'California'),
        ('08', 'Colorado'),
        ('09', 'Connecticut'),
        ('10', 'Delaware'),
        ('11', 'Washington, D.C.'),
        ('12', 'Florida'),
        ('13', 'Georgia'),
        ('15', 'Hawaii'),
        ('16', 'Idaho'),
        ('17', 'Illinois'),
        ('18', 'Indiana'),
        ('19', 'Iowa'),
        ('20', 'Kansas'),
        ('21', 'Kentucky'),
        ('22', 'Louisiana'),
        ('23', 'Maine'),
        ('24', 'Maryland'),
        ('25', 'Massachusetts'),
        ('26', 'Michigan'),
        ('27', 'Minnesota'),
        ('28', 'Mississippi'),
        ('29', 'Missouri'),
        ('30', 'Montana'),
        ('31', 'Nebraska'),
        ('32', 'Nevada'),
        ('33', 'New Hampshire'),
        ('34', 'New Jersey'),
        ('35', 'New Mexico'),
        ('36', 'New York'),
        ('37', 'North Carolina'),
        ('38', 'North Dakota'),
        ('39', 'Ohio'),
        ('40', 'Oklahoma'),
        ('41', 'Oregon'),
        ('42', 'Pennsylvania'),
        ('44', 'Rhode Island'),
        ('45', 'South Carolina'),
        ('46', 'South Dakota'),
        ('47', 'Tennessee'),
        ('48', 'Texas'),
        ('49', 'Utah'),
        ('50', 'Vermont'),
        ('51', 'Virginia'),
        ('53', 'Washington'),
        ('54', 'West Virginia'),
        ('55', 'Wisconsin'),
        ('56', 'Wyoming'),
        ('60', 'American Samoa'),
        ('66', 'Guam'),
        ('72', 'Puerto Rico'),
        ('78', 'Virgin Islands'),
    )

    state_selected = models.CharField(max_length=2, choices=STATES, default='')

    def __str__(self):
        return self.api_description


class HousingVariable(models.Model):
    view_housing_variables = models.ForeignKey(APISetting)
    housing_variable = models.CharField(max_length=200)

    def __str__(self):
        return self.housing_variable


class CensusInfo(models.Model):
    census_info = models.CharField(max_length=200)
    api_view_id = models.CharField(max_length=2)

    def census_zip(self):
        census_zip = json.loads(self.census_info)
        return census_zip['zip code tabulation area']

    def __str__(self):
        return self.census_info
