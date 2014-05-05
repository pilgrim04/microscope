# coding: utf-8
from django.db import models


class Delivery(models.Model):
    field1 = models.CharField(max_length=256)


class Users(models.Model):
    field1 = models.CharField(max_length=256)


class Status(models.Model):
    field1 = models.CharField(max_length=256)


class Zakaz(models.Model):
    field1 = models.CharField(max_length=256)


class Items(models.Model):
    ip = models.CharField(max_length=15)
    name = models.CharField(max_length=256)
    email = models.CharField(max_length=256)
    phone = models.IntegerField()
    city = models.CharField(max_length=256)
    index = models.IntegerField()
    street = models.CharField(max_length=256)
    house = models.IntegerField()
    housing = models.IntegerField()
    office = models.IntegerField()
    comments = models.CharField(max_length=256)
    delivery = models.ForeignKey(Delivery)
    cdate = models.DateTimeField()
    uid = models.ForeignKey(Users)
    pay = models.SmallIntegerField()
    company = models.CharField(max_length=256)
    inn = models.CharField(max_length=256)
    kpp = models.CharField(max_length=256)
    juraddress = models.CharField(max_length=256)
    bank_r_acc = models.CharField(max_length=256)
    bank_k_acc = models.CharField(max_length=256)
    bank_bik = models.CharField(max_length=256)
    baddress = models.CharField(max_length=256)
    status = models.ForeignKey(Status)
    #a_orders


class Orders(models.Model):
    parent = models.ForeignKey(Zakaz)
    product = models.ForeignKey(Items)
    title = models.CharField(max_length=256)
    url = models.CharField(max_length=256)
    price = models.FloatField()
    count = models.FloatField()
    # a_order-items