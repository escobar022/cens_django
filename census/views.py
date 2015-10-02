from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
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
        # And so on for more models
        return context


class ResultsView(generic.DetailView):
    model = APISetting
    template_name = 'census/results.html'


def vote(request, question_id):
    p = get_object_or_404(APISetting, pk=question_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, APISetting.DoesNotExist):

        return render(request, 'census/detail.html', {
            'question': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()

        return HttpResponseRedirect(reverse('census:results', args=(p.id,)))
