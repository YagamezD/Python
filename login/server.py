#EJECUTA NUESTRA APLICACION 
from distutils.log import debug
from flask_app import app 

#Importando mi controlador  

from flask_app.controllers import users_controller

if __name__ == "__main__":
    app.run(debug=True)