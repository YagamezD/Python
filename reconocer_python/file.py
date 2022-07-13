num1 = 42 #Declaracion de variable - dato tipo numero int 
num2 = 2.3 #Declaracion de variable - dato tipo numero float
boolean = True #Declaracion variable - dato tipo booleano
string = 'Hello World' #Declaracion variable - dato tipo String
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #Declaracion lista 
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #Declaracion diccioario 
fruit = ('blueberry', 'strawberry', 'banana') #Declaracio tupla
print(type(fruit)) #Comprobacion de tupla
print(pizza_toppings[1]) #Accediedo al elemento en la posicion 1(Sausage)
pizza_toppings.append('Mushrooms') #Agregando un nuevo elemento a la lista pizza_toppings
print(person['name']) #Accediendo al valor del elemento name en el diccionario person
person['name'] = 'George' #Modificando el valor del elemento name 
person['eye_color'] = 'blue' #Modificando el valor del elemento eye_color
print(fruit[2]) #Accediendo al elemento en la posicion 2(banana) de la tupla

if num1 > 45:
    print("It's greater")
else:
    print("It's lower")

if len(string) < 5:
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")

for x in range(5):
    print(x)
for x in range(2,5):
    print(x)
for x in range(2,10,3):
    print(x)
x = 0
while(x < 5):
    print(x)
    x += 1

pizza_toppings.pop()
pizza_toppings.pop(1)

print(person)
person.pop('eye_color')
print(person)

for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break

def print_hello_ten_times():
    for num in range(10):
        print('Hello')

print_hello_ten_times()

def print_hello_x_times(x):
    for num in range(x):
        print('Hello')

print_hello_x_times(4)

def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)