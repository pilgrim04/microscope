# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Orderitems'
        db.create_table(u'apps_orderitems', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('parent', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('product', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('title', self.gf('django.db.models.fields.CharField')(default='', max_length=255)),
            ('url', self.gf('django.db.models.fields.CharField')(default='', max_length=64)),
            ('price', self.gf('django.db.models.fields.FloatField')(default=0.0)),
            ('count', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
        ))
        db.send_create_signal(u'apps', ['Orderitems'])

        # Adding model 'Orders'
        db.create_table(u'apps_orders', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ip', self.gf('django.db.models.fields.CharField')(default='', max_length=20)),
            ('name', self.gf('django.db.models.fields.CharField')(default='', max_length=32)),
            ('email', self.gf('django.db.models.fields.CharField')(default='', max_length=32)),
            ('phone', self.gf('django.db.models.fields.CharField')(default='', max_length=32)),
            ('city', self.gf('django.db.models.fields.CharField')(default='', max_length=32)),
            ('index', self.gf('django.db.models.fields.CharField')(default='', max_length=32)),
            ('street', self.gf('django.db.models.fields.CharField')(default='', max_length=128)),
            ('house', self.gf('django.db.models.fields.CharField')(default='', max_length=32)),
            ('housing', self.gf('django.db.models.fields.CharField')(default='', max_length=32)),
            ('office', self.gf('django.db.models.fields.CharField')(default='', max_length=32)),
            ('comments', self.gf('django.db.models.fields.CharField')(default='', max_length=128)),
            ('delivery', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('cdate', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('uid', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('pay', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('company', self.gf('django.db.models.fields.CharField')(default='', max_length=32)),
            ('inn', self.gf('django.db.models.fields.CharField')(default='', max_length=32)),
            ('kpp', self.gf('django.db.models.fields.CharField')(default='', max_length=32)),
            ('juraddress', self.gf('django.db.models.fields.CharField')(default='', max_length=32)),
            ('bank_r_acc', self.gf('django.db.models.fields.CharField')(default='', max_length=32)),
            ('bank_k_acc', self.gf('django.db.models.fields.CharField')(default='', max_length=32)),
            ('bank_bik', self.gf('django.db.models.fields.CharField')(default='', max_length=32)),
            ('baddress', self.gf('django.db.models.fields.CharField')(default='', max_length=128)),
            ('status', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'apps', ['Orders'])


    def backwards(self, orm):
        # Deleting model 'Orderitems'
        db.delete_table(u'apps_orderitems')

        # Deleting model 'Orders'
        db.delete_table(u'apps_orders')


    models = {
        u'apps.orderitems': {
            'Meta': {'object_name': 'Orderitems'},
            'count': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'parent': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'price': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'product': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            'url': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '64'})
        },
        u'apps.orders': {
            'Meta': {'object_name': 'Orders'},
            'baddress': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '128'}),
            'bank_bik': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '32'}),
            'bank_k_acc': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '32'}),
            'bank_r_acc': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '32'}),
            'cdate': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'city': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '32'}),
            'comments': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '128'}),
            'company': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '32'}),
            'delivery': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'email': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '32'}),
            'house': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '32'}),
            'housing': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '32'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '32'}),
            'inn': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '32'}),
            'ip': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '20'}),
            'juraddress': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '32'}),
            'kpp': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '32'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '32'}),
            'office': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '32'}),
            'pay': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'phone': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '32'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'street': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '128'}),
            'uid': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['apps']