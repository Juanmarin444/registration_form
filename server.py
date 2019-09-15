from flask import Flask, render_template, redirect, request, session, flash
import re
from datetime import datetime

EMAIL_REGEX = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")

app = Flask(__name__)

app.secret_key = "This is secret"

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def validations():
    password1 = request.form['password1']

    present = datetime.now()

    if len(request.form['bday']) == 0:
        print(len(request.form['bday']),'TEXASTEXASTEXAS')
        year = 9999
        month = 99
        day = 99
    else:
        print(len(request.form['bday']),'LKSDJFLSKDJFLSKDFJ')
        year,month,day= request.form['bday'].split('-')

    # year,month,day= request.form['bday'].split('-')
    print(year,month,day,"THIS IS THE ONE")
   
    if len(request.form['first_name']) < 1:
        flash(u"First name cannot be blank.",'error')

    elif len(request.form['last_name']) < 1:
        flash(u"Last name cannot be blank.", 'error')
    
    elif int(year) > present.year:
        flash(u'Must include a valid Birth Date.', 'error')
        print(year, 'AHHHHH')

    elif int(month) > present.month and int(year) == present.year:
        flash(u'Must include a valid Birth Date.', 'error')
        print(month, 'DDAAAHHH')

    elif int(day) > present.day and int(year) == present.year and int(month) == present.month:
        flash(u'Must include a valid Birth Date.', 'error')
        print(day,'SAAHHHH')

    elif len(request.form['email']) < 1:
        flash(u"Email cannot be blank.", 'error')

    elif not EMAIL_REGEX.match(request.form['email']):
        flash(u"Invalid email address.", 'error')

    elif len(password1) < 1:
        flash(u"Password cannot be empty.", 'error')

    elif not any(x.isupper() for x in password1):
        flash(u'Password must contain at least one upper case letter.', 'error')

    elif not any(x.islower() for x in password1):
        flash(u'Password must contain at least one lower case letter.', 'error')

    elif not any(x.isdigit() for x in password1):
        flash(u'Password must contain at least one digit.', 'error')

    elif len(password1) < 8:
        flash(u'Password must contain at least 8 characters.', 'error')

    elif password1 != request.form['password2']:
        flash(u"Passwords do not match.", 'error')

    else:
        flash("Thank you for submitting your information")

    return redirect('/')


app.run(debug=True)
