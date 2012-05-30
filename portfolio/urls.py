from django.conf.urls.defaults import patterns, include, url
from portfolio.artifact.views import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'portfolio.views.home', name='home'),
    # url(r'^portfolio/', include('portfolio.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^$', 'artifact.views.front', name='front'),
    url(r'^(?P<catid>\d+)/$', 'artifact.views.cat', name='cat'),
    url(r'^admin/', include(admin.site.urls)),
)
