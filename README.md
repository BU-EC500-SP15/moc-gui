#moc-gui
##Extending the MOC GUI

 A demo video made and edited by our own Alex Wong is here: (video link here pls)

###Instructions

####1. Prerequisites

To run this project we need to Python 2, Django 1.8, Pip, the OpenStack Python Clients, and PySocks

* Install Python 2 (https://www.python.org/downloads/)
* Install Django (https://docs.djangoproject.com/en/1.8/topics/install/)
* Install Pip (https://pip.pypa.io/en/latest/installing.html)
* Install the OpenStack Python Clients `pip install python-openstackclient`
* Install PySocks `pip install PySocks`

####2. Installing the UI

* Clone repo: git clone https://github.com/BU-EC500-SP15/moc-gui
* Run `./syncdb.sh`

####3. Connecting

* Go here and follow these instructions: (https://github.com/CCI-MOC/moc-public/wiki/EC500-Instructions)
* Make a proxy to connect to the Harvard Cluster. `ssh -D your_proxy_port_number your_username@140.247.152.200 -N`
  * for example, `ssh -D 5507 xuh@140.247.152.200 -N`
* You also need to change the port inside auth.py 

####4. Running the Server

* `./runserver.sh`
* It's ready! You can now point your browser to http://localhost:9000/

####5. Interface Usage

* Login Page
  * login as an existing keystone user, or register with the ui, using their keystone crediential
* Project Page
  * enter a project and this page lists all projects with which the user is associated 
* Control Page (Project Management)
  * create/edit/delete VMs
  * access to marketplace page
* Marketplace Page
  * add/cancel services 

**Limitations**
* User's password is saved as plain-text in our database. 
* The various openstack clients are spun up everytime they are needed. Which is wildly inefficient. 
* Can only create default VMs. Cannot create custom VMs 

####Meetings Briefs 

Jon, as our mentor, has been really helpful to our project and we really appreicate it. 

#####Other meettings:

* New Control of Flow
* Keystone integration
* ...

#####Meeting on 3/31 with Jon Bell:
* Starting making the market page in a generic way
* Getting familiar with new view.py and models.py 


#####Meetings before the Second Demo with Jon Bell:
* Start using new UI created by our mentors
* Start implementing the marketplace page
* Burndown Trello cards and create new cards for future sprint


#####Meeting on 3/3 with Jon Bell:
* Fixed bugs with user registration
* Added remove user from tenant button on the project page
* Discussed future plans of the project

#####Meeting on 3/1 with Jon Bell:
* Fixed bugs with user registration
* Fixed the contents is not responding with clicking on sidebar on marketplace page
* Be able to login as admin to UI
* Discussed the demo on next Thursday

#####Meeting on 2/24 with Jon Bell:
* Get familiar with all templates we have so far
* Fixed problems of setting up devstack on our own laptops

#####Meeting on 2/17 with Jon Bell:
* Using VM to setup linux env. and Setup the devstack env.
* Get familiar with Django
* Get familiar with work that previously done by the other students

#####Meeting on 2/11 with Jon Bell:
* Setup schedule planning with mentor
  * follow-up : decide to meet 2 times per week. one on weekdays and one on Sundays
* Get Familiar with the detail of the project
* Main task is to reconstruct the marketplace page

#####TODO

* Implement Glance functions/buttons. 
* Update the services fixture to more accurately reflect services available on the Harvard Cluster. 
* Implement the new VM (Customized Settings) form/button. 
* Make default VM button reflect choices made in the market place. 
* Deliberate how to connect to multiple OpenStack Clusters. (current proxy connection implementation is possibly global)
* Find a better way to keep keystone/nova/glance instances. 

#####Known Issues

* Refer to outstanding issues

#####FAQ

* Why am I getting proxy issues?
  * Rerun `ssh -D port_number your_username@140.247.152.200 -N` and make sure that auth.py points to the right port.

* Why can't I log in?
  * Register yourself as a user! Use the sign up button. Make sure your username and password accurately mirror your Harvard Cluster information!
  * You need to be registered to the Harvard Cluster! (https://github.com/CCI-MOC/moc-public/wiki/EC500-Instructions)
