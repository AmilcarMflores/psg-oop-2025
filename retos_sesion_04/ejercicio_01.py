class Cuenta:
    def __init__(self, numero_cuenta, nombre_titular, saldo_inicial=0):
        self.__numero_cuenta = numero_cuenta  
        self.__saldo = saldo_inicial 
        self.nombre_titular = nombre_titular 

    @property
    def numero_cuenta(self):
        return self.__numero_cuenta

    @property
    def saldo(self):
        return self.__saldo

    def deposito(self, monto):
        if monto > 0:
            self.__saldo += monto
        else:
            print("El monto de depósito debe ser positivo")

    def retiro(self, monto):
        if monto > 0:
            if monto <= self.__saldo:
                self.__saldo -= monto
            else:
                print("Saldo insuficiente para realizar el retiro")
        else:
            print("El monto de retiro debe ser positivo")

mi_cuenta = Cuenta(numero_cuenta=12345, nombre_titular="Juan Pérez", saldo_inicial=1000)
    
print(f"Número de cuenta: {mi_cuenta.numero_cuenta}")

print(f"Saldo actual: {mi_cuenta.saldo}")
    
mi_cuenta.deposito(500)
print(f"Saldo después del depósito: {mi_cuenta.saldo}")
    
mi_cuenta.retiro(200)
print(f"Saldo después del retiro: {mi_cuenta.saldo}")

mi_cuenta.nombre_titular = "Juan Carlos Pérez"
print(f"Nuevo nombre del titular: {mi_cuenta.nombre_titular}")
