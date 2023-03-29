from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
#methods argument acccepts post and get requests as opposed to just get
def login():
    form = LoginForm()
    if form.validate_on_submit():
#processes form work, when browser tries to send get request it returns false/post reuquest comes back as true
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    #if statements are true able to navigate different pages
    return render_template('login.html',  title='Sign In', form=form)
