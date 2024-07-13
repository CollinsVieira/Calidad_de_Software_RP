import pytest
from Casos.sopa_de_letras import *

# Pruebas para validar_palabras
@pytest.mark.parametrize("n, palabras, expected", [
    (5, ['CASA', 'PERRO', 'GATO'], True),
    (5, ['CASA', 'PERRO@', 'GATO'], False),
    (5, ['CASA', 'PERRO#', 'GATO'], False),
    (5, ['CASA', 'PERRO$', 'GATO'], False),
    (5, ['CASA', 'PERRO2', 'GATO'], False),
    (5, ['CASA', 'PERRO', 'GATO3'], False),
    (4, ['CASA', 'PERRO', 'GATO'], False),
    (5, ['CASA', 'PERRO', 'GATOS'], True)
])
def test_validar_palabras(n, palabras, expected):
    assert validar_palabras(n, palabras) == expected

# Pruebas para validar_numero
@pytest.mark.parametrize("input, expected", [
    (5, 5),
    ('10', 10)
])
def test_validar_numero_valido(input, expected):
    assert validar_numero(input) == expected

# Pruebas para crear_sopa_de_letras
@pytest.mark.parametrize("n, palabras", [
    (10, []),
    (10, ['CASA', 'PERRO', 'GATO'])
])
def test_creacion_sopa_valida(n, palabras):
    # No debería lanzar ninguna excepción
    crear_sopa_de_letras(n, palabras)

@pytest.mark.parametrize("n, palabras", [
    (10, ['CASA', 'PERRO@', 'GATO']),
    (10, ['CASA', 'PERRO#', 'GATO']),
    (10, ['CASA', 'PERRO$', 'GATO'])
])
def test_creacion_sopa_con_caracteres_especiales(n, palabras):
    with pytest.raises(ValueError, match=r".*caracteres especiales.*"):
        crear_sopa_de_letras(n, palabras)
