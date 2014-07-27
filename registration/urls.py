from django.conf.urls import patterns, url

from registration import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    # url(r'^(?P<student_id>\d+)/studentregistration/$', views.studentregistration, name='studentregistration'),
    url(r'^classes/$', views.class_list, name='class_list'),
    url(r'^departments/$', views.department_list, name='department_list'),
    url(r'^courses/(?P<department_id>\d+)$', views.course_list, name='course_list'),
    url(r'^sections/(?P<course_id>\d+)$', views.section_list, name='section_list'),
    url(r'^students/(?P<section_id>\d+)$', views.student_list, name='student_list'),
    url(r'^student/$', views.student_section, name='student_section'),
    url(r'^student/(?P<student_ssn>\d+)$', views.student_section, name='student_section'),
)
