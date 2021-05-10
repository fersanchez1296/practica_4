class alumno1:

    def __init__(self):
        self.__matricula = 0
        self.__nombre = ""
        self.__fecha_nacimiento = ""
        self.__fecha_ingreso = ""
        self.__genero = ""
        self.__ciudad = ""

    def get_matricula(self):
        return self.__matricula

    def get_nombre_alumno(self):
        return self.__nombre

    def get_fecha_nacimiento(self):
        return self.__fecha_nacimiento

    def get_fecha_ingreso(self):
        return self.__fecha_ingreso

    def get_genero(self):
        return self.__genero

    def get_ciudad(self):
        return self.__ciudad

    def calcular_edad(self):
        pass

    def set_matricula(self, matricula):
        self.__matricula = matricula

    def set_nombre_alumno(self, nombre):
        self.__nombre = nombre

    def set_fecha_nacimiento(self, fecha):
        self.__fecha_nacimiento = fecha

    def set_fecha_ingreso(self, fecha):
        self.__fecha_ingreso = fecha

    def set_genero(self, genero):
        self.__genero =  genero

    def set_ciudad(self, ciudad):
        self.__ciudad = ciudad

    def __str__(self):
        return "Nombre->" + self.get_nombre_alumno() + "\n" + \
            "Matricula->" + str(self.get_matricula()) + "\n" + \
            "Fecha Nacimiento->" + str(self.get_fecha_nacimiento()) + "\n" + \
            "Fecha Ingreso->" +  str(self.get_fecha_ingreso()) + "\n" + \
            "Genero->" + self.get_genero() + "\n" + \
            "Ciudad->" + self.get_ciudad() + "\n"


    #******************************************************************************************************



class profesor:
    
    def __init__(self):
        self.__no_empleado = 0
        self.__nombre = ""
        self.__fecha_ingreso = ""

    def get_no_empleado(self):
        return self.__no_empleado
    
    def get_fecha_ingreso(self):
        return self.__fecha_ingreso

    def set_fecha_ingreso(self,fecha):
        self.__fecha_ingreso = fecha

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_nombre_prof(self):
        return self.__nombre

    def set_no_empleado(self,numero):
        self.__no_empleado = numero

    def calcular_antiguedad(self):
        pass


#***********************************************************************************************************

class materia(profesor):

    def __init__(self):
        profesor.__init__(self)
        self.__nombre = ""
        self.__titular = profesor
        self.__lista_alumnos = []

    def agregar_alumno(self,alumno):
        return self.__lista_alumnos.append(alumno)

    def eliminar_alumno(self):
        pass

    def listar_alumnos(self):
        return self.__lista_alumnos

    def set_nombre_mat(self,nombre):
        self.__nombre = nombre

    def get_nombre_mat(self):
        return self.__nombre

    def set_titular(self,profesor):
        self.__titular = profesor
    
    def get_titular(self):
        return self.__titular

    def __str__ (self):
        return "Nombre materia->" + self.get_nombre_mat() 


#************************************************************************************************************

class carrera(materia):

    def __init__(self):
        materia.__init__(self)
        profesor.__init__(self)
        self.__alumnos = []
        self.__nombre = ""
        self.__materias = []

    def agregar_materia(self,materia):
        pass
    
    def eliminar_materia(self):
        pass

    def listar_materias(self):
        return self.__materias

    def get_nombre(self):
        return self.__nombre

    def get_materias(self):
        return self.__materias

    def set_nombre(self,nombre):
        self.__nombre = nombre

    def set_materias(self,materia):
        self.__materias.append(materia)

    def set_alumnos(self, alumnos):
        self.__alumnos.append(alumnos)

    def get_alumnos(self):
        return self.__alumnos

    def __str__(self):
        return "Nombre carrera-> " + self.get_nombre()

