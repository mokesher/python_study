from flask import Flask,url_for
app = Flask(__name__)

@app.route('/')
def index():
    return 'hello world'
@app.route('/login')
def login():
    pass

@app.route('/user/<username>')
def profile(username):
    return 'user %s'% username

with app.test_request_context():
    print (url_for('index'))
    print (url_for('login'))
    print (url_for('login',next='/'))
    print (url_for('profile',username='moke'))
    
if __name__ =='__main__':
    app.run()
