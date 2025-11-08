# Análisis

Requisitos
- Representar números romanos como objetos
- La clase debe convertir de romano a entero y viceversa
- Se debe poder sumar dos objetos Romano usando `+`
- El resultado debe ser un nuevo objeto Romano
- Ejemplo:
    - "X" + "V" = "XV"      

Objetos
- Romano

Características
- valor_romano: String
- valor_entero: int
    
Acciones
- convertir_romano_a_entero()
- convertir_entero_a_romano()
- sobrecargar operador `+` → `__add__`
- mostrar valor romano (método `__str__`)

# Diseño

```mermaid
classDiagram
    class Romano {
        -valor_romano: String
        -valor_entero: int
        +__init__(valor_romano)
        +__add__(otro: Romano) Romano
        +__str__() String
        -roman_to_int(valor) int
        -int_to_roman(valor) String
    }
```
