class Vizcacha:
    def __init__(self):
        self.escondido = False
        self.estado = "feliz"

    def comer(self, comida):
        if comida == "🥕":
            print(f"Vizcacha está comiendo {comida}.")
        else:
            print(f"Vizcacha no come {comida}.")
    
    def excavar(self):
        print("La vizcacha está excavando un agujero")
        self.escondido = True
        self.estado = "asustada"
        print(f"Vizcacha está {self.estado}.")

    def silvar(self):
        print("iiih iiih")
        self.estado = "feliz"
        print(f"Vizcacha está {self.estado}.")

# Instanciamos un objeto
vizcacha = Vizcacha()
vizcacha.comer("🥕")
vizcacha.comer("🍎")
vizcacha.excavar()
vizcacha.silvar()