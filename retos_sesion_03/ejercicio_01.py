class Atleta:
    energia_inicial = 100

    def __init__(self, nombre, fuerza):
        self.nombre = nombre
        self.fuerza = fuerza
        self.energia = Atleta.energia_inicial

    # Método de instancia
    def entrenar(self):
        if self.energia >= 20:
            self.fuerza += 5
            self.energia -= 20
            print(f"{self.nombre} entrenó. Fuerza: {self.fuerza}, Energía: {self.energia}")
        else:
            print(f"{self.nombre} está muy cansado para entrenar")

    # Método de instancia
    def descansar(self):
        self.energia += 15
        if self.energia > 100:
            self.energia = 100
        print(f"{self.nombre} descansó. Energía: {self.energia}")

    # Método de instancia
    def comer(self, comida):
        if comida.lower() == "hamburguesa":
            self.energia += 25
            if self.energia > 100:
                self.energia = 100
            print(f"{self.nombre} comió y recuperó energía. Energía: {self.energia}")
        else:
            print(f"{self.nombre} solo come hamburguesas, no {comida}")

    # Método para mostrar estado actual
    def mostrar_estado(self):
        print(f"{self.nombre} → Fuerza: {self.fuerza}, Energía: {self.energia}")

    # Método de clase
    @classmethod
    def set_energia_inicial(cls, valor):
        cls.energia_inicial = valor
        print(f"Energía inicial para todos los atletas configurada en {valor}")

    @staticmethod
    def motivar():
        print("Nunca te rindas, el esfuerzo trae resultados!")

print("Creando atletas...")
atleta1 = Atleta("Carlos", 50)
atleta2 = Atleta("Lucía", 60)

# Mostrar estado inicial
atleta1.mostrar_estado()
atleta2.mostrar_estado()

atleta1.entrenar()
atleta1.comer("hamburguesa")
atleta1.descansar()

atleta2.entrenar()
atleta2.comer("ensalada")
atleta2.entrenar()

Atleta.set_energia_inicial(120)

Atleta.motivar()

print("\nEstado final:")
atleta1.mostrar_estado()
atleta2.mostrar_estado()
