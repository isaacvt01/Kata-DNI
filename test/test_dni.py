from src.dni import Dni
import pytest


@pytest.fixture()
def crearDNISinLetra():
    dniSinLetra = Dni('45608961')
    return dniSinLetra


@pytest.fixture()
def crearDNICompleto():
    dniCompleto = Dni('45608961', 'F')
    return dniCompleto


def test_poner_letra(crearDNISinLetra):
    dni = Dni('45608961')
    assert '45608961F' == dni.ponerLetraDNI()


def test_check_largo_dni(crearDNISinLetra, crearDNICompleto):
    dniSinLetra = crearDNISinLetra
    dniCompleto = crearDNICompleto
    assert True is dniCompleto.checkLargoDNI()
    assert False is dniSinLetra.checkLargoDNI()


def test_check_numeros_dni():
    dni = Dni('45608961')
    dniMal = Dni('45798e34')

    assert True is dni.checkNumerosDNI()
    assert False is dniMal.checkNumerosDNI()


def test_check_letra_dni():
    dni = Dni('70988461', 'L')
    dniMal = Dni("70988461", "Ñ")

    assert True is dni.checkLetraDNI()
    assert False is dniMal.checkLetraDNI()

def test_completarDNI(crearDNISinLetra):
    dni= crearDNISinLetra

    assert "45608961F" == dni.completarDNI()
