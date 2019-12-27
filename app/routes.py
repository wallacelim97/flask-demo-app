from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username' : 'Wallace'}
    posts = [
        {
            'author' : {'username' : 'John'},
            'body' : 'The weather is beautiful today!'
        },
        {
            'author' : {'username' : 'Mary'},
            'body' : 'I love my job!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
