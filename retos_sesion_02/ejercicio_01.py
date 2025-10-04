class Animal:
    origen = "feral"

    def __init__(self, especie, tipo, lugar):
        self.especie = especie
        self.tipo = tipo
        self.lugar = lugar

animal1 = Animal("León", "mamífero", "Sabana africana")
animal2 = Animal("Elefante", "mamífero", "Reserva de Kenya")
animal3 = Animal("Iguana", "reptil", "Selva tropical")
animal4 = Animal("Águila", "ave", "Cordillera andina")

print("Animales registrados:")
print("Animal 1:", animal1.origen, animal1.especie, animal1.tipo, animal1.lugar)
print("Animal 2:", animal2.origen, animal2.especie, animal2.tipo, animal2.lugar)
print("Animal 3:", animal3.origen, animal3.especie, animal3.tipo, animal3.lugar)
print("Animal 4:", animal4.origen, animal4.especie, animal4.tipo, animal4.lugar)
