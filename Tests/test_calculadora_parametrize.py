import pytest
from Casos.calculadora import suma, resta, multiplicacion, division, validar_numero

testpm_suma = [
    (2, 3, 5),
    (-2, 3, ValueError),
    (2.5, 3.5, 6.0),
]

testpm_resta = [
    (5, 3, 2),
    (2, -3, ValueError),
    (10.5, 5.5, 5.0),
]

testpm_multiplicacion = [
    (2, 3, 6),
    (-2, 3, ValueError),
    (2.5, 3, 7.5),
]

testpm_division = [
    (6, 3, 2),
    (10, 0, ValueError),
    (7.5, 2.5, 3.0),
]

@pytest.mark.parametrize("num", ["texto", None, {}])
def test_validar_numero_no_numerico(num):
    with pytest.raises(ValueError, match="Solo se permiten números positivos"):
        validar_numero(num)

@pytest.mark.parametrize("a, b, expected", testpm_suma)
def test_suma(a, b, expected):
    if isinstance(expected, type):
        with pytest.raises(expected):
            suma(a, b)
    else:
        assert suma(a, b) == expected

@pytest.mark.parametrize("a, b, expected", testpm_resta)
def test_resta(a, b, expected):
    if isinstance(expected, type):
        with pytest.raises(expected):
            resta(a, b)
    else:
        assert resta(a, b) == expected

@pytest.mark.parametrize("a, b, expected", testpm_multiplicacion)
def test_multiplicacion(a, b, expected):
    if isinstance(expected, type):
        with pytest.raises(expected):
            multiplicacion(a, b)
    else:
        assert multiplicacion(a, b) == expected

@pytest.mark.parametrize("a, b, expected", testpm_division)
def test_division(a, b, expected):
    if isinstance(expected, type):
        with pytest.raises(expected):
            division(a, b)
    else:
        assert division(a, b) == expected
