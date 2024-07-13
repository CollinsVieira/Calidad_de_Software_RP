import pytest
from Casos.calculadora import suma, resta, multiplicacion, division, validar_numero

################################################################
######## Tests ##########
def test_validar_numero_entero_positivo():
    assert validar_numero(5) == 5

def test_validar_numero_flotante_positivo():
    assert validar_numero(3.14) == 3.14

def test_validar_numero_negativo():
    with pytest.raises(ValueError, match="Solo se permiten números positivos"):
        validar_numero(-5)

def test_validar_numero_no_numerico():
    with pytest.raises(ValueError, match="Solo se permiten números positivos"):
        validar_numero("texto")

def test_suma():
    assert suma(3, 5) == 8

def test_resta():
    assert resta(10, 3) == 7

def test_multiplicacion():
    assert multiplicacion(2, 4) == 8

def test_division():
    assert division(10, 2) == 5

def test_division_por_cero():
    with pytest.raises(ValueError, match="No se puede dividir entre cero"):
        division(8, 0)

