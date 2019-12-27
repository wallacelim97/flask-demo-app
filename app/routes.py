from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username' : 'Wallace'}
    return '''
    <html>
        <head>
            <title>Home Page - Microblog</title>
        </head>
        <blog>
            <h1>Hello, ''' + user['username'] + '''</h1>
        </blog>
    </html>'''
