from django.conf.urls import patterns, include, url
from django.contrib import admin
from moc_ui.views import *

urlpatterns = patterns('',
    # login 
    url(r'^login', login),
    url(r'^register', register),
    url(r'^logout', logout),
    # cluster
    url(r'^clusters', clusters),
    # projects
    url(r'^projects/enterProject', enterProject),
    url(r'^projects/create', createProject),
    url(r'^projects/', projects),
    # marketplace
    url(r'^project_space/market', market),
    # project settings
    url(r'^project_space/manage/settings/deleteProject/(?P<projectName>.+)', deleteProject),
    url(r'^project_space/manage/settings/addUser/(?P<projectName>.+)', addUser),
    url(r'^project_space/manage/settings/editRole', editRole),
    url(r'^project_space/manage/settings', settings),
    # project management
    url(r'^project_space/manage/delete/(?P<VMname>.+)', deleteVM),
    url(r'^project_space/manage/create/(?P<VMname>.+);(?P<imageName>.+);(?P<flavorName>.+)', createVM),
    url(r'^project_space/manage/create/(?P<VMname>.+)', createDefaultVM),
    url(r'^project_space/manage/edit/controlVM', editControlVM),
    url(r'^project_space/manage/edit', edit),
    url(r'^project_space/manage', manage),
    # default
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', front_page)
)
