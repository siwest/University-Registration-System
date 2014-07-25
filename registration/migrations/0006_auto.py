# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding M2M table for field faculty_member on 'Department'
        m2m_table_name = db.shorten_name(u'registration_department_faculty_member')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('department', models.ForeignKey(orm[u'registration.department'], null=False)),
            ('facultymember', models.ForeignKey(orm[u'registration.facultymember'], null=False))
        ))
        db.create_unique(m2m_table_name, ['department_id', 'facultymember_id'])


    def backwards(self, orm):
        # Removing M2M table for field faculty_member on 'Department'
        db.delete_table(db.shorten_name(u'registration_department_faculty_member'))


    models = {
        u'registration.course': {
            'Meta': {'object_name': 'Course'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'credit': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'department': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['registration.Department']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'ta_requirement': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'registration.department': {
            'Meta': {'object_name': 'Department'},
            'budget': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'chairperson': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': u"orm['registration.FacultyMember']"}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'faculty_member': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['registration.FacultyMember']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['registration.Location']"}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50'})
        },
        u'registration.facultymember': {
            'Meta': {'object_name': 'FacultyMember'},
            'course_load': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rank': ('django.db.models.fields.CharField', [], {'default': "'Jr.'", 'max_length': '50'}),
            'staff': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['registration.StaffMember']"})
        },
        u'registration.location': {
            'Meta': {'object_name': 'Location'},
            'building': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'capacity': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'equipment': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'room': ('django.db.models.fields.CharField', [], {'max_length': '5'})
        },
        u'registration.section': {
            'Meta': {'object_name': 'Section'},
            'course': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['registration.Course']"}),
            'faculty': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['registration.FacultyMember']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['registration.Location']"}),
            'max_enrollment': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'number': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'student': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['registration.Student']", 'symmetrical': 'False'}),
            'teaching_assistant': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['registration.TeachingAssistant']"}),
            'time_slot': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['registration.TimeSlot']", 'symmetrical': 'False'})
        },
        u'registration.staffmember': {
            'Meta': {'object_name': 'StaffMember'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'salary': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'ssn': ('django.db.models.fields.CharField', [], {'max_length': '9'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'registration.student': {
            'Meta': {'object_name': 'Student'},
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'high_school': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'major': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'ssn': ('django.db.models.fields.CharField', [], {'max_length': '9'}),
            'year': ('django.db.models.fields.CharField', [], {'max_length': '4'})
        },
        u'registration.teachingassistant': {
            'Meta': {'object_name': 'TeachingAssistant'},
            'hours': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'staff': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['registration.StaffMember']"}),
            'status': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['registration.TeachingAssistantStatus']"}),
            'student': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['registration.Student']"})
        },
        u'registration.teachingassistantstatus': {
            'Meta': {'object_name': 'TeachingAssistantStatus'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'Full Time'", 'max_length': '20'})
        },
        u'registration.timeslot': {
            'Meta': {'object_name': 'TimeSlot'},
            'day': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'time': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        }
    }

    complete_apps = ['registration']