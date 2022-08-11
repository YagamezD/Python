from flask_app.config.mysqlconnection import connectToMySQL
from .ninjas import Ninja

class Dojo: 
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []        

    @classmethod  
    def save(cls,formulario):
        query = "INSERT INTO dojos (name) VALUES (%(name)s)"
        result = connectToMySQL('dojos_ninjas').query_db(query,formulario)
        return result
    
    @classmethod
    def show_dojos(cls):
        query = 'SELECT * FROM dojos'
        results = connectToMySQL('dojos_ninjas').query_db(query)
        dojos = []
        for d in results:
            instancia_dojo = cls(d) #User()
            dojos.append(instancia_dojo)
        return dojos 
    
    @classmethod 
    def all_dojo_ninjas(cls, data):
        
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojos_id WHERE dojos.id = %(id)s"
        result = connectToMySQL('dojos_ninjas').query_db(query,data)
        dojo = cls(result[0])
        for row in result:
            n = {
                'id' : row['ninjas.id'],
                'first_name': row['first_name'],
                'last_name': row['last_name'],
                'age': row['age'],
                'created_at': row['ninjas.created_at'],
                'updated_at' : row['ninjas.updated_at']
                }
            instancia_ninja = Ninja(n)
            dojo.ninjas.append(instancia_ninja)
        return dojo
    
        