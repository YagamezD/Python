#1 Actualizar valores en diccionarios y listas
x = [ [5,2,3], [10,8,9] ] 
estudiantes = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
directorio_deportes = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'fútbol' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

print("1.1 -----")
#1.1 Cambia el valor 10 en x a 15. Una vez que hayas terminado, x ahora debería ser [ [5,2,3], [15,8,9] ].
x[1] [0] = 15
print(x)
print("1.2 -----")
#1.2 Cambia el "apellido” del primer alumno de 'Jordan' a 'Bryant'.
estudiantes[0] ['last_name'] = 'Bryant'
print(estudiantes)
print("1.3 -----")
#1.3 En el directorio_deportes, cambia "Messi" por "Andrés".
directorio_deportes['fútbol'] [0] = 'Andres'
print(directorio_deportes) 
print("1.4 -----")
#1.4 Cambia el valor 20 en z a 30.
z[0]['y'] = 30
print(z)
# 2 Iterar a través de una lista de diccionarios
print("2 -----")
estudiantes = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]

def  iterateDictionary(estudiantes):
    for i in estudiantes:
        print("First Name - " + i['first_name'] + " -" + "Last Name - " + i['last_name'] )

res = (iterateDictionary(estudiantes))

# 3 Obtener valores de una lista de diccionarios
print("3 -----")
def iterateDictionary2(key_name, list):
    for n in list:
        print(n[key_name])

lastName = iterateDictionary2('last_name',estudiantes)

#4 Iterar a través de un diccionarios con valores de lista
dojo = {
'ubicaciones': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],

'instructores': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(diccionario):
    for key,value in diccionario.items():
        print("4 -----")
        print(f"{len(value),(key)} ")
        for i in range(0,len(value)):
            print(value[i])

printInfo(dojo)

