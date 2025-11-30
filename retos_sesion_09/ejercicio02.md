# Ejercicio 02 – BeatBox (Singleton)

## Análisis

### Requisitos
Un DJ necesita una consola de mezcla llamada **BeatBox**, capaz de:
- Seleccionar una pista de audio.
- Ajustar el volumen (subir o bajar).
- Mostrar el estado actual de la consola.
- Aplicar un único efecto de sonido a la vez entre: **eco**, **reverb** o **distorsión**.

Para garantizar que la consola sea única durante toda la ejecución, se debe implementar el patrón **Singleton**.

La clase debe incluir los siguientes métodos:
- `seleccionar_pista()`
- `ajustar_volumen()`
- `aplicar_efecto()`
- `mostrar_estado()`

El programa presentará un menú:
1. Ingresar el nombre de la pista de audio  
2. Ajustar volumen  
3. Aplicar efecto de sonido  
4. Mostrar estado actual  
5. Salir  

### Objeto identificado
- **BeatBox**

### Atributos
BeatBox:
- `pista_actual: str`
- `volumen: int`  
- `efecto_actual: str`  
- `__instancia`: instancia única (Singleton)

### Acciones / Métodos
- `seleccionar_pista()`: Cambia la pista de audio actual.
- `ajustar_volumen()`: Incrementa o reduce el volumen según elección del usuario.
- `aplicar_efecto()`: Aplica un solo efecto entre eco, reverb o distorsión.
- `mostrar_estado()`: Muestra la pista actual, el volumen y el efecto aplicado.
- `__new__()`: Aplica Singleton evitando múltiples instancias.

## Diagrama de clases

```mermaid
classDiagram
class BeatBox {
  - __instancia
  - pista_actual: str
  - volumen: int
  - efecto_actual: str
  + seleccionar_pista()
  + ajustar_volumen()
  + aplicar_efecto()
  + mostrar_estado()
  + __new__()
}
