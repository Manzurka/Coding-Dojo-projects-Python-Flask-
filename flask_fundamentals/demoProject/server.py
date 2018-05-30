from flask import Flask,render_template # from VirtEnv import stuff
app = Flask(__name__) # builds new Flask app

@app.route('/') #decorator - syntax to set up route
def index():  # initial route
    return render_template ('index.html')

@app.route('/books') 
def books():  
    return render_template ('books.html')

app.run(debug=True) #start app, debugging is available
