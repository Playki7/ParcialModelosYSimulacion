class Pregrado():

    def __init__(self, tipoPregrado):
        self.tipoPregrado = tipoPregrado

    def calcular_puntosPregrado(tipoPregado):
        if (tipoPregado):
            puntosPregrado=178
        else:
            puntosPregrado=185

        return puntosPregrado

class Especializacion():

    tiempoMinimo_especializacion=2
    puntajeMinimo_especializacion=20
    clinica_valorPorAño_especializacion=15
    noClinica_valorPorAño_especializacion=10
    clinica_topeMaximo_especializacion=75
    noClinica_topeMaximo_especializacion=30

    def __init__(self,tipoEspecializacion,tiempoEspecializacion1,tiempoEspecializacion2=0):
        self.tipoEspecializacion = tipoEspecializacion
        self.tiempoEspecializacion1 = tiempoEspecializacion1
        self.tiempoEspecializacion2 = tiempoEspecializacion2
    
    def calcular_puntosEspecializacion(self):
        totalPuntosEspecializacion = 0
        if (self.tipoEspecializacion):
            totalPuntosEspecializacion= self.calcular_puntosClinicas(self.tiempoEspecializacion1)
        else:
            tiempoTotal=self.tiempoEspecializacion1+self.tiempoEspecializacion2
            totalPuntosEspecializacion = self.calcular_puntosNoClinicas(tiempoTotal)       
            
        return totalPuntosEspecializacion  


    def calcular_puntosClinicas(self,tiempoEspecializacion):
        if (tiempoEspecializacion<=Especializacion.tiempoMinimo_especializacion):
            puntosEspecializacion = Especializacion.puntajeMinimo_especializacion
        else:
            periodoExcedente=tiempoEspecializacion-self.tiempoMinimo_especializacion
            puntosEspecializacion = self.puntajeMinimo_especializacion+(periodoExcedente*self.clinica_valorPorAño_especializacion)
            if puntosEspecializacion>self.clinica_topeMaximo_especializacion:
                puntosEspecializacion=self.clinica_topeMaximo_especializacion

        return puntosEspecializacion 
    

    def calcular_puntosNoClinicas(self,tiempoEspecializacion):

        if (tiempoEspecializacion<self.tiempoMinimo_especializacion):
            puntosEspecializacion=self.puntajeMinimo_especializacion
        else:
            periodoExcedente=tiempoEspecializacion-self.tiempoMinimo_especializacion

            puntosEspecializacion=self.puntajeMinimo_especializacion+(periodoExcedente*self.noClinica_valorPorAño_especializacion)
            if (puntosEspecializacion>self.noClinica_topeMaximo_especializacion):
                puntosEspecializacion=self.noClinica_topeMaximo_especializacion
        
        return puntosEspecializacion

class Magister():

    maxima_cantidad_magister=2
    puntosMinimos_magister=40
    puntosAdicionales_magister=20
    puntosTope_magister=60

    def __init__(self,cantidadDeMagister):
        self.cantidadMagister = cantidadDeMagister

    def calcular_puntosMagister(self):
        if (self.cantidadMagister<self.maxima_cantidad_magister):
            puntosMagister=self.puntosMinimos_magister
        else:
            puntosMagister=self.puntosMinimos_magister+self.puntosAdicionales_magister
            if(puntosMagister>self.puntosTope_magister):
                puntosMagister=self.puntosTope_magister

        return puntosMagister  
      
class Doctorado():

    puntosMinimo=80
    puntosMinimo_conMagister=120
    puntosAdicionales=20
    puntosTope_sinMaestría=120
    puntosTope_conMaestría=140
    maximoDoctorados=2

    def __init__(self,cantidadDoctorados,tieneMaestria):
        self.cantidadDoctorados=cantidadDoctorados
        self.tieneMaestria=tieneMaestria

    def calcular_puntosDoctorado(self):
        if (self.tieneMaestria):
            puntosDoctorado=self.calcularPuntaje_conMaestria()
        else:
            puntosDoctorado=self.calcularPuntaje_sinMaestria()

        return puntosDoctorado
    
    def calcularPuntaje_conMaestria(self):
        if (self.cantidadDoctorados<self.maximoDoctorados):
            puntosDoctorado_conMagister=self.puntosMinimo_conMagister
        else:
            puntosDoctorado_conMagister=self.puntosMinimo_conMagister+self.puntosAdicionales

        return puntosDoctorado_conMagister
    
    def calcularPuntaje_sinMaestria(self):
        if (self.cantidadDoctorados<self.maximoDoctorados):
            puntosDoctorado_sinMagister=self.puntosMinimo
        else:
            puntosDoctorado_sinMagister=self.puntosMinimo+self.puntosAdicionales

        return puntosDoctorado_sinMagister