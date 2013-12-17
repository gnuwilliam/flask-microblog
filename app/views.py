from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = { 'nickname': 'William' }
    posts = [
        {
            'author': { 'nickname': 'John' },
            'body': 'Yay, posting on Flask'
        }
    ]
    
    return render_template('index.html',
                           title = 'Home',
                           user = user)