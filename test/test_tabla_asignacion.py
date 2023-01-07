import pytest
from src.TablaAsignacion import TablaAsignacion


@pytest.fixture()
def tabla():
    tabla = TablaAsignacion()
    return tabla


def test_get_num_divisores(tabla):
    assert 23 == tabla.getNumeroDivisoresDNI()


def test_tabla(tabla):
    posicion = 45608961 % 23
    assert 'F' == tabla.getLetra(posicion)


def test_calcular_letra(tabla):
    assert 'F' == tabla.calcularLetra(45608961)
    assert 'D' == tabla.calcularLetra(45371902)
