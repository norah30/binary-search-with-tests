# Búsqueda Binaria con Pruebas

Implementación en Python del algoritmo de búsqueda binaria, acompañada de pruebas automatizadas para casos comunes y casos límite.

## Descripción general

Este proyecto muestra cómo funciona la búsqueda binaria sobre listas ordenadas y cómo validar su comportamiento mediante pruebas. Incluye escenarios en los que el valor se encuentra en distintas posiciones, así como casos donde no existe en la lista, la lista está vacía, solo contiene un elemento o presenta valores duplicados.

## Características

- Implementación del algoritmo de búsqueda binaria en Python
- Pruebas para casos normales y casos límite
- Estructura simple y fácil de entender
- Proyecto orientado a la práctica de lógica algorítmica y validación de resultados

## Tecnologías usadas

- Python
- Pruebas automatizadas basadas en funciones `test_*` y sentencias `assert`

## Estructura del proyecto

- `busqueda_binaria.py`: implementación del algoritmo
- `test_busqBina.py`: pruebas del algoritmo

## Cómo funciona

La búsqueda binaria divide el espacio de búsqueda en cada iteración para localizar un valor de forma eficiente.  
Este algoritmo solo funciona correctamente si la lista de entrada está ordenada. [web:144][web:147]

## Ejemplo de uso

```python
from busqueda_binaria import busqueda_binaria

numeros =[3][4][5][6]
resultado = busqueda_binaria(numeros, 30)
print(resultado)  # 2
```

## Cobertura de pruebas

Las pruebas incluidas validan los siguientes escenarios:

- Elemento encontrado en el centro
- Elemento encontrado en la primera posición
- Elemento encontrado en la última posición
- Elemento no encontrado
- Lista vacía
- Lista con un solo elemento
- Lista con elementos duplicados

## Ejecución local

```bash
git clone <URL-del-repositorio>
cd binary-search-with-tests
python -m pytest
```

<!-- actualizado -->
