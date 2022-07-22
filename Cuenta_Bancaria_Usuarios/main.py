from Usuario import Usuario
from CuentaBancaria import CuentaBancaria
# Crear 2 instancias de la clase Usuario
juana = Usuario("Juana")
lola = Usuario("Lola")


print("----JUANA---")
# Haz que el 1er usuario haga 3 depositos, 1 retiro, genera intereses y muestra la informacion de la cuenta 
juana.mostrar_balance()
juana.hacer_deposito(15).hacer_deposito(15).hacer_deposito(200).hacer_retiro(100).generar_interes().mostrar_balance()

print("---LOLA----")
# Haz que el 2do usuario haga 2 deposito, 4 retiros, genera intereses y muestra la informacion de la cuenta 
lola.mostrar_balance()
lola.hacer_deposito(180).hacer_deposito(200).hacer_retiro(20).hacer_retiro(30).hacer_retiro(10).hacer_retiro(20).generar_interes().mostrar_balance()


#BONUS NINJA
print("-----BONUS NINJA----")
CuentaBancaria.mostrar_info()


#Bonus agregar metodo transferir_dinero, ejecutar transferencia de un usuario a otro
# print(f'User: {adrien.name}, Balance: {adrien.balance_account}')
# print(f'User: {nibbles.name}, Balance: {nibbles.balance_account}')
# print(f'User: {benny.name}, Balance: {benny.balance_account}')
nibbles.transfer_money(adrien, 400)
# print(f'User: {nibbles.name}, Balance: {nibbles.balance_account}')
# print(f'User: {adrien.name}, Balance: {adrien.balance_account}')"""