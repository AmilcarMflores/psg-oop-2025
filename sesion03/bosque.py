class Arbol:
    altura_germinacion = 0.0
    altura_min_frutos = 10.0
    altura_maxima = 15.0
    def __init__(self, especie, altura, frutal):
        self.especie = especie
        self.altura = altura
        self.frutal = frutal
        self.vivo = True

    @classmethod
    def germinar(cls, especie, frutal):
        print(f"El árbol {especie} ha nacido")
        return cls(especie, cls.altura_germinacion, frutal)
    
    @classmethod
    def puede_morir(cls, arbol):
        if arbol.altura >= cls.altura_maxima:
            print(f"El árbol {arbol.especie} ha muerto")
            arbol.vivo = False
        else:
            print(f"El árbol {arbol.especie} sigue vivo")

    def crecer(self, metros):
        self.altura += metros
        print(f"El árbol ha crecido {metros} metros")
        print(f"Altura actual: {self.altura} metros")

    def dar_frutos(self):
        if self.frutal and self.altura >= self.altura_min_frutos:
            print(f"El árbol {self.especie} ha dado frutos")
        elif self.frutal:
            print(f"El árbol {self.especie} no ha dado frutos.")
        else:
            print(f"El árbol {self.especie} no es frutal.")

roble = Arbol.germinar("Roble", True)
roble.crecer(5.1)
roble.dar_frutos()
roble.crecer(6.4)
roble.dar_frutos()
Arbol.puede_morir(roble)
roble.crecer(3.5)
Arbol.puede_morir(roble)