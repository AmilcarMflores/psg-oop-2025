class Destino:
    def __init__(self, nombre, costo):
        self.nombre = nombre
        self.costo = costo

    def __str__(self):
        return f"{self.nombre} ➡ {self.costo} USD"

class Catalogo:
    def __init__(self):
        self.destinos = []

    def append(self, destino):
        self.destinos.append(destino)

    def __len__(self):
        return len(self.destinos)

    def __getitem__(self, index):
        return self.destinos[index]

    def __setitem__(self, index, valor):
        self.destinos[index] = valor

    def __delitem__(self, index):
        del self.destinos[index]

    def __iter__(self):
        return iter(self.destinos)

    def __str__(self):
        resultado =  "Destinos"
        for i, destino in enumerate(self.destinos, 1):
            resultado += f"\n{i}. {destino}"
        return resultado

d1 = Destino("Paris", 1500)
d2 = Destino("Kyoto", 2000)
d3 = Destino("Cusco", 800)
d4 = Destino("Nueva York", 1800)

catalogo = Catalogo()
catalogo.append(d1)
catalogo.append(d2)
catalogo.append(d3)
catalogo.append(d4)

print(catalogo)

print(f"\nCantidad de destinos: {len(catalogo)}")

print(f"Destino en índice 2: {catalogo[2]}")

d_nuevo = Destino("Roma", 1600)
catalogo[1] = d_nuevo
print(catalogo)

del catalogo[3]
print(catalogo)

for destino in catalogo:
    print(f"OFERTA: {destino}")