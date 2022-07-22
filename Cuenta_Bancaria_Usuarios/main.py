from Usuario import Usuario
from CuentaBancaria import CuentaBancaria

lola = Usuario("Lola")
lola_co = Usuario("Lola Cuenta Corriente")

lola.hacer_deposito(180).hacer_deposito(200)

#BONUS SENSEI
print("-----BONUS SENSEI ----")
lola.transferir(lola_co, 200)

