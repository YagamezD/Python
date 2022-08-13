
from flask import Flask
from flask import render_template , redirect, session, request

app = Flask(__name__) 
app.secret_key = 'shshshs'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def tablas():
    
    session['first_name'] = request.form['first_name']
    session['last_name'] = request.form['last_name']
    session['email'] = request.form['email']
    session['dojos'] = request.form['dojos']
    session['lenguajes'] = request.form['lenguajes']
    session['juegos'] = request.form['juegos']
    session['comments'] = request.form['comments']
    
    return redirect('/results')

@app.route('/results')
def show():
    return render_template('results.html')




if __name__=="__main__":
    app.run(debug=True)   
    