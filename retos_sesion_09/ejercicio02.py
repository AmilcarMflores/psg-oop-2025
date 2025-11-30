class BeatBox:
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
            cls._instancia.pista = None
            cls._instancia.volumen = 50
            cls._instancia.efecto = None
        return cls._instancia

    def seleccionar_pista(self, pista):
        self.pista = pista

    def ajustar_volumen(self, cambio):
        self.volumen = max(0, min(100, self.volumen + cambio))

    def aplicar_efecto(self, efecto):
        if efecto in ["eco", "reverb", "distorsion"]:
            self.efecto = efecto

    def mostrar_estado(self):
        print("Pista:", self.pista)
        print("Volumen:", self.volumen)
        print("Efecto:", self.efecto)


consola = BeatBox()

opcion = 0
while opcion != 5:
    print("\n1. Ingresar pista")
    print("2. Ajustar volumen")
    print("3. Aplicar efecto")
    print("4. Mostrar estado")
    print("5. Salir")

    opcion = int(input("Elige una opción: "))

    if opcion == 1:
        pista = input("Nombre de la pista: ")
        consola.seleccionar_pista(pista)

    elif opcion == 2:
        valor = int(input("Subir/bajar volumen (+ / -): "))
        consola.ajustar_volumen(valor)

    elif opcion == 3:
        efecto = input("Efecto (eco, reverb, distorsion): ")
        consola.aplicar_efecto(efecto)

    elif opcion == 4:
        consola.mostrar_estado()
