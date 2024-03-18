import  estudiosUniversitarios 
import  experienciaCalificada
import  escalafonDocente
import  productividadAcademica

class Docente():



    def __init__(self,carrera,cargo,regimen,valorPunto):
        self.carrera=carrera
        self.cargo=cargo
        self.regimen=regimen
        self.valorPunto=valorPunto

    def calcular_puntosPregrado():
        puntosPregrado=estudiosUniversitarios.Pregrado.calcular_puntosPregrado(carrera)

        return puntosPregrado
    
    def calcular_puntosPosgrado(self,tiempoEspecializacion1,tiempoEspecializacion2,cantidadMagister,cantidadDoctorado):
        puntos_tempEspecializacionMagister=self.calcular_puntosEspecializacion(tiempoEspecializacion1,tiempoEspecializacion2)+self.calcular_puntosMagister(cantidadMagister)

        if (puntos_tempEspecializacionMagister<=60):
            puntos_especializacionMagister=puntos_tempEspecializacionMagister
        else:
            puntos_especializacionMagister=60
        
        puntos_doctorado=self.calcular_puntosDoctorado(cantidadDoctorado)

        puntosPosgrado=puntos_especializacionMagister+puntos_doctorado

        if(puntosPosgrado>140):
            puntosPosgrado=140
        
        return puntosPosgrado

    def calcular_puntosEspecializacion(tiempoEspecializacion1,tiempoEspecializacion2)
        puntosEspecializacion=estudiosUniversitarios.Especializacion.calcular_puntosEspecializacion(carrera,tiempoEspecializacion1,tiempoEspecializacion2)

        return puntosEspecializacion

    def calcular_puntosMagister(cantidadMagister):
         puntosMagister=estudiosUniversitarios.Magister.calcular_puntosMagister(cantidadMagister)

         return puntosMagister
    
    def calcular_puntosDoctorado(cantidadDoctorado):
        puntosDoctorado=estudiosUniversitarios.Doctorado.calcular_puntosDoctorado(cantidadDoctorado)

        return puntosDoctorado
    
    def calrcular_puntosCargo(self,cargo)

carrera_str=input("Seleccione:\n1-Pegrado no clinico\n2-Pregrado clinico\n->")

if(int(carrera_str)==1):
    carrera=True
else:
    carrera=False

cargo_str=input("Seleccione en el cargo \n1-Profesor Auxiliar,Instructor Asistente\n2-Instructor Asosciado\n3-Profesor Asistente\n4-Profesor Asociado\n5-Profesor Titular\n->")

regimen_str=input("Seleccione el regimen el cual estaba\n1-Nuevo\n2-1444\n3-Diferente\n->")

valorPunto_str=input("Digite el valor punto para este año\n->")

especializacion_str=input("Hizo especializaciones\n1-Si\2-No\n->")


profesor = Docente(carrera=carrera,cargo=int(cargo_str),regimen=int(regimen_str),valorPunto=int(valorPunto_str))

profesorPregrado = estudiosUniversitarios.Pregrado(tipoPregrado=carrera)
profesorEspecializacion = estudiosUniversitarios.Especializacion(tiempoEspecializacion1=tiempoEspecializacion,tiempoEspecializacion2=tiempoEspecializacion2)
profesorMagister = estudiosUniversitarios.Magister(cantidadDeMagister=cantidadMagisters)
profesorDoctorado = estudiosUniversitarios.Doctorado(cantidadDoctorados=cantidadDoctorado)
profesorExperiencia_sinRegimen = experienciaCalificada.ExperienciaCalificada(cargo=cargo_str)
profesorExperiencia_conRegimen = experienciaCalificada.RegimenExperienciaCalificada(cargo=cargo_str)
profesorCargo = escalafonDocente.Docente(tipoDocente=cargo_str)
profesorArticulo = productividadAcademica.Artículo(tipoProduccion=produccion,categoría=categoria,cantidad=cantidad,autores=autores)
profesorOtrasModalidades = productividadAcademica.OtrasModalidades(tipoProduccion=categoria,categoría=categoria,cantidad=cantidad,autores=autores)
profesorProduccionVideos = productividadAcademica.ProduccionVideos(autores=autores,alcance=alcance,cantidad=cantidad,categoria=categoria)
profesorLibros






