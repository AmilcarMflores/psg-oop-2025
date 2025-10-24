class Vehiculo:
    def __init__(self, velocidad=0, medio="desconocido"):
        self._velocidad = velocidad 
        self.medio = medio  

    def get_velocidad(self):
        return self._velocidad

    def get_medio(self):
        return self.medio

    def set_medio(self, medio):
        self.medio = medio


class Bicicleta(Vehiculo):
    def __init__(self, velocidad=0):
        super().__init__(velocidad, medio="terrestre")

    def pedalear(self):
        self._velocidad += 5
        print(f"La bicicleta pedalea y alcanza {self._velocidad} km/h.")


class Avion(Vehiculo):
    def __init__(self, velocidad=0):
        super().__init__(velocidad, medio="aéreo")

    def volar(self):
        self._velocidad += 50
        print(f"El avión acelera y alcanza {self._velocidad} km/h.")

bici = Bicicleta()
avion = Avion()

bici.pedalear()
bici.pedalear()

avion.volar()
avion.volar()

print(f"Bicicleta - Velocidad: {bici.get_velocidad()} km/h, Medio: {bici.get_medio()}")
print(f"Avión - Velocidad: {avion.get_velocidad()} km/h, Medio: {avion.get_medio()}")
