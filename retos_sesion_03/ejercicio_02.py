class Cocinero:
    recetas_permitidas = {
        "pan": {"harina", "agua"},
        "pizza": {"harina", "agua", "sal", "tomate", "queso"},
        "galleta": {"harina", "agua", "sal", "chocolate"}
    }

    cocineros_registrados = []

    def __init__(self, nombre, ingredientes):
        self.nombre = nombre
        self.ingredientes = set(ingredientes)
        self.productividad = 0
        Cocinero.cocineros_registrados.append(self)

    # Método de instancia: preparar una receta
    def preparar(self, receta):
        if receta not in Cocinero.recetas_permitidas:
            print(f"{self.nombre}:La receta '{receta}' no existe en el sistema.")
            return

        ingredientes_requeridos = Cocinero.recetas_permitidas[receta]

        if ingredientes_requeridos.issubset(self.ingredientes):
            self.productividad += 1
            print(f"{self.nombre}:Preparó {receta} con éxito. Productividad: {self.productividad}")
        else:
            faltantes = ingredientes_requeridos - self.ingredientes
            print(f"{self.nombre}:No tiene los ingredientes necesarios para {receta}. Faltan: {faltantes}")

    def mostrar_estado(self):
        print(f"{self.nombre} → Ingredientes: {self.ingredientes}, Productividad: {self.productividad}")

    @classmethod
    def productividad_total(cls):
        total = sum(c.productividad for c in cls.cocineros_registrados)
        print(f"Productividad total de la cocina: {total} puntos")
        return total

    @staticmethod
    def mostrar_recetas():
        print("\nRecetas disponibles en el sistema:")
        for nombre, ingredientes in Cocinero.recetas_permitidas.items():
            print(f"• {nombre}: {', '.join(ingredientes)}")

Cocinero.mostrar_recetas()

c1 = Cocinero("Mario", ["harina", "agua", "sal", "tomate", "queso"])
c2 = Cocinero("Lucía", ["harina", "agua", "sal", "chocolate"])
c3 = Cocinero("Pedro", ["agua", "harina"])
print("\n--- Estado Inicial ---")
c1.mostrar_estado()
c2.mostrar_estado()
c3.mostrar_estado()
print("\n--- Preparando Recetas ---")
c1.preparar("pizza")
c2.preparar("galleta")
c3.preparar("pan")
c3.preparar("pizza")
print("\n--- Estado Final ---")
c1.mostrar_estado()
c2.mostrar_estado()
c3.mostrar_estado()
print("\n--- Métrica Global ---")
Cocinero.productividad_total()
