from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
    
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
        
    @classmethod
    def saven(cls, formulario):
        query = 'INSERT INTO ninjas (first_name, last_name, age, dojos_id) VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojos_id)s)'
        result = connectToMySQL('dojos_ninjas').query_db(query, formulario)
        return result 
    
    