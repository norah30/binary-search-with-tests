from busqueda_binaria import busqueda_binaria


def test_encontrado_en_el_centro():
    assert busqueda_binaria([10, 20, 30, 40, 50], 30) == 2


def test_encontrado_primer_elemento():
    assert busqueda_binaria([10, 20, 30, 40, 50], 10) == 0


def test_encontrado_ultimo_elemento():
    assert busqueda_binaria([10, 20, 30, 40, 50], 50) == 4


def test_no_encontrado():
    assert busqueda_binaria([10, 20, 30, 40, 50], 35) == -1


def test_lista_vacia():
    assert busqueda_binaria([], 5) == -1


def test_unico_elemento_encontrado():
    assert busqueda_binaria([7], 7) == 0


def test_unico_elemento_no_encontrado():
    assert busqueda_binaria([7], 3) == -1


def test_elementos_duplicados():
    resultado = busqueda_binaria([2, 2, 2, 2, 2], 2)
    assert resultado in [0, 1, 2, 3, 4]
