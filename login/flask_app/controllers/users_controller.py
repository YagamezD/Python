
from flask import render_template, redirect, session, request, flash
from flask_app import app 


#Importacion del modelo
from flask_app.models.users import User

#Importacion BCrypty 
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/registrate', methods=['POST'])
def registrate():
    #Validar la informacion ingresada
    if not User.valida_usuario(request.form):
        return redirect('/')
    
    pwd = bcrypt.generate_password_hash(request.form['password']) #Encriptamos el password del usuario
    formulario = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'password': pwd
    }
    #request.form = FORMULARIO HTML 
    id = User.save(formulario) #RECIBO ID DE MI NUEVO USUARIO
    session['user_id'] = id
    return redirect('/dashboard')

    
@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/')
    
    formulario = {
        'id': session['user_id']
    }
    user = User.get_by_id(formulario)
    return render_template('dashboard.html', user=user)

    

@app.route('/login', methods=['POST'])
def login():
#Verificar que el email exista
#request.form RECIBIMOS DE HTML 
    user = User.get_by_email(request.form) #Recibiendo una instancia de usuario o Falso 
    if not user: 
        flash('E.mail no encontrado', 'login')
        return redirect('/')

    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash('Password incorrecto', 'login')
        return('/')
    
    session['user_id'] = user.id
    return redirect('/dashboard')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')


