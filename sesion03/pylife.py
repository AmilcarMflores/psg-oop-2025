class Persona:
    # Constructor
    def __init__(self, nombre):
        self.nombre = nombre
        self.hambre = True  # Nueva característica
    # Método de instancia
    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre}")
    # Nuevo método de instancia
    def dormir(self, horas):
        print(f"{self.nombre} duerme por {horas} hrs.")
        print(f"{self.nombre} se ha despertado.")
        self.hambre = True # Al despertar tiene hambre
    def comer(self, comida):
        if self.hambre:
            print(f"{self.nombre} está comiendo {comida}.")
            self.hambre = False
            return "🍽️"
        else:
            print(f"{self.nombre} no tiene hambre.")
            return comida

# Instanciamos un objeto
jhon = Persona("Jhon")
jhon.saludar()
jhon.dormir(8)

# Llamando al método de la instancia
comida = jhon.comer("🍔")
print(f"Devolvió: {comida}")
comida = jhon.comer("🍕")
print(f"Devolvió: {comida}")


class Perro:
    factor_edad = 7  # Atributo de clase
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def ladrar(self):
        print(f"{self.nombre} dice: ¡Guau! ¡Guau!")

    def crecer(self, tiempo):
        self.edad += tiempo
        print(f"{self.nombre} ha crecido. Ahora tiene {self.edad} años.")

    # Método de clase
    @classmethod
    def nacer(cls, nombre):
        print(f"{nombre} ha nacido como un cachorro.")
        return cls(nombre, 0)
    
    @classmethod
    def edad_a_humano(cls, perro):
        print(f"En años humanos, {perro.nombre}")
        print(f"tiene {perro.edad * cls.factor_edad} años.")

# Instanciamos un objeto
rex = Perro.nacer("Rex")
rex.ladrar()
rex.crecer(3)
Perro.edad_a_humano(rex)
print()

class Gato:
    def __init__(self, nombre, color):
        self.nombre = nombre
        self.color = color
        self.edad = 0

    @classmethod
    def nacer(cls, nombre, color):
        print(f"{nombre} ha nacido como un cachorro")
        return cls(nombre, color)
    
    def crecer(self, tiempo):
        self.edad += tiempo
        print(f"{self.nombre} ha crecido {tiempo} años")

    def maullar(self):
        print(f"{self.nombre} dice: {Gato.sonidos()[0]}")

    @staticmethod
    def sonidos():
        return ["miau", "ronroneo"]
    
# Instanciamos un objeto
mimi = Gato.nacer("Mimi", "blanco")
mimi.maullar()
mimi.crecer(2)
sonidos = Gato.sonidos()
print(f"Sonidos de {mimi.nombre}: {sonidos}")