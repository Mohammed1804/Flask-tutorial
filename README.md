Databases
1)Flask does not support databases but flask support others in this case were using relational databases becasue the application is more structured 
2)pip ibstall flask-sqlalchemy
3)pip install flask-migrate - this is to make changes to the databases without having to update the whole thing
4)Need to make changes to the config - Flask-SQLAlchemy extension takes the location of the application's database from the SQLALCHEMY_DATABASE_URI
5)added db, migration script to init.py, and imported models which defines the database of the structure
6)models.py amended so that database models (username, email & password) included
7)__repr__ method tells Python how to print objects of this class, which is going to be useful for debugging
8)create fake user and run migration repo (flask db init)
9)flask db migrate -m "users table"
10)flask db upgrade/downgrade this updates info and downgrade reverses it 
11)database has users and posts, in posts there is a 'foreign key' knwon as user_id, this is linked to the id of the user so you can see which user posted what and vice-versa models.py
12)UTCnow function included for uniform timestamps
