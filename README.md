#moc-gui
Extending the MOC GUI

###Meetings Briefs 

#####Meeting on 4/2 with Jon Bell:


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

* State DB - checking users, endpoints, session info
* With a State DB:
  * Improvement of Keystone client sessions
  * Currently inefficient
  * Some privilege workarounds may be solved using private keystone endpoint, port 353572 (instead of public 5000)
* Add error checking
* Implement OCX Library

#####Known Issues

* Refer to outstanding issues

#####FAQ

* Why does the UI not work anymore? 
  * Run ./rejoin**stack.sh

* Why does OpenStack send connection errors? 
  * You might need to rejoin or restack 

* Why does Django say port already in use when running server?
  * OpenStack may be using the port, either runserver first, or specify port (ie. python manage.py runserver 9999)

* How can I test the OpenStack python API efficiently??
  * Look at UI/marketUI/auth.py. Use the defined keystone, glance and nova clients via python command line (first run 'source ~/devstack/openrc')
