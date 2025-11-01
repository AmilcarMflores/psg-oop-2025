class Pasajero:
    def __init__(self, nombre, destino):
        self.nombre = nombre
        self.destino = destino

    def mostrar(self):
        print(f"🧍 Pasajero: {self.nombre}, destino: {self.destino}")

class Minibus:
    def __init__(self, numero_ruta, paradas):
        self.numero_ruta = numero_ruta
        self.paradas = paradas
        self._pasajeros = []           # Lista de pasajeros abordo
        self._indice_actual = 0        # Posición actual en la ruta
        self._direccion = 1            # 1 = ida, -1 = vuelta

    def parada_actual(self):
        return self.paradas[self._indice_actual]

    def avanzar(self):
        self._indice_actual += self._direccion

        if self._indice_actual == len(self.paradas) - 1 or self._indice_actual == 0:
            self._direccion *= -1

        print(f"Avanzando a la parada: {self.parada_actual()}")
        self.bajar_pasajeros()

    def subir_pasajero(self, pasajero):
        if pasajero.destino in self.paradas:
            self._pasajeros.append(pasajero)
            print(f"{pasajero.nombre} subió al minibus (Destino: {pasajero.destino})")
        else:
            print(f"{pasajero.nombre} no puede subir (Destino fuera de ruta)")

    def bajar_pasajeros(self):
        bajan = [p for p in self._pasajeros if p.destino == self.parada_actual()]
        for p in bajan:
            print(f"{p.nombre} bajó en la parada: {p.destino}")
            self._pasajeros.remove(p)

    def mostrar_estado(self):
        print(f"Minibus Ruta {self.numero_ruta}")
        print(f"Parada actual: {self.parada_actual()}")
        print("Pasajeros a bordo:")
        if not self._pasajeros:
            print("   (sin pasajeros)")
        else:
            for p in self._pasajeros:
                print(f"   - {p.nombre} → {p.destino}")
        print("-" * 40)

paradas = ["Arce", "Prado", "Perez"]
minibus = Minibus(42, paradas)

p1 = Pasajero("Ana", "Prado")
p2 = Pasajero("Luis", "Perez")
p3 = Pasajero("Marta", "Arce")

minibus.subir_pasajero(p1)
minibus.subir_pasajero(p2)
minibus.subir_pasajero(p3)

minibus.mostrar_estado()
for _ in range(6):
    minibus.avanzar()
    minibus.mostrar_estado()
