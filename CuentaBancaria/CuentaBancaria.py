class CuentaBancaria:

    cuentasTotales = []

    def __init__(self, tasa_interes=0.01, balance=0):
        self.tasa_interes = tasa_interes
        self.balance = balance
        CuentaBancaria.cuentasTotales.append(self)

    def deposito(self, amount):
        self.balance += amount
        print(f"Tu nuevo balance es: {self.balance}")
        print(f"Tu monto es de: {amount}")
        return self

    def retiro(self, amount):
        if self.balance >= amount:
            self.balance -= amount

    def retiro(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Retiraste: {amount}")
            print(f"Tu nuevo balance es: {self.balance}")
        else:
            print("Fondos insuficientes: cobrando una tarifa de $5")
            self.balance -= (amount + 5)
            print(f"Tu nuevo balance es: {self.balance}")
        return self

    def mostrar_info_cuenta(self):
        print(f"Balance: {self.balance}")
        return self

    def generar_interes(self):
        if self.balance > 0:
            self.balance += self.balance * self.tasa_interes
            print(f"Tu nuevo monto con intereses es: {self.balance}")
        else:
            print("Sin saldo")
        return self

    def printInformation(self):
        print(f"Intereses: {self.tasa_interes} y  Balance: {self.balance}")
        return self

    @classmethod
    def printAllAccountsInfo(cls): 
        print(f"Esta es la informacion de todas las cuentas")
        for x in cls.cuentasTotales:
            x.printInformation()
