class alumno:

    __matricula = 0
    __nombre = ""
    __fecha_nacimiento = ""
    __fecha_ingreso = ""
    __genero = ""
    __ciudad = ""

    def get_matricula(self):
        return self._matricula

    def get_nombre(self):
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

    def setNombre(nombre):
        self.__nombre = nombre

    def set_fecha_nacimiento(fecha):
        self.__fecha_nacimiento = fecha

    def set_fecha_ingreso(fecha):
        self.__fecha_ingreso = fecha

    def set_genero(genero):
        self.__genero =  genero

    def set_ciudad(ciudad):
        self.__ciudad = ciudad


    #******************************************************************************************************



class profesor:

    __no_empleado = 0
    __nombre = ""
    __fecha_ingreso = ""

    def get_no_empleado(self):
        return self.__no_empleado

    def get_nombre_prof(self):
        return self.__nombre
    
    def get_fecha_ingreso(self):
        return self.__fecha_ingreso

    def set_fecha_ingreso(self,fecha):
        self.__fecha_ingreso = fecha

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_no_empleado(self,numero):
        self.__no_empleado = numero

    def calcular_antiguedad(self):
        pass


#***********************************************************************************************************

class materia(profesor):

    __nombre = ""
    __titular = profesor
    __lista_alumnos = []

    def __init__(self):
        profesor.__init__(self)

    def agregar_alumno(self):
        pass

    def eliminar_alumno(self):
        pass

    def listar_alumnos(self):
        pass

    def set_nombre(self,nombre):
        self.__nombre = nombre

    def get_nombre_mat(self):
        return self.__nombre

    def set_titular(self,profesor):
        self.__titular = profesor
    
    def get_titular(self):
        return self.__titular


#************************************************************************************************************

class carrera(materia):

    __nombre = ""
    __materias = []

    def __init__(self):
        materia.__init__(self)

    def agregar_materia(self,materia):
        #self.set_materias(materia)
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
        self.__materias = materia

