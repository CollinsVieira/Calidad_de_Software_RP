import pytest
from Casos.sopa_de_letras import validar_palabras, crear_sopa_de_letras,validar_numero


# TEst para validar palabras con caracteres especiales que no deben ser aceptadas
def test_validar_palabras_con_caracteres_especiales():
    
    assert validar_palabras(5, ['CASA', 'PERRO', 'GATO']) == True
    assert validar_palabras(5, ['CASA', 'PERRO@', 'GATO']) == False
    assert validar_palabras(5, ['CASA', 'PERRO#', 'GATO']) == False
    assert validar_palabras(5, ['CASA', 'PERRO$', 'GATO']) == False

def test_validar_palabras_con_numeros():
    assert validar_palabras(5, ['CASA', 'PERRO2', 'GATO']) == False
    assert validar_palabras(5, ['CASA', 'PERRO', 'GATO3']) == False

def test_validar_palabras_exceden_longitud():
    assert validar_palabras(4, ['CASA', 'PERRO', 'GATO']) == False
    assert validar_palabras(5, ['CASA', 'PERRO', 'GATOS']) == True

# TEst para intentar crear sopa de letras con caracteres especiales cosa que no debería :v
def test_creacion_sopa_con_caracteres_especiales():
    with pytest.raises(ValueError, match=r".*caracteres especiales.*"):
        crear_sopa_de_letras(10, ['CASA', 'PERRO@', 'GATO'])

    with pytest.raises(ValueError, match=r".*caracteres especiales.*"):
        crear_sopa_de_letras(10, ['CASA', 'PERRO#', 'GATO'])

    with pytest.raises(ValueError, match=r".*caracteres especiales.*"):
        crear_sopa_de_letras(10, ['CASA', 'PERRO$', 'GATO'])
        

def test_validar_numero_no_valido():
    with pytest.raises(ValueError, match="El tamaño de la sopa de letras debe ser un número entero positivo."):
        validar_numero(-1)
    with pytest.raises(ValueError, match="Ingrese un número entero válido para el tamaño de la sopa de letras."):
        validar_numero('abc')