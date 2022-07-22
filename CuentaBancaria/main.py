from CuentaBancaria import CuentaBancaria
# Crear 2 instancias de la clase Usuario
juana = CuentaBancaria("Juana")
lola = CuentaBancaria("Lola")


print("----JUANA---")
# Haz que el 1er usuario haga 3 depositos, 1 retiro, genera intereses y muestra la informacion de la cuenta 
juana.mostrar_info_cuenta()
juana.deposito(15).deposito(15).deposito(200).retiro(100).generar_interes().mostrar_info_cuenta()

print("---LOLA----")
# Haz que el 2do usuario haga 2 deposito, 4 retiros, genera intereses y muestra la informacion de la cuenta 
lola.mostrar_info_cuenta()
lola.deposito(180).deposito(200).retiro(20).retiro(30).retiro(10).retiro(20).generar_interes().mostrar_info_cuenta()


#BONUS NINJA
print("-----BONUS NINJA----")
CuentaBancaria.mostrar_info()
