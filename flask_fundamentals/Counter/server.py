from flask import Flask, render_template,request, redirect, session
app = Flask(__name__)
app.secret_key="SecretKey"
app.count=0


@app.route ('/')
def root():
    if 'count' in session:
        session['count']+=1
    else: 
        session['count'] =1
        return render_template('index.html',count=session['count'])

@app.route ('/plustwo')
def plustwo():
    session['count'] += 2
    return render_template('index.html',count=session['count'])

@app.route ('/zero')
def zero():
    session['count'] = 0
    return render_template('index.html',count=session['count'])

app.run(debug=True)


