from app import app
from flask import render_template
from app.forms import LoginForm

@app.route('/')

@app.route('/hello')
def hello():
    return render_template('hello.html')

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title="Sign in", form=form)