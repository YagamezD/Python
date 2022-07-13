#Básico: imprime todos los números enteros del 0 al 150.
for n in range(151):
    print(n)
print("--------")
#Múltiplos de cinco: imprime todos los múltiplos de 5 entre 5 y 1,000.
for m in range(1001):
    if m % 5 ==0:
        print(m)
print("--------")

#Contar, a la manera del Dojo: imprime números enteros del 1 al 100. Si es divisible por 5, imprime "Coding” en su lugar. Si es divisible por 10, imprime "Coding Dojo".
for p in range(1,101):
    if p%5 ==0:
        print("Coding")
    if p%10 ==0:
        print("Coding Dojo")
    else:
        print(p)
print("--------")
#Whoa. Es un gran idiota: agrega los enteros impares del 0 al 500,000, e imprime la suma final.
sum = 0
for i in range(500001):
    if i%2 ==0:
        sum = sum + i
print(sum)
print("--------")

#Cuenta regresiva de a 4: imprime números positivos comenzando desde el 2018, en cuenta regresiva de 4 en 4.
num=2018
for i in range(2018):
    print(num)
    num-=4
    if(num>=0):
        continue
    else:
        break
print("--------")
    
#Contador flexible: establece tres variables: lowNum, highNum, mult. 
#Comenzando en lowNum y pasando por highNum, imprime solo los enteros que sean múltiplos de mult. 
#Por ejemplo, si lowNum=2, highNum=9 y mult=3. El bucle debe imprimir 3, 6, 9 (en líneas sucesivas).

lowNum = 2
highNum = 9
mult = 3
for o in range(lowNum, highNum+1): 
    if o % mult == 0:
        print(o)


