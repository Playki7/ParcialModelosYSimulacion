class ExperienciaCalificada():
    def __init__(self,cargo,tiempoExperiencia):
        self.cargo=cargo
        self.tiempoExperiencia=tiempoExperiencia
    
    def calcularPuntaje(self):
        puntaje=self.tiempoExperiencia*self.calcular_valorPuntoAnual()
        if (puntaje<=self.calcular_puntosMaximo()):
            totalPuntos=puntaje
        else:
            totalPuntos=self.calcular_puntosMaximo()

        return totalPuntos
    
    def calcular_puntosMaximo(self):
        match self.cargo:
            case 1:
                puntosMaximo=20
            case 2:
                puntosMaximo=45
            case 3:
                puntosMaximo=90
            case 4:
                puntosMaximo=120
            case _:
                puntosMaximo=1

        return puntosMaximo
    
    def calcular_valorPuntoAnual(self):
        match self.cargo:
            case 1:
                valorPunto_porAño=6
            case 2:
                valorPunto_porAño=4
            case 3:
                valorPunto_porAño=4
            case 4:
                valorPunto_porAño=3
            case _:
                valorPunto_porAño=1

        return valorPunto_porAño

class RegimenExperienciaCalificada(ExperienciaCalificada):
    def __init__(self, cargo, tiempoExperiencia):
        super().__init__(cargo, tiempoExperiencia)

    def calcularPuntaje(self):
        puntaje=self.tiempoExperiencia*self.calcular_valorPuntoAnual()
        if (puntaje<=self.calcular_puntosMaximo()):
            totalPuntos=puntaje
        else:
            totalPuntos=self.calcular_puntosMaximo()
        return totalPuntos
    
    def calcular_valorPuntoAnual(self):
        match self.cargo:
            case 1:
                valorPunto_porAño=3
            case 2:
                valorPunto_porAño=5
            case 3:
                valorPunto_porAño=6
            case 4:
                valorPunto_porAño=7
            case _:
                valorPunto_porAño=0
        
        return valorPunto_porAño
