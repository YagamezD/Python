from flask_app import app
from flask import render_template, request, redirect
from flask_app.models.user import User


@app.route('/')
def index():
    usuarios = User.muestra_usuarios()
    return render_template('index.html', usuarios=usuarios)

@app.route('/new')
def new():
    return render_template('new.html')

@app.route('/create', methods=['POST'])
def create():
    User.guardar(request.form)
    return redirect('/')

@app.route('/delete/<int:Id>')
def delete(Id):
    formulario = {'Id': Id}
    User.borrar(formulario)
    return redirect('/')

@app.route('/edit/<int:Id>')
def edit(Id):
    data = {
        'Id': Id
        }
    user = User.buscar_usuario(data)
    print(user)
    return render_template('edit.html', usuarios=user)
        
    
@app.route('/update', methods=['POST'])
def update():
    User.actualizar(request.form)
    return redirect('/')
