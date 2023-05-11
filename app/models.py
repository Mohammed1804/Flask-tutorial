from datetime import datetime
from app import db, login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from hashlib import md5

followers = db.Table(
    'followers',
    db.Column('follower_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('followed_id', db.Integer, db.ForeignKey('user.id'))
)


# Generic statements for login (mixin)
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    about_me = db.Column(db.String(140)) #add two new fields to the database table
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)
    followed = db.relationship(
        'User', secondary=followers,
#db.relationship links User instances to User instances
#secondarry is association table
        primaryjoin=(followers.c.follower_id == id),
#links parernt class to other class with the association table (follower to following)
        secondaryjoin=(followers.c.followed_id == id),
#Links follwed to association table
        backref=db.backref('followers', lazy='dynamic'), lazy='dynamic')
#backref indicates how the followed links to followers
#lazy = execution mode for query
#dynamic sets up query not run until requested

    def avatar(self, size):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(
            digest, size)

    def __repr__(self):
        return '<User {}>'.format(self.username)
#password hashing logic
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
#both follow and unfollow use append/remove and is following is used so there are no duplicates in database
    def follow(self, user):
        if not self.is_following(user):
            self.followed.append(user)

    def unfollow(self, user):
        if self.is_following(user):
            self.followed.remove(user)

    def is_following(self, user):
        return self.followed.filter(
            followers.c.followed_id == user.id).count() > 0

#The join query in this instance creates an association table connecting posts and follwers to the posts
#Followed id = posts, database takes info from posts and attach it to the follwers table
#join operation gives a lisst of posts followed by some users but more than needed and this is sorted by filter
#filter only keeps in joined table that have follower_id so only info kept is from the person being followed
#results sorted by the timestamp field of the post in descending order.
    def followed_posts(self):
        followed = Post.query.join(
            followers, (followers.c.followed_id == Post.user_id)).filter(
                followers.c.follower_id == self.id)
        own = Post.query.filter_by(user_id=self.id)
        # user is able to see their own posts
        return followed.union(own).order_by(Post.timestamp.desc())

#tells flask-login to get unique identify to determain if user is logged in
@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)



