# 1) password hashing in implemented in models.py (converts passwords into long encoded sequences)
# 2) pip install flask-login (initialized in init.py)
# 3) prepare the user model for flask login, the flask extention has 4 required items (authenticated, active, anonymous, get_id) incorperated with mixin
# 4) Preparing loader function (flask login keeps track of logged in users by storing their unique userid in the user session ) models.py
# 5) logged in users changes routes.py
# 6) logout function
# 7) Requring users to login
# 8) Registering users forms.py conatins email validator, equal to password check