class CuentaBancaria:

    cuentasTotales = []

    def __init__(self, tasa_interes=0.01, balance=0):
        self.tasa_interes = tasa_interes
        self.balance = balance
        CuentaBancaria.cuentasTotales.append(self)

    def deposito(self, amount):
        self.balance += amount
        print(f"You're new balance is {self.balance}")
        print(f"Tu Monto Es De {amount}")
        return self

    def retiro(self, amount):
        if self.balance >= amount:
            self.balance -= amount

    def retiro(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Retiraste: {amount}")
            print(f"Tu nuevo balance es {self.balance}")
        else:
            print("Fondos insuficiente: Te cargaremos un fee de $5")
            self.balance -= (amount + 5)
            print(f"Tu nuevo balance es {self.balance}")
        return self

    def mostrar_info_cuenta(self):
        print(f"Balance: {self.balance}")
        return self

    def generar_interes(self):
        if self.balance > 0:
            self.balance += self.balance * self.tasa_interes
            print(f"Tu nuevo monto con Intres es {self.balance}")
        else:
            print("No Tienes Saldo Suficientes:(")
        return self

    def printInformation(self):
        print(
            f"Account interest: {self.tasa_interes}. Account balance: {self.balance}.")
        return self

    @classmethod
    def printAllAccountsInfo(cls): 
        print(f"This is the information for all the accounts")
        for x in cls.cuentasTotales:
            x.printInformation()
