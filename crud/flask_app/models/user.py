from flask_app.config.mysqlconnection import connectToMySQL

class User:
    def __init__(self, data):
        self.Id = data['Id']
        self.First_name = data['First_name']
        self.Last_name = data['Last_name']
        self.Email = data['Email']
        self.Created_at = data['Created_at']
        self.Update_at = data['Update_at']

    @classmethod
    def guardar(cls, formulario):

        query = "INSERT INTO usuarios (First_name, Last_name, Email) VALUES (%(First_name)s, %(Last_name)s, %(Email)s)"
        result = connectToMySQL('crud').query_db(query, formulario)
        return result
    
    @classmethod
    def muestra_usuarios(cls):
        query = 'SELECT * FROM usuarios'
        results = connectToMySQL('crud').query_db(query)
        usuarios = []
        for u in results:
            instancia_usuario = cls(u) #User()
            usuarios.append(instancia_usuario)
        return usuarios
    
    @classmethod
    def borrar(cls, formulario):
        query = "DELETE FROM usuarios WHERE Id = %(Id)s"
        result = connectToMySQL('crud').query_db(query, formulario)
        return result
    
    @classmethod
    def actualizar(cls, formulario):
        query = "UPDATE usuarios SET First_name = %(First_name)s,  Last_name = %(Last_name)s, Email = %(Email)s  WHERE Id = %(Id)s;"
        return connectToMySQL('crud').query_db(query, formulario)
        
        
    @classmethod
    def buscar_usuario(cls, formulario):
        query = "SELECT * FROM usuarios WHERE Id = %(Id)s"
        result = connectToMySQL('crud').query_db(query,formulario)
        print(result)
        return cls(result[0])