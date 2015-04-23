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
    # Add & Remove are placeholders at the moment. I think we shouldn't have in particular add and remove, but a
    # Sort of toggle function. Like toggle_service and toggle_default. Just add and remove in the regex with whatever
    # function name you want to pass to the view. 
    url(r'^(?!.+add\/?$|.+remove\/?$)market\/(?P<project>.+)?\/$', market),
    # Market Place filtering functionality:
    #url(r'^market\/(?P<project>.+)\/(?P<filter>.+)\/?$', market),
    url(r'^(?!.+add\/?$|.+remove\/?$)market\/(?P<project>.+)?\/(?P<filter>.+)\/?$', market),
    # Tells the view to perform an action on a service. 
    url(r'^market\/(?P<project>.+)\/(?P<service>.+)\/(?P<action>.+)\/?$', market),
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
