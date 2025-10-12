class Perro:
    especie = "canino"
    tipo = "mamifero"
    habitat = "terrestre"
    def __init__(self, nombre, edad, genero, raza, vacuna, propietario):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.raza = raza
        self.vacuna = vacuna
        self.propietario = propietario
    
# Instanciamos y mostramos dos perros
perro1 = Perro("Chuck", 3, "Macho", "Beagle", True, "Juan")
perro2 = Perro("Luna", 5, "Hembra", "Pastor Alemán", False, "Ana")

print("Perro 1: ", perro1.tipo, perro1.especie, perro1.habitat)
print(perro1.nombre)
print(perro1.edad)
print(perro1.genero)
print(perro1.raza)
print(perro1.vacuna)
print(perro1.propietario)
print()
print("Perro 2: ", perro2.tipo, perro2.especie, perro2.habitat)
print(perro2.nombre)
print(perro2.edad)
print(perro2.genero)
print(perro2.raza)
print(perro2.vacuna)
print(perro2.propietario)
print()
print("Perro es:", Perro.tipo, "Especie:", Perro.especie, "Habitat:", Perro.habitat)