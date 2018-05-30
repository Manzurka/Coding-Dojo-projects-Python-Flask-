from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def root():
    return render_template("index.html")

@app.route('/ninja')
def ninja():
    return render_template("ninjas.html")

@app.route('/ninja/<color>')
def show_ninja(color):
    if color == "blue":
        return render_template("ninjablue.html")
    elif color == "red":
        return render_template("ninjared.html")
    elif color == "orange":
        return render_template("ninjaorange.html")
    elif color == "purple":
        return render_template("ninjapurple.html")
    else:
        return render_template("ninjanone.html")

app.run(debug=True)