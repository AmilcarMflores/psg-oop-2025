class Vino:
    def __init__(self, nombre, tipo, cepa, anio):
        self.nombre = nombre
        self.tipo = tipo
        self.cepa = cepa
        self.anio = anio

class Queso:
    def __init__(self, nombre, variedad, edad, lleva_sal):
        self.nombre = nombre
        self.variedad = variedad
        self.edad = edad
        self.lleva_sal = lleva_sal

vino1 = Vino("Cabernet Sauvignon", "tinto", "Cabernet", 2018)
vino2 = Vino("Chardonnay Reserva", "blanco", "Chardonnay", 2020)
vino3 = Vino("Malbec Roble", "tinto", "Malbec", 2019)
vino4 = Vino("Rosé Verano", "rosado", "Syrah", 2021)

queso1 = Queso("Gouda", "semiduro", "6 meses", True)
queso2 = Queso("Brie", "blando", "2 semanas", False)
queso3 = Queso("Parmesano", "duro", "18 meses", True)

print("\nInventario de Vinos:")
print(f"1. {vino1.nombre}, {vino1.tipo}, {vino1.cepa}, año {vino1.anio}")
print(f"2. {vino2.nombre}, {vino2.tipo}, {vino2.cepa}, año {vino2.anio}")
print(f"3. {vino3.nombre}, {vino3.tipo}, {vino3.cepa}, año {vino3.anio}")
print(f"4. {vino4.nombre}, {vino4.tipo}, {vino4.cepa}, año {vino4.anio}")

print("\nInventario de Quesos:")
print(f"1. {queso1.nombre}, {queso1.variedad}, {queso1.edad}, lleva sal: {queso1.lleva_sal}")
print(f"2. {queso2.nombre}, {queso2.variedad}, {queso2.edad}, lleva sal: {queso2.lleva_sal}")
print(f"3. {queso3.nombre}, {queso3.variedad}, {queso3.edad}, lleva sal: {queso3.lleva_sal}")
