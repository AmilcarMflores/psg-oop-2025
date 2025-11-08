class Romano:
    _valores = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100
    }

    def __init__(self, valor_romano):
        self.valor_romano = valor_romano
        self.valor_entero = self._roman_to_int(valor_romano)

    def _roman_to_int(self, valor):
        total = 0
        prev = 0
        for letra in reversed(valor):
            actual = self._valores[letra]
            if actual < prev:
                total -= actual
            else:
                total += actual
            prev = actual
        return total

    def _int_to_roman(self, valor):
        conversion = [
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I")
        ]

        resultado = ""
        for numero, simbolo in conversion:
            while valor >= numero:
                resultado += simbolo
                valor -= numero
        return resultado

    def __add__(self, otro):
        if not isinstance(otro, Romano):
            raise TypeError("Solo se pueden sumar objetos de tipo Romano")
        suma = self.valor_entero + otro.valor_entero
        nuevo_romano = self._int_to_roman(suma)
        return Romano(nuevo_romano)

    def __str__(self):
        return self.valor_romano

num1 = Romano("X")  # 10
num2 = Romano("V")  # 5
resultado = num1 + num2
print(f"{num1} + {num2} = {resultado}")  # X + V = XV
