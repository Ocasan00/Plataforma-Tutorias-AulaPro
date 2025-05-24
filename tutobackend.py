from collections import defaultdict
from datetime import datetime

class Estudiante:
    def __init__(self, nombre, edad, materias_interes):
        self.nombre = nombre
        self.edad = edad
        self.materias_interes = materias_interes
        self.progreso = defaultdict(list)  

   #Funcion para dar nota en una materia
    def agregar_nota(self, materia, nota):
        self.progreso[materia].append(nota)


    def __str__(self):
        return f"Estudiante: {self.nombre}, Edad: {self.edad}, Interés: {self.materias_interes}"

class Tutor:
    def __init__(self, nombre, especialidades, disponibilidad):
        self.nombre = nombre
        self.especialidades = especialidades 
        self.disponibilidad = disponibilidad  
        self.sesiones = 0

    # Funcion para verificar si el tutor está disponible en una fecha y hora específicas

    def esta_disponible(self, fecha, hora):
        fecha_hora = f"{fecha} {hora}"
        return fecha_hora in self.disponibilidad
    
    # Funcion para asignar un horario a una tutoría y actualizar la disponibilidad

    def asignar_horario(self, fecha, hora):
        fecha_hora = f"{fecha} {hora}"
        self.disponibilidad.remove(fecha_hora)
        self.sesiones += 1

    def __str__(self):
        return f"Tutor: {self.nombre}, Especialidades: {self.especialidades}, Disponible: {self.disponibilidad}"

class Tutoria:
    def __init__(self, estudiante, tutor, fecha, hora, materia):
        self.estudiante = estudiante
        self.tutor = tutor
        self.fecha = fecha
        self.hora = hora
        self.materia = materia

    def __str__(self):
        return f"Tutoría de {self.estudiante.nombre} con {self.tutor.nombre} - {self.materia} el {self.fecha} a las {self.hora}"

class Busqueda:
    def __init__(self, plataforma):
        self.plataforma = plataforma

    #Funcion para buscar tutorias por nombre de estudiante

    def por_estudiante(self, nombre):
        return [t for t in self.plataforma.tutorias if t.estudiante.nombre == nombre]
    
    #Funcion para buscar tutorias por nombre de tutor

    def por_tutor(self, nombre):
        return [t for t in self.plataforma.tutorias if t.tutor.nombre == nombre]
    
    #Funcion para buscar tutorias por nombre de materia

    def por_materia(self, materia):
        return [t for t in self.plataforma.tutorias if t.materia == materia]

class Plataforma:
    def __init__(self):
        self.estudiantes = []
        self.tutores = []
        self.tutorias = []
        self.busqueda = Busqueda(self)

    #Funciones para registrar un estudiante y tutor nuevo en la plataforma

    def registrar_estudiante(self, nombre, edad, materias_interes):
        estudiante = Estudiante(nombre, edad, materias_interes)
        self.estudiantes.append(estudiante)
        return estudiante

    def registrar_tutor(self, nombre, especialidades, disponibilidad):
        tutor = Tutor(nombre, especialidades, disponibilidad)
        self.tutores.append(tutor)
        return tutor
    
    # Función para agendar una tutoría entre un estudiante y un tutor

    def agendar_tutoria(self, estudiante, tutor, fecha, hora, materia):
        if estudiante not in self.estudiantes:
            raise ValueError(f"El estudiante {estudiante.nombre} no está registrado.")
        if tutor not in self.tutores:
            raise ValueError(f"El tutor {tutor.nombre} no está registrado.")

        if not tutor.esta_disponible(fecha, hora):
            raise ValueError(f"{tutor.nombre} no está disponible el {fecha} a las {hora}.")

        if materia not in tutor.especialidades:
            raise ValueError(f"{tutor.nombre} no tiene {materia} como especialidad.")
        
        #Crea la tutoria y actualiza los datos

        tutoria = Tutoria(estudiante, tutor, fecha, hora, materia)
        self.tutorias.append(tutoria)

        tutor.asignar_horario(fecha, hora)

        return tutoria
    
    # Funcion para obtener tutores que imparten una materia específica
    
    def obtener_tutores_por_materia(self, materia):
        return [tutor for tutor in self.tutores if materia.lower() in [m.lower() for m in tutor.especialidades]]
    
    # Funcion para obtener los horarios disponibles de un tutor en específico

    def obtener_disponibilidades_tutor(self, nombre_tutor):
        tutor = next((t for t in self.tutores if t.nombre == nombre_tutor), None)
        if tutor:
            return tutor.disponibilidad
        return []
    
    # Funcon para obtener tutores disponibles para una materia y fecha 
    def obtener_tutores_disponibles(self, materia, fecha):
        tutores_filtrados = []
        for tutor in self.obtener_tutores_por_materia(materia):
            
            disponibles_en_fecha = [d for d in tutor.disponibilidad if d.startswith(fecha)]
            if disponibles_en_fecha:
                tutores_filtrados.append((tutor, disponibles_en_fecha))
        return tutores_filtrados
    
    # Funcion para generar un reporte de las materias más solicitadas ordenadas de mayor a menor

    def reporte_materias_mas_solicitadas(self):
        contador = defaultdict(int)
        for tutoria in self.tutorias:
            contador[tutoria.materia] += 1
        return sorted(contador.items(), key=lambda x: x[1], reverse=True)
    
    # Función para generar un reporte de los tutores más activos ordenados por sesiones impartidas

    def reporte_tutores_mas_activos(self):
        return sorted(self.tutores, key=lambda t: t.sesiones, reverse=True)
    
    #Funcion para generar reporte del progreso academico de los estudiantes con su promedio

    def reporte_progreso_estudiantes(self):
        reportes = []
        for estudiante in self.estudiantes:
            reporte = f"\n{estudiante.nombre}"
            for materia, notas in estudiante.progreso.items():
                promedio = sum(notas) / len(notas) if notas else 0
                reporte += f"\n  {materia}: Promedio {promedio:.2f}"
            reportes.append(reporte)
        return "\n".join(reportes)
    
    # Funcion para registrar una nota del progreso académico

    def registrar_progreso(self, estudiante, materia, nota):
        if estudiante not in self.estudiantes:
            raise ValueError(f"El estudiante {estudiante.nombre} no está registrado.")
        estudiante.agregar_nota(materia, nota)



