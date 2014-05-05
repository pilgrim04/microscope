# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Delivery'
        db.create_table(u'apps_delivery', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('field1', self.gf('django.db.models.fields.CharField')(max_length=256)),
        ))
        db.send_create_signal(u'apps', ['Delivery'])

        # Adding model 'Users'
        db.create_table(u'apps_users', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('field1', self.gf('django.db.models.fields.CharField')(max_length=256)),
        ))
        db.send_create_signal(u'apps', ['Users'])

        # Adding model 'Status'
        db.create_table(u'apps_status', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('field1', self.gf('django.db.models.fields.CharField')(max_length=256)),
        ))
        db.send_create_signal(u'apps', ['Status'])

        # Adding model 'Zakaz'
        db.create_table(u'apps_zakaz', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('field1', self.gf('django.db.models.fields.CharField')(max_length=256)),
        ))
        db.send_create_signal(u'apps', ['Zakaz'])

        # Adding model 'Items'
        db.create_table(u'apps_items', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ip', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('phone', self.gf('django.db.models.fields.IntegerField')()),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('index', self.gf('django.db.models.fields.IntegerField')()),
            ('street', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('house', self.gf('django.db.models.fields.IntegerField')()),
            ('housing', self.gf('django.db.models.fields.IntegerField')()),
            ('office', self.gf('django.db.models.fields.IntegerField')()),
            ('comments', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('delivery', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['apps.Delivery'])),
            ('cdate', self.gf('django.db.models.fields.DateTimeField')()),
            ('uid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['apps.Users'])),
            ('pay', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('company', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('inn', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('kpp', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('juraddress', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('bank_r_acc', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('bank_k_acc', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('bank_bik', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('baddress', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('status', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['apps.Status'])),
        ))
        db.send_create_signal(u'apps', ['Items'])

        # Adding model 'Orders'
        db.create_table(u'apps_orders', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['apps.Zakaz'])),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['apps.Items'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('price', self.gf('django.db.models.fields.FloatField')()),
            ('count', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal(u'apps', ['Orders'])


    def backwards(self, orm):
        # Deleting model 'Delivery'
        db.delete_table(u'apps_delivery')

        # Deleting model 'Users'
        db.delete_table(u'apps_users')

        # Deleting model 'Status'
        db.delete_table(u'apps_status')

        # Deleting model 'Zakaz'
        db.delete_table(u'apps_zakaz')

        # Deleting model 'Items'
        db.delete_table(u'apps_items')

        # Deleting model 'Orders'
        db.delete_table(u'apps_orders')


    models = {
        u'apps.delivery': {
            'Meta': {'object_name': 'Delivery'},
            'field1': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'apps.items': {
            'Meta': {'object_name': 'Items'},
            'baddress': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'bank_bik': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'bank_k_acc': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'bank_r_acc': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'cdate': ('django.db.models.fields.DateTimeField', [], {}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'comments': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'company': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'delivery': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['apps.Delivery']"}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'house': ('django.db.models.fields.IntegerField', [], {}),
            'housing': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index': ('django.db.models.fields.IntegerField', [], {}),
            'inn': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'juraddress': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'kpp': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'office': ('django.db.models.fields.IntegerField', [], {}),
            'pay': ('django.db.models.fields.SmallIntegerField', [], {}),
            'phone': ('django.db.models.fields.IntegerField', [], {}),
            'status': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['apps.Status']"}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'uid': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['apps.Users']"})
        },
        u'apps.orders': {
            'Meta': {'object_name': 'Orders'},
            'count': ('django.db.models.fields.FloatField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['apps.Zakaz']"}),
            'price': ('django.db.models.fields.FloatField', [], {}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['apps.Items']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        u'apps.status': {
            'Meta': {'object_name': 'Status'},
            'field1': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'apps.users': {
            'Meta': {'object_name': 'Users'},
            'field1': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'apps.zakaz': {
            'Meta': {'object_name': 'Zakaz'},
            'field1': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['apps']