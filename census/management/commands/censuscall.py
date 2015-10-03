import requests

from django.core.management.base import BaseCommand, CommandError
from census.models import APISetting
from census.models import CensusInfo


class Command(BaseCommand):
    help = 'Imports data from API if not done before'

    def handle(self, *args, **options):
        calls = APISetting.objects.exclude(api_used='true')
        for call in calls:
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
                # census_entry = {key: value for (key, value) in each_value}
                for i in range(len(data_received_keys)):
                    census_entry[data_received_keys[i]] = each_value[i]
                entry = CensusInfo(census_info=census_entry, api_view_id=call.id)
                # print(census_entry)
                entry.save()

            call.api_used = 'true'
            call.save()
