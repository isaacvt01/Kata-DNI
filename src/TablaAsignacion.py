class TablaAsignacion:

    def __init__(self):
        self.tabla = ['T', 'R', 'W', 'A', 'G', 'M', 'Y', 'F', 'P', 'D', 'X', 'B', 'N', 'J', 'Z', 'S', 'Q', 'V', 'H',
                      'L', 'C', 'K', 'E']

    def getNumeroDivisoresDNI(self):
        return len(self.tabla)

    def getLetra(self, posicion):
        return self.tabla[posicion]

    def calcularLetra(self, DNI):
        posicion = int(DNI) % self.getNumeroDivisoresDNI()
        return self.getLetra(posicion)
