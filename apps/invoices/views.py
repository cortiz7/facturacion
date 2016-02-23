from django.shortcuts import render
from django.core.urlresolvers import reverse, reverse_lazy


from django.views.generic import TemplateView, CreateView, DetailView, UpdateView, DeleteView

from .models import Invoice
from .forms import InvoiceForm



class CreateInvoice(CreateView):

	form_class = InvoiceForm
	template_name = 'invoices/panel/crear.html'
	success_url = reverse_lazy('main:home')


class DetailInvoice(DetailView):

	template_name = 'invoices/panel/detalle.html'
	model = Invoice


class EditInvoice(UpdateView):

	template_name = 'invoices/panel/editar.html'
	success_url = reverse_lazy('main:home')
	model = Invoice
	form_class = InvoiceForm


class DeleteInvoice(DeleteView):

	template_name = 'invoices/panel/eliminar.html'
	model = Invoice
	success_url = reverse_lazy('main:home')
	context_object_name = 'invoice'