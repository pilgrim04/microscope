from django.shortcuts import render
from .models import *
from django.views.generic import TemplateView


class ListView(TemplateView):
    template_name = 'list.html'

    def get_context_data(self, **kwargs):
        context = super(ListView, self).get_context_data(**kwargs)
        items = Items.objects.all()
        context['items'] = items

        orders = Orders.objects.all()
        context['orders'] = orders

        return context