from app import app
from flask import render_template,flash, redirect, request
from app.forms import DateForm
import datetime
from dateutil import relativedelta


@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500

@app.route('/')
def index():
    return render_template('index.html', title="Welcome")

@app.route('/about')
def get_about():
    return render_template('about.html', title="About the page")

@app.route('/sobriety_date', methods=['GET'])
def get_date():
    form = DateForm()
 
    if form.validate_on_submit():
        #flash("Username is {}, date selected is {}".format(form.username.data, form.date.data))
        return  redirect('/sobriety_date')
    return render_template('sobriety_date.html', title="Get Sobriety Date", form=form)

@app.route('/sobriety_date_results', methods =['POST'])
def show_date():
    username = request.form['username']
    date = request.form['date']
    year, month, day = map(int, date.split('-'))
    date1 = datetime.date(year, month, day)

    today = datetime.date.today()
    #diff = (today - date1)
    diff = relativedelta.relativedelta(today,date1)

    years = diff.years
    months = diff.months
    days = diff.days
    
    return render_template('sobriety_date_results.html', title ="Your Results", username=username, years=years, months=months, days=days)

   