from django import template

register = template.Library()


@register.filter
def in_current_view(censuspoints, view_id):
    return censuspoints.filter(api_view_id=view_id)
