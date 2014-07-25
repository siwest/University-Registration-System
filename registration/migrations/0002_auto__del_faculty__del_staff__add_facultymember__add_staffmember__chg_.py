# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Faculty'
        db.delete_table(u'registration_faculty')

        # Deleting model 'Staff'
        db.delete_table(u'registration_staff')

        # Adding model 'FacultyMember'
        db.create_table(u'registration_facultymember', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('staff', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['registration.StaffMember'])),
            ('rank', self.gf('django.db.models.fields.CharField')(default='Jr.', max_length=50)),
            ('course_load', self.gf('django.db.models.fields.IntegerField')(default=1)),
        ))
        db.send_create_signal(u'registration', ['FacultyMember'])

        # Adding model 'StaffMember'
        db.create_table(u'registration_staffmember', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ssn', self.gf('django.db.models.fields.CharField')(max_length=9)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('street', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('salary', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'registration', ['StaffMember'])


        # Changing field 'Department.chairperson'
        db.alter_column(u'registration_department', 'chairperson_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['registration.FacultyMember']))

        # Changing field 'Section.faculty'
        db.alter_column(u'registration_section', 'faculty_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['registration.FacultyMember']))

        # Changing field 'TeachingAssistant.staff'
        db.alter_column(u'registration_teachingassistant', 'staff_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['registration.StaffMember']))

    def backwards(self, orm):
        # Adding model 'Faculty'
        db.create_table(u'registration_faculty', (
            ('course_load', self.gf('django.db.models.fields.IntegerField')(default=1)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('rank', self.gf('django.db.models.fields.CharField')(default='Jr.', max_length=50)),
            ('staff', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['registration.Staff'])),
        ))
        db.send_create_signal(u'registration', ['Faculty'])

        # Adding model 'Staff'
        db.create_table(u'registration_staff', (
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('street', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('salary', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('ssn', self.gf('django.db.models.fields.CharField')(max_length=9)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=50)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'registration', ['Staff'])

        # Deleting model 'FacultyMember'
        db.delete_table(u'registration_facultymember')

        # Deleting model 'StaffMember'
        db.delete_table(u'registration_staffmember')


        # Changing field 'Department.chairperson'
        db.alter_column(u'registration_department', 'chairperson_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['registration.Faculty']))

        # Changing field 'Section.faculty'
        db.alter_column(u'registration_section', 'faculty_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['registration.Faculty']))

        # Changing field 'TeachingAssistant.staff'
        db.alter_column(u'registration_teachingassistant', 'staff_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['registration.Staff']))

    models = {
        u'registration.course': {
            'Meta': {'object_name': 'Course'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'credit': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'ta_requirement': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'registration.department': {
            'Meta': {'object_name': 'Department'},
            'budget': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'chairperson': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': u"orm['registration.FacultyMember']"}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'faculty': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['registration.FacultyMember']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
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