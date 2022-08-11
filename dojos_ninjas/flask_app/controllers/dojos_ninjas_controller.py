
from flask import render_template, redirect, request
from flask_app import app 
from flask_app.models.dojos import Dojo
from flask_app.models.ninjas import Ninja

@app.route('/')
def index():
    return redirect('/dojos')

@app.route('/dojos')
def dojos():
    all_dojos = Dojo.show_dojos()
    return render_template('index.html', all_dojos=all_dojos)

@app.route('/create/dojo', methods=['POST'])
def create_dojo():
    #request.form = {name:'Colombia'}
    Dojo.save(request.form)
    return redirect('/dojos')

@app.route('/new/ninja')
def new_ninja():
    all_dojos = Dojo.show_dojos()
    return render_template('new.html', all_dojos=all_dojos)

@app.route('/create/ninja', methods=['POST'])
def create_ninja():
    Ninja.saven(request.form)
    return redirect('/dojos')


@app.route('/dojo/<int:id>')
def all_dojos(id):
    data = {
        'id': id
    }
    dojo = Dojo.all_dojo_ninjas(data)
    return render_template('dojo.html', dojo=dojo)