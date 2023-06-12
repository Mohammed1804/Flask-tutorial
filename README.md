1)Create a blueprint package this helps to encapsulate a componant of the application, in this situation error messages
three parts to blueprints, blueprint package (storage for componants), blueprint creation (initialisation of BP)and BP registration to be registered (in the init.py file)
4)same for auth
5)same for main
note that app.route -> bp.route / url_for() -> url_for(auth.login) 
6)change application from global variable for testing functions purposes this is done displacing app w/ current ap

