from flask import Flask
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'


@app.route('/home')
def home():
    return 'Home'

@app.route('/about')
def about():
    return 'The About Page'

