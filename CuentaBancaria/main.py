from Usuario import Usuario
from CuentaBancaria import CuentaBancaria
# Crear 3 instancias de la clase Usuario
juana = Usuario("Juana")
lola = Usuario("Lola")



# Haz que el 1er usuario haga 3 depositos y 1 giro, luego muestre balance
juana.make_deposit(10).make_deposit(10).make_deposit(200).make_withdraw(100).show_balance()
print("-------")

# Haz que el 2do usuario haga 1 deposito y 3 giros, luego muestre balance
lola.make_deposit(180).make_withdraw(20).make_withdraw(30).make_withdraw(10).show_balance()
print("-------")

#BONUS SENSEI
oscar= Usuario("Oscar")
oscar.cuentaAhorros.deposito(100).deposito(200) .generar_interes()
print("-------")

oscar.cuentaCorriente.deposito(500).retiro(200).generar_interes().mostrar_info_cuenta()