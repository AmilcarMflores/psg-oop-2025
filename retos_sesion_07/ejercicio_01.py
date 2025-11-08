class Martillo:
    def usar(self):
        print("🔨 Clavando clavos")

class LlaveInglesa:
    def usar(self):
        print("🔧 Apretando tuercas")

class Destornillador:
    def usar(self):
        print("🪛 Ajustando tornillos")

class Carpintero:
    def usar(self, herramienta):
        herramienta.usar()

carpintero = Carpintero()
martillo = Martillo()
llave = LlaveInglesa()
destornillador = Destornillador()

carpintero.usar(martillo)
carpintero.usar(llave)
carpintero.usar(destornillador)

class Martillo:
    def __init__(self, tipo_mango, material, peso):
        self.tipo_mango = tipo_mango
        self.material = material
        self.peso = peso

    def usar(self):
        print("🔨 Clavando clavos con el martillo")


class Destornillador:
    def __init__(self, tipo_mango, material, peso):
        self.tipo_mango = tipo_mango
        self.material = material
        self.peso = peso

    def usar(self):
        print("🪛 Ajustando tornillos con el destornillador")


class LlaveInglesa:
    def __init__(self, tipo_mango, material, peso):
        self.tipo_mango = tipo_mango
        self.material = material
        self.peso = peso

    def usar(self):
        print("🔧 Apretando tuercas con la llave inglesa")


class Carpintero:
    def usar_herramienta(self, herramienta):
        herramienta.usar()


martillo = Martillo("madera", "acero", 1.2)
destornillador = Destornillador("goma", "acero", 0.5)
llave = LlaveInglesa("plástico", "acero reforzado", 0.8)

carpintero = Carpintero()

herramientas = [martillo, destornillador, llave]

for h in herramientas:
    carpintero.usar_herramienta(h)
