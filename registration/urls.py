from django.conf.urls import patterns, url

from registration import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    # url(r'^(?P<student_id>\d+)/studentregistration/$', views.studentregistration, name='studentregistration'),
)
