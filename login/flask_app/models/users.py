from unittest import result
from flask_app.config.mysqlconnection import connectToMySQL

import re #Importando Expresiones regulares
#EXPRESION REGULAR DE EMAIL 
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


from flask import flash

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
    @classmethod
    def save(cls, formulario):
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s)"
        result = connectToMySQL('login_reg').query_db(query, formulario)
        return result
        
    @staticmethod
    def valida_usuario(formulario):
        es_valido = True
            
        #Validar que el nombre tenga al menos 3 caracteres
        if len(formulario['first_name']) < 3:
            flash('Nombre debe de tener al menos 3 caracteres', 'registro')
            es_valido = False
                
        if len(formulario['last_name']) < 3:
            flash('Apellido debe de tener al menos 3 caracteres', 'registro')
            es_valido = False 
                
        #Verificar que el email tenga el formato correcto = EXPRESIONES REGULARES
        if not EMAIL_REGEX.match(formulario['email']):
            flash('E-mail Invalido', 'registro')
            es_valido = False
                
        #Password con al menos 6 caracteres 
        if len(formulario['password']) < 6:
            flash('Contraseña debe tener al menos 6 caracteres', 'registro')
            es_valido= False
                
        #Verificamos que las contraseñas coincidan 
        if formulario['password'] != formulario['confirm_password']:
            flash('Contraseñas no coinciden', 'registro')
            es_valido= False
            
        #Consultar si ya existe ese correo electronico 
        query = "SELECT * FROM users WHERE email = %(email)s"
        results = connectToMySQL('login_reg').query_db(query, formulario)
        if len(results) >= 1:
            flash('E-mail registrado previamente', 'registro')
            es_valido= False
                
        return es_valido
        
    
    @classmethod
    def get_by_email(cls, formulario):
        query = "SELECT * FROM users WHERE email = %(email)s"
        result = connectToMySQL('login_reg').query_db(query, formulario) #Los SELECT regresan una lista
        if len(result)< 1: #NO EXISTE REGISTRO CON ESE CORREO
            return False
        else:
            user = cls(result[0])
            return user
        
    @classmethod
    def get_by_id(cls, formulario):
        query = 'SELECT * FROM users WHERE id = %(id)s'
        result = connectToMySQL('login_reg').query_db(query, formulario)
        user = cls(result[0])
        return user