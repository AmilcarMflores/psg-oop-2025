class Mascota:
    origen = "abandonado"
    def __init__(self, nombre, especie):
        self.nombre = nombre
        self.especie = especie
    
print("Mascotas encontradas...")
perro = Mascota("perro 001", "perro")
gato = Mascota("gato 002", "gato")
print("Mascota 1:", perro.nombre, perro.especie, perro.origen)
print("Mascota 2:", gato.nombre, gato.especie, gato.origen)

print("\nRescatando mascotas...")
Mascota.origen = "rescatado"
perro.nombre = "Milaneso"
gato.nombre = "Kitty"

print("Mascotas rescatadas...")
print("Mascota 1:", perro.nombre, perro.especie, perro.origen)
print("Mascota 2:", gato.nombre, gato.especie, gato.origen)