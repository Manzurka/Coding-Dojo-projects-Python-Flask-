from flask import Flask, render_template, request, redirect, session, Markup
app=Flask(__name__)
app.secret_key='Monkey'

import random
import datetime

@app.route('/') 
def root():
    session['gold'] =0
    session['activity'] = list()
    return render_template('index.html')

@app.route('/process_money', methods=['POST']) 
def process():
    if  request.form.get('building') == "farm":
        winnings=random.randrange(10,20)
        session['gold']+=winnings
        session['activity'].append("Earned "+str(winnings)+" golds from the farm!  "+'{:%Y/%m/%d %I:%M %p}'.format(datetime.datetime.now()))

    elif request.form.get('building') == "cave":
        winnings=random.randrange(5,10)
        session['gold']+=winnings
        session['activity'].append("Earned "+str(winnings)+" golds from the cave!  "+'{:%Y/%m/%d %I:%M %p}'.format(datetime.datetime.now()))

    elif request.form.get('building') == "house":
        winnings=random.randrange(2,5)
        session['gold']+=winnings
        session['activity'].append("Earned "+str(winnings)+" golds from the house!  "+'{:%Y/%m/%d %I:%M %p}'.format(datetime.datetime.now())) 

    elif request.form.get('building') == "casino":
        money=random.randrange(-50,50)

        if (money>0):
            session['gold']+=money
            session['activity'].append("Earned "+str(money)+" golds from the casino!  "+'{:%Y/%m/%d %I:%M %p}'.format(datetime.datetime.now()))
        else:
            session['gold']-=abs(money)
            session['activity'].append("Lost "+str(abs(money))+" golds from the casino!  "+'{:%Y/%m/%d %I:%M %p}'.format(datetime.datetime.now()))
   
    return render_template('index.html', activity=session['activity'])

app.run(debug=True)