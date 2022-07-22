class CuentaBancaria:

    cuentasB = []

    def __init__(self,balance=0, tasa_interes=0.01 ):
        self.tasa_interes = tasa_interes
        self.balance = balance
        CuentaBancaria.cuentasB.append(self)

    def deposito(self, amount):
        self.balance += amount
        print(f"Has depositado dinero, tu nuevo balance es: {self.balance}")
        return self

    def retiro(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Has retirado dinero, tu nuevo balance es: {self.balance}")
        else:
            print("Fondos insuficientes: cobrando una tarifa de $5")
            self.balance -= (amount + 5)
        return self

    def mostrar_info_cuenta(self):
        print(f" Balance: {self.balance}")
        return self

    def generar_interes(self):
        if self.balance >= 0:
            self.tasa_interes += self.balance * self.tasa_interes
            self.balance += self.balance + self.tasa_interes
            print(f"Tu nuevo monto con intereses es: {self.balance}")
        return self

    @classmethod
    def mostrar_info(cls): 
        print("Esta es la informacion de todas las cuentas")
        for cuentas in cls.cuentasB:
            cuentas.mostrar_info_cuenta()
