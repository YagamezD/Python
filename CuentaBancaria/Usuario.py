from CuentaBancaria import CuentaBancaria
class Usuario:


    def __init__(self, name):
        self.name = name
        self.cuenta = CuentaBancaria(balance=0, tasa_interes=0.02)
        self.cuentaAhorros=CuentaBancaria(balance=0,tasa_interes=0.02)
        self.cuentaCorriente=CuentaBancaria(balance=0,tasa_interes=0.01)
        
        
    def make_deposit(self, amount):
        self.cuenta.deposito(amount)
        return self
        
        
    def make_withdraw(self, amount):
        self.cuenta.retiro(amount)
        return self
        
    def show_balance(self):
        self.cuenta.printInformation()
        return self

        
    def transfer_money(self, other_user, amount):
        self.make_withdraw(amount)
        other_user.make_deposit(amount)
        self.show_balance()
        other_user.show_balance()   
    


    def método_ejemplo(self):
        self.cuenta.depósito(100)		
        print(self.cuenta.balance)







