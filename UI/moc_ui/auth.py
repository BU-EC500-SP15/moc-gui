from os import environ as env
import novaclient.v1_1.client as nvclient
import glanceclient.v2.client as glclient
import keystoneclient.v2_0.client as ksclient

# New Login

from keystoneclient.auth.identity import v2
from keystoneclient import session
from novaclient import client

# Socks Stuff

import socks
import socket

# Set up SOCKS proxy usage:

s = socks.socksocket()
socks.set_default_proxy(socks.SOCKS5, 'localhost', 5678) # Change the port here!
socket.socket = socks.socksocket


# def loginUser(username, password, request):
#         """
# 	Create keystone client for user; called on login
# 	"""
# 	print 'lucas-test-auth-loginUser'
	
#         keystone = ksclient.Client(
# 	        auth_url = 'http://140.247.152.207:5000/v2.0',
# 		username = username,
#        		password = password)
#     	print 'lucas-test-auth-loginUser-succesfully'
# 	return keystone


def _loginTenant (request, username, password, tenant_name):
	auth_url = 'http://140.247.152.207:5000/v2.0'
	auth = v2.Password(auth_url = auth_url, username = username, password = password, tenant_name = tenant_name)
	sess = session.Session(auth=auth)
	nova = client.Client('1.1', session=sess)

	request.session['nova'] = nova


def loginTenant(request, tenant_name):
	"""
	Create keystone, nova, and glance clients for tenant; on tenant selection
	"""

	username = request.session['username']
	password = request.session['password']

	print 'lucas-test-auth-loginTenant'
	keystone = ksclient.Client(auth_url = 'http://140.247.152.207:5000/v2.0', username = username,
		password = password, tenant_name = tenant_name)
	print 'lucas-test-auth-loginTenant-succesfully'
	nova = nvclient.Client(auth_url = 'http://140.247.152.207:5000/v2.0',
		username = username,
		api_key = password,
		project_id = tenant_name)
	glance_endpoint = keystone.service_catalog.url_for(service_type='image')
	glance = glclient.Client(glance_endpoint, token = keystone.auth_token)
	return {'keystone': keystone, 'nova': nova, 'glance': glance}

def get_keystone(request, tenant_name):
	username = request.session['username']
	password = request.session['password']
	keystone = ksclient.Client(auth_url = 'http://140.247.152.207:5000/v2.0', username = username,
		password = password, tenant_name = tenant_name)
	return keystone

def get_nova(request, tenant_name):
	username = request.session['username']
	password = request.session['password']
	nova = nvclient.Client(auth_url = 'http://140.247.152.207:5000/v2.0',
		username = username,
		api_key = password,
		project_id = tenant_name)
	return nova

def get_glance(request, tenant_name):
	username = request.session['username']
	password = request.session['password']
	glance_endpoint = keystone.service_catalog.url_for(service_type='image')
	glance = glclient.Client(glance_endpoint, token = keystone.auth_token)
	return {'keystone': keystone, 'nova': nova, 'glance': glance}
	

#return keystone, nova, glance


##### OUTDATED SECTION - USEFUL FOR TESTING
# admin keystone auth
#keystone = ksclient.Client(token='admin', endpoint='http://10.0.2.15:35357/v2.0')

#keystoneImages = ksclient.Client(auth_url=env['OS_AUTH_URL'],
#username=env['OS_USERNAME'],
#password=env['OS_PASSWORD'],
#tenant_name=env['OS_TENANT_NAME'],
#region_name=env['OS_REGION_NAME'])

#glance_endpoint = keystoneImages.service_catalog.url_for(service_type='image')
#glance = glclient.Client(glance_endpoint, token=keystoneImages.auth_token)

#nova = nvclient.Client(auth_url=env['OS_AUTH_URL'],
#username=env['OS_USERNAME'],
#api_key=env['OS_PASSWORD'],
#project_id=env['OS_TENANT_NAME'],
#region_name=env['OS_REGION_NAME'])
#####


