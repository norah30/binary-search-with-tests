def busqueda_binaria(arr: list[int], objetivo: int) -> int:
    """
    Busca un valor en una lista ordenada usando búsqueda binaria.

    Args:
        arr: Lista ordenada de enteros.
        objetivo: Valor que se desea encontrar.

    Returns:
        El índice del valor encontrado o -1 si no existe en la lista.
    """
    bajo = 0
    alto = len(arr) - 1

    while bajo <= alto:
        medio = (bajo + alto) // 2

        if arr[medio] == objetivo:
            return medio

        if arr[medio] < objetivo:
            bajo = medio + 1
        else:
            alto = medio - 1

    return -1
