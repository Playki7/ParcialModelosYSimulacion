class Docente():

    def __init__(self,tipoDocente):
        self.tipoDocente=tipoDocente

    def calcular_puntosDocente(self):
        match self.tipoDocente:
            case 1:
                puntosDocente=37
            case 2:
                puntosDocente=44
            case 3:
                puntosDocente=58
            case 4:
                puntosDocente=74
            case 5:
                puntosDocente=96
            case _:
                return 0

        return puntosDocente