from django.conf.urls import url
from .views import CreateInvoice, DetailInvoice, EditInvoice, DeleteInvoice

urlpatterns = [
    url(r'^panel/invoices/nuevo/$', CreateInvoice.as_view(), name="nuevo"),
	url(r'^panel/invoices/(?P<pk>\d+)/$', DetailInvoice.as_view(), name="detalle"),
	url(r'^panel/invoices/editar/(?P<pk>\d+)/$', EditInvoice.as_view(), name="editar"),
	url(r'^panel/invoices/eliminar/(?P<pk>\d+)/$', DeleteInvoice.as_view(), name="eliminar"),

]