from django.db import models

cities = [
    {'name': 'Mumbai', 'population': '19,000,000', 'country': 'India'},
    {'name': 'Calcutta', 'population': '15,000,000', 'country': 'India'},
    {'name': 'New York', 'population': '20,000,000', 'country': 'USA'},
    {'name': 'Chicago', 'population': '7,000,000', 'country': 'USA'},
    {'name': 'Tokyo', 'population': '33,000,000', 'country': 'Japan'},
]


class APISetting(models.Model):
    api_description = models.CharField(max_length=200)
    api_key = models.CharField(max_length=200)
    api_used = models.CharField(max_length=200, default='false')

    STATES = (
        ('', 'Select a State'),
        ('36', 'New York'),
        ('37', 'New Jersey'),
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
        census_zip = self.census_info
        return census_zip

    def __str__(self):
        return self.census_info
