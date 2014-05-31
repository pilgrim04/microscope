# coding: utf-8
from django.db import models
from .consts import *


class Orderitems(models.Model):
    parent = models.IntegerField(null=False, default=0, blank=True)
    product = models.IntegerField(null=False, default=0, blank=True)
    title = models.CharField(max_length=255, null=False, default='', blank=True)
    url = models.CharField(max_length=64, null=False, default='', blank=True)
    price = models.FloatField(null=False, default=0.0, blank=True)
    count = models.SmallIntegerField(null=False, default=0, blank=True)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __unicode__(self):
        return unicode(self.title)


class Orders(models.Model):
    ip = models.CharField(max_length=20, null=False, default='', blank=True)
    name = models.CharField(max_length=32, null=False, default='', blank=True)
    email = models.CharField(max_length=32, null=False, default='', blank=True)
    phone = models.CharField(max_length=32, null=False, default='', blank=True)
    city =  models.CharField(max_length=32, null=False, default='', blank=True)
    index = models.CharField(max_length=32, null=False, default='', blank=True)
    street = models.CharField(max_length=128, null=False, default='', blank=True)
    house = models.CharField(max_length=32, null=False, default='', blank=True)
    housing = models.CharField(max_length=32, null=False, default='', blank=True)
    office = models.CharField(max_length=32, null=False, default='', blank=True)
    comments = models.CharField(max_length=128, null=False, default='', blank=True)
    delivery = models.IntegerField(choices=ORDERS_DELIVERY_CHOICES, null=False, default=0, blank=True)
    cdate = models.IntegerField(null=False, default=0, blank=True)
    uid = models.IntegerField(null=False, default=0, blank=True)
    pay = models.IntegerField(choices=ORDERS_PAY_CHOICES, null=False, default=0, blank=True)
    company = models.CharField(max_length=32, null=False, default='', blank=True)
    inn = models.CharField(max_length=32, null=False, default='', blank=True)
    kpp = models.CharField(max_length=32, null=False, default='', blank=True)
    juraddress = models.CharField(max_length=32, null=False, default='', blank=True)
    bank_r_acc = models.CharField(max_length=32, null=False, default='', blank=True)
    bank_k_acc = models.CharField(max_length=32, null=False, default='', blank=True)
    bank_bik = models.CharField(max_length=32, null=False, default='', blank=True)
    baddress = models.CharField(max_length=128, null=False, default='', blank=True)
    status = models.IntegerField(choices=ORDERS_STATUS_CHOICES, null=False, default=0, blank=True)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __unicode__(self):
        return unicode(self.id)
