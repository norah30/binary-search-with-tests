# Búsqueda Binaria con Pruebas

Implementación en Python del algoritmo de búsqueda binaria, acompañada de pruebas unitarias para casos comunes y casos límite.

## Descripción generalmnb

Este proyecto muestra cómo funciona la búsqueda binaria sobre listas ordenadas y cómo validar su comportamiento mediante pruebas automatizadas. Incluye ejemplos para búsquedas exitosas, valores no encontrados, listas vacías, listas con un solo elemento y elementos duplicados.

## Características

- Implementación del algoritmo de búsqueda binaria en Python
- Pruebas unitarias para casos normales y casos límite
- Estructura simple y fácil de entender
- Proyecto útil para practicar lógica algorítmica y validación con tests

## Tecnologías usadas

- Python
- Pruebas unitarias con estilo pytest

## Estructura del proyecto

- `busqueda_binaria.py`: implementación del algoritmo
- `test_busqBina.py`: pruebas unitarias del algoritmo

## Cómo funciona

La búsqueda binaria reduce el espacio de búsqueda a la mitad en cada iteración.  
Para que funcione correctamente, la lista de entrada debe estar ordenada.

## Ejemplo de uso

```python
from busqueda_binaria import busqueda_binaria

numeros =[1][2][3][4]
resultado = busqueda_binaria(numeros, 30)
print(resultado)  # 2
```

## Cobertura de pruebas

Las pruebas incluidas validan los siguientes escenarios:

- Elemento encontrado en la mitad
- Elemento encontrado en la primera posición
- Elemento encontrado en la última posición
- Elemento no encontrado
- Lista vacía
- Lista con un solo elemento
- Lista con elementos duplicados
