# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('cliente', models.CharField(max_length=150)),
                ('number', models.PositiveIntegerField(default=0, null=True, blank=True)),
                ('total', models.DecimalField(default=0.0, max_digits=5, decimal_places=2)),
            ],
        ),
        migrations.CreateModel(
            name='InvoiceLine',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('product', models.CharField(max_length=150)),
                ('qty', models.PositiveIntegerField(default=0, null=True, blank=True)),
                ('price_unit', models.DecimalField(default=0.0, max_digits=5, decimal_places=2)),
                ('total', models.DecimalField(default=0.0, max_digits=5, decimal_places=2)),
                ('invoice', models.ForeignKey(to='invoices.Invoice')),
            ],
        ),
    ]
