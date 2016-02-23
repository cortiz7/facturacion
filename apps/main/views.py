from django.shortcuts import render
from django.views.generic import TemplateView
from apps.invoices.models import Invoice

class Home(TemplateView):

	template_name="main/home.html"

	def get_context_data(self, **kwargs):
		context = super(Home, self).get_context_data(**kwargs)
		context['invoices'] = Invoice.objects.all()
		
		return context
