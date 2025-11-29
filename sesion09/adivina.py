import random

class Juego:
    __instancia = None
    iniciado = False
    intentos = 0
    scores = []

    def __new__(cls):
        if cls.__instancia is None:
            cls.__instancia = super().__new__(cls)
        return cls.__instancia
    
    def iniciar(self):
        if self.iniciado:
            print("💢 El juego ya está en curso.")
            return
        print("💬 Adivina el número entre 1 y 100.")
        self.numero = random.randint(1, 100)
        self.intentos = 0
        self.iniciado = True
    
    def finalizar(self):
        print("❗ Juego finalizado.")
        self.iniciado = False
    
    def estado(self):
        return self.iniciado
    
    def adivinar(self, numero, jugador):
        if not self.iniciado:
            print("💢 El juego no ha iniciado.")
            return False
        self.intentos += 1
        if numero < self.numero:
            print("💡 El número es mayor.")
        elif numero > self.numero:
            print("💡 El número es menor.")
        else:
            print("🎉Adivinaste el número 🎉")
            self.scores.append((jugador, self.intentos))
            self.finalizar()
            return True
        return False
    
    def score(self):
        print("🏁 Score")
        for jugador, intentos in self.scores:
            print(f"{jugador}: {intentos} intentos")

class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return f"🕹️ {self.nombre}"
    
    def jugar(self):
        Juego().iniciar()
    
    def adivinar(self, numero):
        return Juego().adivinar(numero, self)
    
    def finalizar(self):
        Juego().finalizar()
 
    def jugando(self):
        return Juego().estado()
    
while True:
    nombre = input("💬 Tu nombre (o 'salir' para terminar): ")
    if nombre.lower() == "salir":
        break
    jugador = Jugador(nombre)
    jugador.jugar()
    while jugador.jugando():
        numero = input("💬 Adivina el número o 'salir': ")
        if numero.lower() == "salir":
            jugador.finalizar()
        else:
            try:
                jugador.adivinar(int(numero))
            except ValueError:
                print("💢 Ingresa un número válido")
    Juego().score()
print("👋 Gracias por jugar. ¡Hasta luego!")