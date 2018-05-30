from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def root():
    return render_template ('index.html')

@app.route('/ninja')
def ninja():
    return render_template ('ninja.html')

@app.route('/dojos/new')
def dojos():
    return render_template ('dojos.html')
    
# @app.route('/dojos/new', methods=['POST'])
# def create_user():
#     # name = request.form['name']
#     # email = request.form['email']

#     return redirect('/dojos')

app.run(debug=True)