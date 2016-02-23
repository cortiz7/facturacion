#encoding:utf-8
from django.contrib import admin

from .models import Invoice, InvoiceLine

@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
	pass

@admin.register(InvoiceLine)
class InvoiceLineAdmin(admin.ModelAdmin):
	pass