# coding: utf-8
from django.contrib import admin
from django.core.cache import get_cache
from django.contrib.admin import ListFilter
from .models import *
# noinspection PyUnresolvedReferences
from django.utils.translation import ugettext_lazy as _


class OrderitemsAdmin(admin.ModelAdmin):
    pass


class OrdersAdmin(admin.ModelAdmin):
    list_display = ('id', 'delivery', 'status', 'name', 'pay')
    list_filter = ('status', 'delivery', 'pay')

admin.site.register(Orderitems, OrderitemsAdmin)
admin.site.register(Orders, OrdersAdmin)