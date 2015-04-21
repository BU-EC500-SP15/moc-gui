from django.conf.urls import patterns, include, url
from django.contrib import admin
from views import *

##Template Rendering and querying state
urlpatterns = patterns('',
    # front page
    url(r'^$', front_page),
    # cloud splash
    url(r'^clouds', clouds),
    # marketplace
    url(r'^market/(?P<project>.+)/$', market),
    # # sidebar
    url(r'^market/(?P<project>.+)/(?P<ftext>.+)$', market),
)
##Form Processing
urlpatterns += patterns('',
    # user management 
    url(r'^login', login),
    url(r'^register', register),
    url(r'^logout', logout),
    ## DB dusting
    url(r'^create/(?P<object_class>.+)', create_object),
    url(r'^delete/(?P<object_class>.+)', delete_object),
    # projects control
#    url(r'^createProject', createProject),
#    url(r'^deleteProject', deleteProject),
#    # cluster control
#    url(r'^createClusterAccount', createClusterAccount),
#    url(r'^deleteClusterAccount', deleteClusterAccount),
#    url(r'^createOSProject', createOSProject),
#    url(r'^deleteOSProject', deleteOSProject),
#    # vm control 
#    url(r'^createVM', createVM),
#    url(r'^deleteVM', deleteVM),
#    url(r'^controlVM', controlVM),
)
