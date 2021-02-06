from .models import *
from django.views.generic import ListView, DetailView


class HomePage(ListView):
    model = Predictionmodel
    template_name = 'modelsdata/home.html'
    context_object_name = 'modelsdata'
    ordering = ['-id']

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super(HomePage, self).get_context_data(**kwargs)
        ctx['title'] = 'Главная страница сайта'
        return ctx


class ModelsDataDetailPage(DetailView):
    model = Predictionmodel
    template_name = 'modelsdata/model-detail.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super(ModelsDataDetailPage, self).get_context_data(**kwargs)
        ctx['title'] = Predictionmodel.objects.filter(slug=self.kwargs['slug']).first()
        ctx['requesttext'] = Predictionrequest.objects.filter(predictionmodel=ctx['title']).order_by('number')
        return ctx


class PredictionrequestDetailPage(DetailView):
    model = Predictionmodel
    template_name = 'modelsdata/predictions-detail.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super(PredictionrequestDetailPage, self).get_context_data(**kwargs)

        predmodel = Predictionmodel.objects.filter(slug=self.kwargs['slug']).first()
        requesttext = list(Predictionrequest.objects.filter(predictionmodel=predmodel).filter(slug=self.kwargs['request_slug']).values())

        # print(requesttext)
        ctx['title'] = requesttext[0]['title']
        ctx['comm'] = requesttext[0]['comment']
        ctx['addres'] = requesttext[0]['addres_http']
        return ctx