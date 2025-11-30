import random

class PiedraPapelTijera:
    __instancia = None
    puntaje_jugador = 0
    puntaje_computadora = 0

    def __new__(cls):
        if cls.__instancia is None:
          cls.__instancia = super().__new__(cls)
        return cls.__instancia
    
    def iniciar_partida(self):
        opciones = ['piedra', 'papel', 'tijera']
        while True:
          eleccion_jugador = input("Elige piedra, papel o tijera (o 'salir' para terminar): ").lower()
          if eleccion_jugador == 'salir':
            print("Gracias por jugar!")
            break
          if eleccion_jugador not in opciones:
            print("Elección inválida. Intenta de nuevo.")
            continue
          
          eleccion_computadora = random.choice(opciones)
          print(f"La computadora eligió: {eleccion_computadora}")

          if eleccion_jugador == eleccion_computadora:
            print("Empate!")
          elif (eleccion_jugador == 'piedra' and eleccion_computadora == 'tijera') \
            or (eleccion_jugador == 'papel' and eleccion_computadora == 'piedra') \
            or (eleccion_jugador == 'tijera' and eleccion_computadora == 'papel'):
            print("¡Ganaste!")
            self.puntaje_jugador += 1
          else:
            print("Perdiste!")
            self.puntaje_computadora += 1

    def mostrar_puntaje(self):
        print(f"Puntaje final - Jugador: {self.puntaje_jugador}, Computadora: {self.puntaje_computadora}")

    def reiniciar_juego(self):
        self.puntaje_jugador = 0
        self.puntaje_computadora = 0
        print("El juego ha sido reiniciado.")

while True:
    print("=="*30)
    print("1. Iniciar una nueva partida")
    print("2. Mostrar puntajes")
    print("3. Reiniciar el juego")
    print("4. Salir")

    opcion = input("Elige una opción: ")

    juego = PiedraPapelTijera()

    if opcion == '1':
        juego.iniciar_partida()
    elif opcion == '2':
        juego.mostrar_puntaje()
    elif opcion == '3':
        juego.reiniciar_juego()
    elif opcion == '4':
        print("¡Gracias por jugar!")
        break
    else:
        print("Opción inválida. Intenta de nuevo.")