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


class MyOrderItemView(TemplateView):
    template_name = 'myorderitem.html'

    def get_context_data(self, **kwargs):
        context = super(MyOrderItemView, self).get_context_data(**kwargs)

        return context


class MyOrdersView(TemplateView):
    template_name = 'myorders.html'

    def get_context_data(self, **kwargs):
        context = super(MyOrdersView, self).get_context_data(**kwargs)

        return context


class OrderItemView(TemplateView):
    template_name = 'orderitem.html'

    def get_context_data(self, **kwargs):
        context = super(OrderItemView, self).get_context_data(**kwargs)

        return context


class OrdersView(TemplateView):
    template_name = 'orders.html'

    def get_context_data(self, **kwargs):
        context = super(OrdersView, self).get_context_data(**kwargs)

        return context