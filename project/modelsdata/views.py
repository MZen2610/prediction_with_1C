from .models import *
from django.views.generic import ListView

class HomePage(ListView):
		model = Predictionmodel
		template_name = 'modelsdata/home.html'
		context_object_name = 'modelsdata'
		ordering = ['-id']

		def get_context_data(self, *, object_list=None, **kwargs):
			ctx = super(HomePage, self).get_context_data(**kwargs)
			ctx['title'] = 'Главная страница сайта'
			return ctx

