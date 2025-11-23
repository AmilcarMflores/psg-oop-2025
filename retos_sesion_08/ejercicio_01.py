class Fraccion:
    def __init__(self, numerador, denominador):
        self.numerador = int(numerador)
        if denominador == 0:
            raise ValueError("El denominador no puede ser cero.")
        self.denominador = int(denominador)

    def __str__(self):
        return f"{self.numerador}/{self.denominador}"

    def __add__(self, otro):
        nuevo_num = (self.numerador * otro.denominador) + (otro.numerador * self.denominador)
        nuevo_den = self.denominador * otro.denominador
        return Fraccion(nuevo_num, nuevo_den)

    def __sub__(self, otro):
        nuevo_num = (self.numerador * otro.denominador) - (otro.numerador * self.denominador)
        nuevo_den = self.denominador * otro.denominador
        return Fraccion(nuevo_num, nuevo_den)

    def __mul__(self, otro):
        nuevo_num = self.numerador * otro.numerador
        nuevo_den = self.denominador * otro.denominador
        return Fraccion(nuevo_num, nuevo_den)

    def __truediv__(self, otro):
        nuevo_num = self.numerador * otro.denominador
        nuevo_den = self.denominador * otro.numerador
        return Fraccion(nuevo_num, nuevo_den)

    def __eq__(self, otro):
        if isinstance(otro, Fraccion):
            return (self.numerador * otro.denominador) == (otro.numerador * self.denominador)
        return False

    def __ne__(self, otro):
        return not self.__eq__(otro)

    def __lt__(self, otro):
        if isinstance(otro, Fraccion):
            return (self.numerador / self.denominador) < (otro.numerador / otro.denominador)
        return False

    def __gt__(self, otro):
        if isinstance(otro, Fraccion):
            return (self.numerador / self.denominador) > (otro.numerador / otro.denominador)
        return False

f1 = Fraccion(1, 2)
f2 = Fraccion(3, 4)
f3 = Fraccion(2, 4) 

print(f"Fracción 1: {f1}")
print(f"Fracción 2: {f2}")

suma = f1 + f2
resta = f2 - f1
multi = f1 * f2
div = f1 / f2 

print(f"{f1} + {f2} = {suma}")
print(f"{f2} - {f1} = {resta}")
print(f"{f1} * {f2} = {multi}")
print(f"{f1} / {f2} = {div}")

print(f"¿{f1} == {f3}? {f1 == f3}")
print(f"¿{f1} != {f2}? {f1 != f2}")
print(f"¿{f1} < {f2}?  {f1 < f2}")
print(f"¿{f1} > {f2}?  {f1 > f2}")