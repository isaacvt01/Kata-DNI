from src.TablaAsignacion import TablaAsignacion


class Dni:
    def __init__(self, numero, cadena=''):
        self.dni = numero + cadena
        self.numero = numero
        self.letra = cadena
        self.tabla = TablaAsignacion()

    def ponerLetraDNI(self):
        if self.numero.isdigit():
            self.letra = self.tabla.calcularLetra(self.dni)
            self.dni = self.numero + self.letra
            return self.dni
        else:
            return 'Solo se aceptan números'

    def checkLargoDNI(self):
        return len(self.numero) == 8 and len(self.letra) == 1

    def checkNumerosDNI(self):
        return self.numero.isdigit()

    def checkLetraDNI(self):
        return self.letra == self.tabla.calcularLetra(self.numero)

    def checkDNICompleto(self):
        return self.checkLargoDNI() and self.checkNumerosDNI() and self.checkLetraDNI()

    def completarDNI(self):
        if self.letra == '':
            return self.ponerLetraDNI()




