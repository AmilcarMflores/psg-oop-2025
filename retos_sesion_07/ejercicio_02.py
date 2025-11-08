class Instrumento:
    def __init__(self, nombre):
        self.nombre = nombre

    def tocar(self):
        print("El instrumento está sonando")

class Guitarra(Instrumento):
    def __init__(self, nombre, cuerdas, material):
        super().__init__(nombre)
        self.cuerdas = cuerdas
        self.material = material

    def tocar(self):
        print("strum strum (guitarra sonando)")

class Piano(Instrumento):
    def __init__(self, nombre, teclas, tipo):
        super().__init__(nombre)
        self.teclas = teclas
        self.tipo = tipo

    def tocar(self):
        print("plin plin (piano sonando)")

class Tambor(Instrumento):
    def __init__(self, nombre, tamaño, material):
        super().__init__(nombre)
        self.tamaño = tamaño
        self.material = material

    def tocar(self):
        print("boom boom (tambor sonando)")
instrumentos = [
    Guitarra("Guitarra Acústica", 6, "madera"),
    Piano("Piano de cola", 88, "acústico"),
    Tambor("Tambor militar", "mediano", "madera")
]

for instrumento in instrumentos:
    print(f"Usando: {instrumento.nombre}")
    instrumento.tocar()
