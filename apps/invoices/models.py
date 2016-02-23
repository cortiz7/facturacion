#encoding:utf-8
from django.db import models

class Invoice(models.Model):
	date = models.DateField(auto_now_add=False)
	cliente = models.CharField(max_length=150)
	number = models.PositiveIntegerField(default=0, blank=True, null=True)
	total = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)

	def __unicode__(self):
		return "%d" %self.number

class InvoiceLine(models.Model):
	invoice = models.ForeignKey(Invoice)
	product = models.CharField(max_length=150)
	qty = models.PositiveIntegerField(default=0, blank=True, null=True)
	price_unit = total = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
	total = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)

	def __unicode__(self):
		return "Factura: %s - Detalle: %d" %(self.invoice.number,self.id)