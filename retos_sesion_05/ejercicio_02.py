class Nadador:
    def nadar(self):
        print("Estoy nadando por el agua.")

class Volador:
    def volar(self):
        print("Estoy volando por el cielo.")


class Pez(Nadador):
    def mostrar(self):
        print("Soy un Pez y mi habilidad principal es nadar.")


class Pajaro(Volador):
    def mostrar(self):
        print("Soy un Pájaro y mi habilidad principal es volar.")


class Pato(Nadador, Volador):
    def mostrar(self):
        print("Soy un Pato y puedo nadar y volar.")

pez = Pez()
pajaro = Pajaro()
pato = Pato()

pez.mostrar()
pez.nadar()
print()

pajaro.mostrar()
pajaro.volar()
print()

pato.mostrar()
pato.nadar()
pato.volar()
