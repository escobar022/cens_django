import requests

from django.core.management.base import BaseCommand
from census.models import APISetting
from census.models import CensusInfo
import json


class Command(BaseCommand):
    help = 'Imports data from API if not done before'

    def handle(self, *args, **options):
        calls = APISetting.objects.exclude(api_used='true')
        for call in calls:
            # Creates api call with settings from APISetting
            census_api = 'http://api.census.gov/data/2010/sf1?key='
            all_hs_variables = call.housingvariable_set.values_list('housing_variable', flat=True)
            all_hs_vars_string = ','.join(all_hs_variables)
            get_hs_vars = '&get=' + all_hs_vars_string
            get_for_zip = '&for=zip+code+tabulation+area:*'
            get_state = '&in=state:' + call.state_selected

            join_api_call = (census_api, str(call.api_key), str(get_hs_vars), str(get_for_zip), str(get_state))

            api_call = ''.join(map(str, join_api_call))
            r = requests.get(api_call)

            data_received = r.json()

            data_received_keys = data_received[0]

            census_entry = dict()

            for each_value in data_received[1:]:
                for i in range(len(data_received_keys)):
                    census_entry[data_received_keys[i]] = each_value[i]
                census_parsed = json.dumps(census_entry)
                entry = CensusInfo(census_info=census_parsed, api_view_id=call.id)
                entry.save()

            call.api_used = 'true'
            call.save()
