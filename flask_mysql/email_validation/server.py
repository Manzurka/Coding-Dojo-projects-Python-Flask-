from flask import Flask, request, redirect, render_template, flash, session
from mysqlconnection import MySQLConnector

import re 
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app = Flask(__name__)
mysql = MySQLConnector(app,'emailsdb')
app.secret_key = "Secret!"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/emails', methods=['POST'])
def create():
    if not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!")
        return redirect('/')
    else:
        flash("The Email Address you entered " + request.form['email'] + " is a valid email address! Thank you!")
        print request.form['email']
        query = "INSERT INTO emails (email, created_at ) VALUES (:email, NOW())"

        data = {
            'email': request.form['email']
        }
        mysql.query_db(query, data)
        
        return redirect('/success')
@app.route('/success')
def add():
    query = "SELECT * FROM emails"  
    emails = mysql.query_db(query) 
    return render_template('success.html', all_emails=emails)

@app.route('/delete', methods=['POST'])
def delete():
    query = "DELETE FROM emails WHERE email = :email"
    data = {'email': request.form['email']}
    mysql.query_db(query, data)
    return redirect('/success')
app.run(debug=True)