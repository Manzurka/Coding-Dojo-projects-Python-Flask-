from flask import Flask, request, redirect, render_template, flash, session
from mysqlconnection import MySQLConnector

import md5

import re 
NAME_REGEX = re.compile(r"[a-zA-Z]")
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app = Flask(__name__)
mysql = MySQLConnector(app,'login_registrationdb')
app.secret_key = "TopSecret!"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def createUser():
    if len(request.form['first_name']) < 2:
        flash("First Name cannot be less than 2 characters!")
        return redirect('/')
    elif not NAME_REGEX.match(request.form['first_name']):
        flash("First Name cannot contain numbers!")
        return redirect('/') 
    elif len(request.form['last_name']) < 2:
        flash("Last name cannot be less than 2 characters!")
        return redirect('/')
    elif not NAME_REGEX.match(request.form['last_name']):
        flash("Last Name cannot contain numbers!")
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
        hashed_password = md5.new(request.form['password']).hexdigest()
        query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (:first_name, :last_name, :email, :password, NOW(), NOW())"

        data = {
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'email': request.form['email'],
            'password': hashed_password
        }
        mysql.query_db(query, data)
        flash("Thank you for registering! Please log in below!")
        return redirect('/')

@app.route('/success', methods=['POST'])
def login():
    if not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!")
        return redirect('/')
    elif len(request.form['password']) < 8:
        flash("Password should be 8 characters!")
        return redirect('/')
    else:
        user_email = request.form['email']
        hashed_password = md5.new(request.form['password']).hexdigest()
        query = "SELECT * FROM users WHERE email = :user_email"
        data = {
        'user_email': request.form['email']
        }
        users = mysql.query_db(query,data)
        if hashed_password == users[0]['password']:  
            session['user_id'] = users[0]['id']
            print  session['user_id']
            return render_template('success.html', name=users[0]['first_name'])
        else: 
            flash("Password doesnot match!")
            return redirect('/')
app.run(debug=True)