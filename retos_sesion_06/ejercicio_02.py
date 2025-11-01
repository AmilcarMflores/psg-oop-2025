class Departamento:
    def __init__(self, numero, inquilinos=None):
        self.numero = numero
        self.inquilinos = inquilinos if inquilinos else []

    def mostrar_info(self):
        print(f"Departamento {self.numero}")
        if self.inquilinos:
            print("      Inquilinos:")
            for i in self.inquilinos:
                print(f"         - {i}")
        else:
            print("      (Sin inquilinos)")

class Oficina:
    def __init__(self, numero, telefono):
        self.numero = numero
        self.telefono = telefono

    def mostrar_info(self):
        print(f"Oficina {self.numero} - Teléfono: {self.telefono}")

class Piso:
    def __init__(self, numero):
        self.numero = numero
        self.departamentos = []
        self.oficinas = []

    def agregar_departamento(self, departamento):
        self.departamentos.append(departamento)

    def agregar_oficina(self, oficina):
        self.oficinas.append(oficina)

    def mostrar_info(self):
        print(f"Piso {self.numero}")
        print(" Departamentos:")
        if not self.departamentos:
            print("   (No hay departamentos)")
        else:
            for d in self.departamentos:
                d.mostrar_info()

        print(" Oficinas:")
        if not self.oficinas:
            print("   (No hay oficinas)")
        else:
            for o in self.oficinas:
                o.mostrar_info()

class Edificio:
    def __init__(self, nombre, direccion):
        self.nombre = nombre
        self.direccion = direccion
        self.pisos = []

    def agregar_piso(self, piso):
        self.pisos.append(piso)

    def mostrar_info(self):
        print(f"Edificio: {self.nombre}")
        print(f"Dirección: {self.direccion}")
        print("=" * 40)
        for piso in self.pisos:
            piso.mostrar_info()
        print("=" * 40)

edificio = Edificio("Torre Andina", "Av. Mariscal Santa Cruz #123")

piso1 = Piso(1)
piso2 = Piso(2)
piso3 = Piso(3)

piso1.agregar_departamento(Departamento(101, ["Juan", "María"]))
piso1.agregar_oficina(Oficina("1A", "222-1111"))

piso2.agregar_departamento(Departamento(201, ["Carlos"]))
piso2.agregar_oficina(Oficina("2B", "222-2222"))
piso2.agregar_oficina(Oficina("2C", "222-3333"))

piso3.agregar_departamento(Departamento(301, ["Lucía", "Pedro"]))
piso3.agregar_departamento(Departamento(302))
piso3.agregar_oficina(Oficina("3A", "333-4444"))

edificio.agregar_piso(piso1)
edificio.agregar_piso(piso2)
edificio.agregar_piso(piso3)

edificio.mostrar_info()
