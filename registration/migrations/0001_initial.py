# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Student'
        db.create_table(u'registration_student', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ssn', self.gf('django.db.models.fields.CharField')(max_length=9)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('high_school', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('major', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('year', self.gf('django.db.models.fields.CharField')(max_length=4)),
        ))
        db.send_create_signal(u'registration', ['Student'])

        # Adding model 'Staff'
        db.create_table(u'registration_staff', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ssn', self.gf('django.db.models.fields.CharField')(max_length=9)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('street', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('salary', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'registration', ['Staff'])

        # Adding model 'Faculty'
        db.create_table(u'registration_faculty', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('staff', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['registration.Staff'])),
            ('rank', self.gf('django.db.models.fields.CharField')(default='Jr.', max_length=50)),
            ('course_load', self.gf('django.db.models.fields.IntegerField')(default=1)),
        ))
        db.send_create_signal(u'registration', ['Faculty'])

        # Adding model 'TeachingAssistantStatus'
        db.create_table(u'registration_teachingassistantstatus', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('status', self.gf('django.db.models.fields.CharField')(default='Full Time', max_length=20)),
        ))
        db.send_create_signal(u'registration', ['TeachingAssistantStatus'])

        # Adding model 'TeachingAssistant'
        db.create_table(u'registration_teachingassistant', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('student', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['registration.Student'])),
            ('staff', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['registration.Staff'])),
            ('hours', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('status', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['registration.TeachingAssistantStatus'])),
        ))
        db.send_create_signal(u'registration', ['TeachingAssistant'])

        # Adding model 'Department'
        db.create_table(u'registration_department', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('name', self.gf('django.db.models.fields.CharField')(default='', max_length=50)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('budget', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('chairperson', self.gf('django.db.models.fields.related.ForeignKey')(related_name='+', to=orm['registration.Faculty'])),
        ))
        db.send_create_signal(u'registration', ['Department'])

        # Adding M2M table for field faculty on 'Department'
        m2m_table_name = db.shorten_name(u'registration_department_faculty')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('department', models.ForeignKey(orm[u'registration.department'], null=False)),
            ('faculty', models.ForeignKey(orm[u'registration.faculty'], null=False))
        ))
        db.create_unique(m2m_table_name, ['department_id', 'faculty_id'])

        # Adding model 'Location'
        db.create_table(u'registration_location', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('building', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('room', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('equipment', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('capacity', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'registration', ['Location'])

        # Adding model 'Course'
        db.create_table(u'registration_course', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('credit', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('ta_requirement', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'registration', ['Course'])

        # Adding model 'TimeSlot'
        db.create_table(u'registration_timeslot', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('day', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('time', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal(u'registration', ['TimeSlot'])

        # Adding model 'Section'
        db.create_table(u'registration_section', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('course', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['registration.Course'])),
            ('number', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('location', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['registration.Location'])),
            ('max_enrollment', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('faculty', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['registration.Faculty'])),
            ('teaching_assistant', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['registration.TeachingAssistant'])),
        ))
        db.send_create_signal(u'registration', ['Section'])

        # Adding M2M table for field time_slot on 'Section'
        m2m_table_name = db.shorten_name(u'registration_section_time_slot')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('section', models.ForeignKey(orm[u'registration.section'], null=False)),
            ('timeslot', models.ForeignKey(orm[u'registration.timeslot'], null=False))
        ))
        db.create_unique(m2m_table_name, ['section_id', 'timeslot_id'])

        # Adding M2M table for field student on 'Section'
        m2m_table_name = db.shorten_name(u'registration_section_student')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('section', models.ForeignKey(orm[u'registration.section'], null=False)),
            ('student', models.ForeignKey(orm[u'registration.student'], null=False))
        ))
        db.create_unique(m2m_table_name, ['section_id', 'student_id'])


    def backwards(self, orm):
        # Deleting model 'Student'
        db.delete_table(u'registration_student')

        # Deleting model 'Staff'
        db.delete_table(u'registration_staff')

        # Deleting model 'Faculty'
        db.delete_table(u'registration_faculty')

        # Deleting model 'TeachingAssistantStatus'
        db.delete_table(u'registration_teachingassistantstatus')

        # Deleting model 'TeachingAssistant'
        db.delete_table(u'registration_teachingassistant')

        # Deleting model 'Department'
        db.delete_table(u'registration_department')

        # Removing M2M table for field faculty on 'Department'
        db.delete_table(db.shorten_name(u'registration_department_faculty'))

        # Deleting model 'Location'
        db.delete_table(u'registration_location')

        # Deleting model 'Course'
        db.delete_table(u'registration_course')

        # Deleting model 'TimeSlot'
        db.delete_table(u'registration_timeslot')

        # Deleting model 'Section'
        db.delete_table(u'registration_section')

        # Removing M2M table for field time_slot on 'Section'
        db.delete_table(db.shorten_name(u'registration_section_time_slot'))

        # Removing M2M table for field student on 'Section'
        db.delete_table(db.shorten_name(u'registration_section_student'))


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
            'chairperson': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': u"orm['registration.Faculty']"}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'faculty': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['registration.Faculty']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50'})
        },
        u'registration.faculty': {
            'Meta': {'object_name': 'Faculty'},
            'course_load': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rank': ('django.db.models.fields.CharField', [], {'default': "'Jr.'", 'max_length': '50'}),
            'staff': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['registration.Staff']"})
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
            'faculty': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['registration.Faculty']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['registration.Location']"}),
            'max_enrollment': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'number': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'student': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['registration.Student']", 'symmetrical': 'False'}),
            'teaching_assistant': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['registration.TeachingAssistant']"}),
            'time_slot': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['registration.TimeSlot']", 'symmetrical': 'False'})
        },
        u'registration.staff': {
            'Meta': {'object_name': 'Staff'},
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
            'staff': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['registration.Staff']"}),
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