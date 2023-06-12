Localisation!!
install and initialise flask-babel
configure disered languages in config.py
Babel instance provides a localeselector which is invoked for each request to select a language translation
Mark text to translate using _() convention 
some harder than other because there are form fields involved so flask-babel provides lazy_gettext():
Once text is marked pybabel extracts them to a portable object template which is stroage for text that needs to translated babel.cfg
