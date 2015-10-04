from django import template
import json

register = template.Library()

# Gets censusinfo by the id of the current censusview
@register.filter
def in_current_view(data, view_id):
    return data.filter(api_view_id=view_id)


@register.filter
def get_hs_values(data, key):
    census_zip = json.loads(data)
    return census_zip[key]
