# Forms to use in pages
import forms
# Dictionaries to pass to template context
import dicts
# Models to access our db's tables
import models


#currently retrieves a models.user object from the Django Models database
#instead needs to return a Keystone token
def retrieveUser(userName):
    try:
        return models.User.objects.get(name=userName)
    except: 
        return None 

def Retrieve_Object(Object, object_name):
    try:
        return models.Object.objects.get(name=object_name)
    except: 
        return None 

    
