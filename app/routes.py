from app import app

@app.route('/')
@app.route('/index')
#@ is a decorator and can be registered as a callback function
def index():
    return "Testing new branch!"
