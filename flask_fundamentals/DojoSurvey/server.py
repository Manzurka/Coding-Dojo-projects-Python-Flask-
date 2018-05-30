from flask import Flask,render_template, request, redirect, session, flash
# import re 
# name_check = re.compile(r"[a-zA-Z]")

app = Flask(__name__)
app.secret_key = "ThisIsSecret!"

@app.route('/')
def root():
    return render_template ('index.html')

@app.route('/result', methods=['POST']  )
def result():
    name=request.form['name']
    location=request.form['dojolocation']
    language=request.form['favoriteLanguage']
    comment=request.form['comment']
    if len(request.form['name']) < 1:
        flash("Name field cannot be empty!")
        return redirect('/')
    # elif not name_check.match(request.form['name']):
    #     flash("Please enter your name correctly!")
    #     return redirect('/')
    elif len(request.form['comment']) < 1:
        flash("Comment field cannot be empty!")
        return redirect('/')
    elif len(request.form['comment']) > 120:
        flash("Comment is more than 120 characters!")
        return redirect('/')
    else:
        return render_template ('result.html', name=name, location=location, language=language, comment=comment)

app.run(debug=True)