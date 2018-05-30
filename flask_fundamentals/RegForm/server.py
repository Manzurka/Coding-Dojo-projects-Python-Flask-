from flask import Flask,render_template, request, redirect, session, flash
import re 
NAME_REGEX = re.compile(r"[a-zA-Z]")
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app = Flask(__name__)
app.secret_key = "Secret!"

@app.route('/')
def root():
    return render_template ('index.html')

@app.route('/submit', methods=['POST']  )
def submit():
    if len(request.form['firstName']) < 1:
        flash("First Name field cannot be empty!")
        return redirect('/')
    elif not NAME_REGEX.match(request.form['firstName']):
        flash("Please enter your first name correctly!")
        return redirect('/') 
    elif len(request.form['lastName']) < 1:
        flash("Last name field cannot be empty!")
        return redirect('/')
    elif not NAME_REGEX.match(request.form['lastName']):
        flash("Please enter your last name correctly!")
        return redirect('/')
    elif len(request.form['email']) < 1:
        flash("Email field cannot be empty!")
        return redirect('/')
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!")
        return redirect('/')
    elif len(request.form['password']) < 8:
        flash("Password should be 8 characters!")
        return redirect('/')
    elif request.form['pw_confirmation']!=request.form['password']:
        flash("Password should match!")
        return redirect('/')
    else:
        flash("Success!")
        return redirect('/')

app.run(debug=True)