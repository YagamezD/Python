from Usuario import Usuario
#Crear 3 instancias de la clase Usuario
adrien = Usuario("Adrien")
nibbles = Usuario("Mr. Nibbles")
benny = Usuario("Benny Bob")


#Haz que el 1er usuario haga 3 depositos y 1 giro, luego muestre balance
adrien.make_deposit(115).make_deposit(100).make_deposit(100).make_withdraw(10).show_balance()

#Haz que el 2do usuario haga 1 deposito y 3 giros, luego muestre balance
nibbles.make_deposit(1800).make_withdraw(200).make_withdraw(200).make_withdraw(200).show_balance()

#Haz que el 3 haga 1 deposito y 3 giros, luego muestre balance
benny.make_deposit(500).make_withdraw(1000).make_withdraw(3500).make_withdraw(3500).show_balance()

#Bonus agregar metodo transferir_dinero, ejecutar transferencia de un usuario a otro
# print(f'User: {adrien.name}, Balance: {adrien.balance_account}')
# print(f'User: {nibbles.name}, Balance: {nibbles.balance_account}')
# print(f'User: {benny.name}, Balance: {benny.balance_account}')
nibbles.transfer_money(adrien, 400)
# print(f'User: {nibbles.name}, Balance: {nibbles.balance_account}')
# print(f'User: {adrien.name}, Balance: {adrien.balance_account}')"""