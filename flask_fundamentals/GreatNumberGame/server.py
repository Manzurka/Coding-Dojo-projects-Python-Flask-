from flask import Flask, render_template,request,redirect, session
app = Flask(__name__)
app.secret_key="Key"

import random

@app.route('/')
def root():
    if 'randomNum' not in session: #so it is not generating random number again when the page reloads
        session ['randomNum']=random.randrange(0,101) #random.randint(1,100)
        print session ['randomNum']
        return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    number=request.form['number']
    session ['number']=number
    print  session ['number'] 
    return render_template('index.html', number=int(session ['number']), randomNum= int(session ['randomNum']))
    # if int(request.form['number']) == session['randomNum']:
    #     print "got it right"
        # session["outcome"]='correct'
    # elif int(request.form['number']) < session['randomNum']:
    #     print "too low"
        # session["outcome"]='low'
    # else:
    #     print "too high"
        # session["outcome"]='high'
    # return redirect ('/')

@app.route('/reset')
def reset():
    # session.pop('randomNum')
    session.clear()
    return redirect('/')

app.run(debug=True)