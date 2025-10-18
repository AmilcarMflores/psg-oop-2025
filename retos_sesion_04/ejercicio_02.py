class Celula:
    def __init__(self, adn, tipo_celula, energia_inicial=100):
        self.__adn = adn
        self.__tipo_celula = tipo_celula
        self.__energia = energia_inicial

    @property
    def adn(self):
        return self.__adn

    @property
    def tipo_celula(self):
        return self.__tipo_celula

    @tipo_celula.setter
    def tipo_celula(self, nuevo_tipo):
        self.__tipo_celula = nuevo_tipo

    @property
    def energia(self):
        return self.__energia

    def comer(self, cantidad_energia):
        if cantidad_energia > 0:
            self.__energia += cantidad_energia
        else:
            print("La cantidad de energía para comer debe ser positiva")

    def dividirse(self):
        energia_minima_division = 50
        
        if self.__energia >= energia_minima_division:
            energia_nueva_celula = self.__energia // 2
            self.__energia = self.__energia - energia_nueva_celula
            
            nueva_celula = Celula(
                adn=self.__adn, 
                tipo_celula=self.__tipo_celula, 
                energia_inicial=energia_nueva_celula
            )
            
            return nueva_celula
        else:
            print("Energía insuficiente para dividirse")


celula_madre = Celula(adn="ATCG123", tipo_celula="Neurona", energia_inicial=100)
        
print(f"Célula Madre:")
print(f"ADN: {celula_madre.adn}")
print(f"Tipo: {celula_madre.tipo_celula}")
print(f"Energía inicial: {celula_madre.energia}")
        
celula_madre.comer(50)
print(f"\nDespués de comer:")
print(f"Energía: {celula_madre.energia}")
        
celula_hija = celula_madre.dividirse()
print(f"\nDespués de dividirse:")
print(f"Energía Célula Madre: {celula_madre.energia}")
print(f"Energía Célula Hija: {celula_hija.energia}")
        
