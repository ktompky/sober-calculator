from app import app
from flask import render_template,flash, redirect
from app.forms import DateForm

@app.route('/')
def index():
    return render_template('index.html', title="Welcome")

@app.route('/sobriety_date', methods=['GET','POST'])
def get_date():
    form = DateForm()
    if form.validate_on_submit():
        flash("Username is {}, date selected is {}".format(form.username.data, form.date.data))
        return  redirect('/answer')
    return render_template('sobriety_date.html', title="Get Sobriety Date", form=form)

@app.route('/answer', methods =['GET', 'POST'])
def show_date():

    return render_template('')