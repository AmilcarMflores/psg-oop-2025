# Simulación de Vehículos

## Análisis

### Requisitos

La empresa de transporte necesita modelar distintos tipos de vehículos (bicicletas y aviones) que comparten ciertas características y comportamientos comunes.  
Para ello se utilizará herencia para evitar duplicar código.

### Objetos
- Vehiculo

### Características
- Vehículo
  - _velocidad (protegido)
  - medio (público) (terrestre, acuático, aéreo).

### Acciones
  - get_velocidad()
  - set_medio(medio)
  - get_medio()

### Objetos derivados
- Bicicleta (hereda de Vehiculo)
- Avión (hereda de Vehiculo)

#### Acciones
  - pedalear() (Bicicleta)
  - volar() (Avión)

## Diagrama

```mermaid
classDiagram
    class Vehiculo {
        - _velocidad: float
        + medio: str
        + get_velocidad(): float
        + get_medio(): str
        + set_medio(medio: str)
    }

    class Bicicleta {
        + pedalear()
    }

    class Avion {
        + volar()
    }

    Vehiculo <|-- Bicicleta
    Vehiculo <|-- Avion
```

