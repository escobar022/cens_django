from django.views import generic

from .models import APISetting, CensusInfo


class IndexView(generic.ListView):
    template_name = 'census/index.html'
    context_object_name = 'all_census_views'
    # APISetting.objects.exclude(api_used='true')

    def get_queryset(self):
        return APISetting.objects.exclude(api_used='false')


class DetailView(generic.DetailView):
    context_object_name = 'census_view'
    template_name = 'census/detail.html'
    queryset = APISetting.objects.all()

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        context['censuspoints'] = CensusInfo.objects.all()
        return context
