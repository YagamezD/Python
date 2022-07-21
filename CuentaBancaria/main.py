from Usuario import Usuario
from CuentaBancaria import CuentaBancaria
# Crear 2 instancias de la clase Usuario
juana = Usuario("Juana")
lola = Usuario("Lola")


print("----JUANA---")
# Haz que el 1er usuario haga 3 depositos y 1 giro, luego muestre balance
juana.mostrar_balance()
juana.hacer_deposito(15).hacer_deposito(15).hacer_deposito(200).hacer_retiro(100).generar_interes().mostrar_balance()

print("---LOLA----")
# Haz que el 2do usuario haga 1 deposito y 3 giros, luego muestre balance
lola.mostrar_balance()
lola.hacer_deposito(180).hacer_deposito(200).hacer_retiro(20).hacer_retiro(30).hacer_retiro(10).hacer_retiro(20).generar_interes().mostrar_balance()


#BONUS NINJA
print("-----BONUS NINJA----")
CuentaBancaria.mostrar_info()
