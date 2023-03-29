Introduction of web forms to application
1) For web forms the flask extention Flask-WTF was used (installed using pip)
2)Configuration variables are defined next (kept seperate from application in config.py)
3)Configuration setting defined as a class variable
4)Secret key configuration is used a cryptographic key (for tokens) protects webforms against CSRF
5)With configuration file created flask reads it in init.py. Lower case is the name of python module and uppercase is the actual class
6)To create the userlogin form as new forms page is created (for seperation purposes) here flask-wtf uses python classes to represent webforms which converts the field into a form)
7)Form is added to a HTML template so it can be rendered on a webpage (novalidate is used to tell browser is field requires validation)
8)Before form can be seen in browser view functiin in routes must be updated
9)Form data can be filled but application cannot accept/read the data so routes must be updated
10)field validation is then improved, while the application shows the form in unsuccessful it does not show why and this is improved in login.html
