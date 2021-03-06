# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'SignUp'
        db.create_table(u'signups_signup', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('para_voce', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=120, null=True, blank=True)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=120, null=True, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('horario', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('atualizado', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'signups', ['SignUp'])


    def backwards(self, orm):
        # Deleting model 'SignUp'
        db.delete_table(u'signups_signup')


    models = {
        u'signups.signup': {
            'Meta': {'object_name': 'SignUp'},
            'atualizado': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'horario': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'}),
            'para_voce': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        }
    }

    complete_apps = ['signups']