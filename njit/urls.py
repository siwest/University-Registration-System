from django.conf.urls import patterns, include, url
from django.contrib import admin
from registration import views
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', views.index, name="index"),
    url(r'^registration/', include('registration.urls')),
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^studentregistration/', include('studentregistration.urls')),
)
