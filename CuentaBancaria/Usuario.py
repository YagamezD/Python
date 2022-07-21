from CuentaBancaria import CuentaBancaria
class Usuario:

    def __init__(self, name):
        self.name = name
        self.cuenta = CuentaBancaria(balance=0, tasa_interes=0.02)

    def hacer_deposito(self, amount):
        self.cuenta.deposito(amount)
        return self
        
        
    def hacer_retiro(self, amount): 
        self.cuenta.retiro(amount)
        return self
        
    def mostrar_balance(self):
        print(f"Usuario: {self.name}, Balance: $ {self.cuenta.balance}")
        return self
    
    def generar_interes(self):
        self.cuenta.generar_interes()
        return self

    







