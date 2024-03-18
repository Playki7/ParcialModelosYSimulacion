class ProductividadAcademica():
    
    def __init__(self,tipoProduccion,autores):
        self.tipoProduccion=tipoProduccion
        self.autores=autores

    def calcularPuntaje():
        pass

class RevistaEspecializada(ProductividadAcademica):

    def __init__(self, tipoProduccion,categoría,cantidad,autores):
        super().__init__(tipoProduccion,autores)
        self.categoría=categoría
        self.cantidad=cantidad
    
    def calcularPuntos():
        pass

    def calcular_puntosProduccion(self): 
        match self.tipoProduccion:
            case 1:
                puntosProduccion=15
            case 2:
                puntosProduccion=12
            case 3:
                puntosProduccion=8
            case 4: 
                puntosProduccion=3
            case _:
                puntosProduccion=0
    
        return puntosProduccion

class Artículo(RevistaEspecializada):

    def __init__(self, tipoProduccion, categoría, cantidad,autores):
        super().__init__(tipoProduccion, categoría, cantidad,autores)

    def calcular_puntosProduccion(self): 
        match self.tipoProduccion:
            case 1:
                puntosProduccion=15
            case 2:
                puntosProduccion=12
            case 3:
                puntosProduccion=8
            case 4: 
                puntosProduccion=3
            case _:
                puntosProduccion=0
    
        return puntosProduccion
    
    def calcularPuntos(self):
        puntosPorProduccion = self.calcular_puntosProduccion()*self.cantidad

        return puntosPorProduccion

class OtrasModalidades(RevistaEspecializada):

    def __init__(self, tipoProduccion, categoría, cantidad,autores):
        super().__init__(tipoProduccion, categoría, cantidad,autores)

    def calcularPuntos(self):
        puntosPorProduccion = (self.calcular_puntosProduccion()*self.calcular_porcentajePuntos)*self.cantidad

        return puntosPorProduccion

    def calcular_puntosProduccion(self):
        match self.tipoProduccion:
            case 1:
                puntosProduccion=15
            case 2:
                puntosProduccion=12
            case 3:
                puntosProduccion=8
            case 4: 
                puntosProduccion=3
            case _:
                puntosProduccion=0
    
        return puntosProduccion

    def calcular_porcentajePuntos(self):
        match self.categoría:
            case 1:
                porcentaje=1
            case 2:
                porcentaje=0.6
            case 3:
                porcentaje=0.3
            case _:
                porcentaje=0

        return porcentaje
    
class ProduccionVideos(ProductividadAcademica):

    topeMaximo=5
    
    def __init__(self,autores,alcance,categoria,cantidad):
        super().__init__(autores)
        self.alcance=alcance
        self.categoria=categoria
        self.cantidad=cantidad

    def calcularPuntaje(self):

        if (self.cantidad<=self.topeMaximo):
            cantidad=self.cantidad
        else:
            cantidad=self.topeMaximo

        puntaje=self.calcular_valorPunto()*self.calcularCategoria

        return puntaje


    def calcular_valorPunto(self):
        match  self.alcance:
            case 1:
                valorPunto=12
            case 2: 
                valorPunto=7
            case _:
                valorPunto=0

        return  valorPunto
    
    def calcularCategoria(self):
        match self.categoria:
            case 1:
                valorPorcentaje=1
            case 2:
                valorPorcentaje=0.8
            case _3:
                valorPorcentaje=0

        return valorPorcentaje

class Libros(ProductividadAcademica):

    def __init__(self, tipoProduccion, autores,categoria,cantidad):
        super().__init__(tipoProduccion, autores)
        self.categoria=categoria
        self.cantidad=cantidad

    def calcular_valorPuntos(self):
        match self.tipoProduccion:
            case 1:
                valorPuntos=20
            case 2:
                valorPuntos=15
            case _:
                valorPuntos=0

        return valorPuntos

    def calcular_porcentajePorCategoria(self):
        match self.categoria:
            case 1:
                valorPorcentaje=1
            case 2:
                valorPorcentaje=0.8
            case _:
                valorPorcentaje=0
        
        return valorPorcentaje
    
    def calcularPuntaje(self):
        
        puntaje = self.calcular_porcentajePorCategoria()*self.calcular_valorPuntos()*self.cantidad

        return puntaje
    
class Premios(ProductividadAcademica):

    puntosPremio=15

    def __init__(self, tipoProduccion,autores, categoria,cantidad):
       super().__init__(tipoProduccion,autores)
       self.categoria=categoria
       self.cantidad=cantidad

    def calcular_valorPorcategoria(self):
       
       valorPorCategoria=self.puntosPremio/self.autores

       return valorPorCategoria

    def calcularPuntaje(self):

        posicion=self.autores/self.categoria
        puntaje=self.calcular_valorPorcategoria()*posicion(self.cantidad)

        return puntaje

class Patentes():

    valorPorPatente=25

    def __init__(self,cantidad):
        self.cantidad=cantidad
    
    def calcularPuntaje(self):
        puntaje=self.valorPorPatente*self.cantidad

        return puntaje

class TraduccionesLibros():

    valorTraduccionLibro=15

    def __init__(self,cantidad):
        self.cantidad=cantidad

    def calcularPuntaje(self):
        puntaje=self.valorTraduccionLibro*self.cantidad

        return puntaje

class ObrasArtísticas(ProductividadAcademica):

    def __init__(self,tipoProduccion,alcance,cantidad):
        super().__init__(tipoProduccion)
        self.alcance=alcance
        self.cantidad=cantidad

    def calcular_valorPunto():
        pass

class Original(ObrasArtísticas):

    valorPunto_internacional=20
    valorPunto_nacional=14

    def __init__(self, tipoProduccion, alcance, cantidad):
        super().__init__(tipoProduccion, alcance, cantidad)

    def calcular_valorPunto(self):
        match super().alcance:
            case 1:
                valorObra=self.valorPunto_internacional
            case 2:
                valorObra=self.valorPunto_nacional
            case _:
                valorObra=0

        return valorObra
    
    def calcularPuntaje(self):
        puntaje=self.calcular_valorPunto()*self.cantidad

        return puntaje
    
class Complementaria(ObrasArtísticas):
    valorPunto_internacional=12
    valorPunto_nacional=8

    def __init__(self, tipoProduccion, alcance, cantidad):
        super().__init__(tipoProduccion, alcance, cantidad)

    def calcular_valorPunto(self):
        match super().alcance:
            case 1:
                valorObra=self.valorPunto_internacional
            case 2:
                valorObra=self.valorPunto_nacional
            case _:
                valorObra=0

        return valorObra
    
    def calcularPuntaje(self):
        puntaje=self.calcular_valorPunto()*self.cantidad

        return puntaje

class Interpretacion(ObrasArtísticas):

    valorPunto_internacional=14
    valorPunto_nacional=8

    def __init__(self, tipoProduccion, alcance, cantidad):
        super().__init__(tipoProduccion, alcance, cantidad)

    def calcular_valorPunto(self):
        match super().alcance:
            case 1:
                valorObra=self.valorPunto_internacional
            case 2:
                valorObra=self.valorPunto_nacional
            case _:
                valorObra=0

        return valorObra
    
    def calcularPuntaje(self):
        puntaje=self.calcular_valorPunto()*self.cantidad

        return puntaje
    
class ProduccionTecnica(ProductividadAcademica):

    valor_puntoInnovacion=15
    valor_puntoAdaptacion=8

    def __init__(self, tipoProduccion, autores,cantidad,categoria):
        super().__init__(tipoProduccion, autores)
        self.cantidad=cantidad
        self.categoria=categoria

    def calcular_valorPunto(self):
        match self.categoria:
            case 1:
                valorPunto=self.valor_puntoInnovacion
            case 2:
                valorPunto=self.valor_puntoAdaptacion
            case _:
                valorPunto=0
        
        return valorPunto
    
class produccionSoftware(ProductividadAcademica):

    valor_puntosSoftware=15

    def __init__(self, tipoProduccion, autores,cantidad):
        super().__init__(tipoProduccion, autores)
        self.cantidad=cantidad

    def calcularPuntaje(self):
        puntaje = self.valor_puntosSoftware*self.cantidad

        return puntaje
