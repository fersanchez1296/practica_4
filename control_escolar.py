"""
Practica #4--->Control escolar

Fernando Sánchez Plascencia--->219341143   
Luis Davis Olvera Aguilera---->219341178
Juan Carlos Duran Zepeda------>219893731
Luis Alberto Ruelas Barbosa--->215537205

Entrega: Mayo 11 2021


Descripcion:
Se te ha contratado como miembro de un equipo de trabajo para que apoyes en el desarrollo de un sistema. 
Dado un diagrama de clases en UML, tu tarea será realizar la implementación de cada una de las clases. 
Como ingeniero y experto en el desarrollo de software, deberás determinar si los atributos y métodos de cada clase 
son suficientes o si debes incluir más atributos o/y métodos.

La empresa que te contrató desea que el sistema les permita registrar carreras, materias, profesores y alumnos. 
Adicionalmente, se espera poder realizar consultas de esta información. Por ejemplo, listar las carreras, listar los alumnos 
de una carrera, listar las materias de una carrera, listar los alumnos de una materia y listar los profesores que imparten 
una misma materia.

La funcionalidad a implemenar es:
   *Registrar carreras.
   *Registrar materias para cada carrera.
   *Registrar alumnos en cada carrera.
   *Inscribir alumnos a las materias.
   *Registrar profesores.
   *Asignar materia(s) a profesor(es)
   *Listar carreras.
   *Listar materias de una carrera.
   *Listar los alumnos de una carrera.
   *Listar los alumnos inscritos a una materia.
   *Listar las materias que imparte un profesor.


Conclusion:

"""



from clases_control_escolar import * #importamos las clases que vamos a utilizar
from datetime import date #libreria necesaria para usar el tipo de dato date para windows
from datetime import datetime#libreria necesaria para usar el tipo de dato date para linux
from colorama import init, Fore, Back, Style #libreria necesaria para cambiar los colores de consola
import os #libreria necesaria para borrar pantalla
init(autoreset=True) #inicializador de la clase colorama

lista_carreras = [] #almacena las carreras
lista_empleado = [] #almacena los empleados
lista_alumnos = [] #almacena los alumnos


def borrarPantalla(): #Definimos la función estableciendo el nombre que queramos para borrar pantalla
    """
    Esta funcion examina el sistema de operativo que usa el usuario y dependiendo
    el sistema, limpia la pantalla de una manera u otra
    """
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")


def pause():
    """
    Utilizamos esta funcion para hacer una pausa y poder ver la informacion
    """
    programPause = input("Press the <ENTER> key to continue...")

def menu_principal():
    """
    Esta funcion es la del menu, retorna una opcion segun sea la eleccion
    del usuario
    """

    borrarPantalla()
    print("1)Registrar carrera",
     "2)Registrar profesor",
     "3)Registrar materias a carrera",
     "4)Registrar alumno a carrera",
     "5)Inscribir/eliminar alumno de una materia",
     "6)Asignar materia a profesor",
     "7)Listar Carerras",
     "8)Listar materias de una carrera",
     "9)Listar alumnos de una carrera", 
     "10)Listar alumnos inscritos a una materia",
     "11)Listar materias de un profesor",
     "12)Salir",
    sep="\n",end="\n\n")
    opcion = int(input("Ingrese la opcion deseada->"))
    return opcion

def validar_cadenas(cadena):
    """
    Esta funcion toma como parametro una cadena para validar que se ingresen unicamente nombres basados
    en el alfabeto. Mediante los metodos join() y split() validamos los espacios entre palabras.
    Retorna la cadena ya validada.
    En caso de que la cadena sea invalida, pedimos al usuario que intente nuevamente y lo recalcamos
    marcando el texto con un color diferente mediante la funcion Fore.color y concatenamos con el texto
    """
    while True:
        validacion = cadena.split()
        validacion = "".join(validacion)
        if validacion != validacion.isalpha() == False:
            print(Fore.RED+"¡¡¡Este nombre no es valido!!!")
            cadena = input(Fore.CYAN+"Intente nuevamente ->")
        else:
            return cadena

def validar_numeros(numero):
    """
    Esta funcion valida las entradas numericas para que solo sean de tipo int()
    si el usuario ingresa algo invalido se le indica su error mediante una excepcion
    retorna un numero
    """
    while True:
        numero = str(numero)
        if numero != numero.isdigit() == False:
            print(Fore.RED+"¡¡¡FORMATO INVALIDO!!!", "NOTA:\nDEBES INGRESAR NUMEROS",sep="\n",end="\n")
            while True:
                try:
                    numero = int(input(Fore.CYAN+"Intente nuevamente ->"))
                    print("")
                except ValueError as error:
                    print(Fore.RED+"{}".format(error),"¡¡¡FORMATO INVALIDO!!!", "NOTA:\nDEBES INGRESAR NUMEROS",sep="\n",end="\n")
                    continue
                else:
                    borrarPantalla()
                    return numero
                break
        else:
            borrarPantalla()
            return int(numero)
            

def main():
    while True:
        opcion = menu_principal()


        if opcion == 1:
            """
            Esta es la opcion de registrar carrera, instanciamos la clase carrera() con el objeto "especialidad"
            comprobamos que lista_carreras no este vacia, y si lo esta, se lo indicamos al usuario.
            utilizamos los metodos get() y set() para obtener y asignar valores a nuestras funciones miembro
            de nuestra clase.
            Podemos ingresar mas de una carrera a la vez, las carreras se agregan a la lista "lista_carreras"
            """
            borrarPantalla()
            print("***REGISTRAR CARRERA***")
            condicion_salida = "si"
            while condicion_salida != "no":
                especialidad = carrera()
                if len(lista_carreras) == 0:
                    nombre_carrera = validar_cadenas(input("Ingrese el nombre de la carrera->"))
                    especialidad.set_nombre(nombre_carrera)
                    lista_carreras.append(especialidad)
                    print(Fore.GREEN+"***CARRERA REGISTRADA CON EXITO***")
                    salir = validar_cadenas(input("Registrar otra carrera? si/no->"))
                    if salir == "si":
                        condicion_salida = "si"
                    else:
                        condicion_salida = "no"
                else:
                    nombre_carrera = validar_cadenas(input("Ingrese el nombre de la carrera->"))
                    for carreras in lista_carreras:
                        if nombre_carrera != carreras.get_nombre():
                            especialidad.set_nombre(nombre_carrera)
                            lista_carreras.append(especialidad)
                            print(Fore.GREEN+"***CARRERA REGISTRADA CON EXITO***")
                            salir = validar_cadenas(input("Registrar otra carrera? si/no->"))
                            if salir == "si":
                                condicion_salida = "si"
                                
                            else:
                                condicion_salida = "no"
                                break
                    else:
                        print(Fore.YELLOW+"¡¡¡Esta carrera ya existe!!!")
                        pause()


        elif opcion == 2:
            """
            Creamos una instancia de profesor() llamada "maestro", comprobamos que la lista_empleado no este vacia, y si
            lo esta se indicamos al usuario, los objetos de tipo profesor() los agregamos a esta lista.
            Utilizamos la clase datetime.now() para obtener la fecha de registro del profesor, ya que al estar
            registrando al profesor es una nueva instancia, la fecha de registro es la fecha en la cual estamos
            registrando al profesor.
            Validamos las entradas con las funciones validadoras declaradas anteriormente.
            No se puede resgistrar un numero_empleado dos veces, tienen que ser unicos, se le indica esto
            al usuario segun sea su entrada
            """
            borrarPantalla()
            maestro = profesor()
            print("***REGISTRAR PROFESOR***")
            if len(lista_empleado) == 0:
                numero_profesor = validar_numeros(input("Ingrese el número de profesor/empleado->"))
                nombre_profesor = validar_cadenas(input("Ingrese el nombre del profesor->"))
                fecha_ingreso = datetime.now()
                print("***NOTA***","Fecha de ingreso {}".format(fecha_ingreso))
                maestro.set_no_empleado(numero_profesor)
                maestro.set_nombre(nombre_profesor)
                maestro.set_fecha_ingreso(fecha_ingreso)
                lista_empleado.append(maestro)
                print(Fore.GREEN+"***EMPLEADO REGISTRADO CON EXITO***")
                pause()
            else:
                numero_profesor = int(input("Ingrese el número de profesor/empleado->"))
                for profe in lista_empleado:
                    if numero_profesor != profe.get_no_empleado():
                        nombre_profesor = validar_cadenas(input("Ingrese el nombre del profesor->"))
                        fecha_ingreso = datetime.now()
                        print("***NOTA***","Fecha de ingreso {}".format(fecha_ingreso))
                        maestro.set_no_empleado(numero_profesor)
                        maestro.set_nombre(nombre_profesor)
                        maestro.set_fecha_ingreso(fecha_ingreso)
                        lista_empleado.append(maestro)
                        print(Fore.GREEN+"***EMPLEADO REGISTRADO CON EXITO***")
                        pause()
                        break
                else:
                    print(Fore.YELLOW+"***ESTE NUMERO DE EMPLEADO YA EXISTE***")
                    pause()


        elif opcion == 3:
            """
            Realizamo una instancia de la clase materia() de nombre asignatura.
            Realizamos las pertinentes validaciones y comprobacion en nuestra listas y posteriormente
            las agregamos mediante los metodos get() y set()
            """
            borrarPantalla()
            print("***REGISTRAR MATERIAS A CARRERA***")
            if len(lista_carreras) == 0:
                print(Fore.YELLOW+"¡¡¡AUN NO HAY MATERIAS REGISTRADAS!!!")
            else:
                for carreras in lista_carreras:
                    print(carreras,end="\n\n")

                nombre_carrera = validar_cadenas(input("Ingrese el nombre de la carrera->"))
                for carreras in lista_carreras:
                    if nombre_carrera == carreras.get_nombre():
                        condicion_salida = "si"
                        while condicion_salida != "no":
                            asignatura = materia()
                            if len(carreras.get_materias()) == 0:
                                nombre_materia = validar_cadenas(input("Ingrese el nombre de la materia->"))
                                asignatura.set_nombre_mat(nombre_materia)
                                carreras.set_materias(asignatura)
                                print(Fore.GREEN+"***MATERIA AGREGADA CON EXITO***")
                                salir = validar_cadenas(input("Registrar otra materia? si/no->"))
                                if salir == "si":
                                    condicion_salida = "si"
                                    
                                else:
                                    condicion_salida = "no"
                                    break
                            else:
                                nombre_materia = validar_cadenas(input("Ingrese el nombre de la materia->"))
                                for materias in carreras.get_materias():
                                    if nombre_materia == materias.get_nombre_mat():
                                        print(Fore.YELLOW+"***ESTA MATERIA YA EXISTE")
                                    else:
                                        asignatura.set_nombre_mat(nombre_materia)
                                        carreras.set_materias(asignatura)
                                        print(Fore.GREEN+"***MATERIA AGREGADA CON EXITO***")
                                        salir = validar_cadenas(input("Registrar otra materia? si/no->"))
                                        if salir == "si":
                                            condicion_salida = "si"
                                            
                                        else:
                                            condicion_salida = "no"
                                            break
                else:
                    print("¡¡¡ESTA CARRERA NO EXISTE***")    
                    pause()    


        elif opcion == 4:
            """
            Realizamos una instancia de la clase alumno() con el objeto estudiante.
            Realizamos las validaciones pertinentes de los datos de entrada y mediante
            los metodos set() y get()  de nuestra clase, actualizamos datos 
            Utilizamos la clase datetime para la fecha de ingreso y fecha de nacimiento
            Podemos registrar varios alumnos a la vez
            """
            borrarPantalla()
            print("***REGISTRAR ALUMNO A CARRERA***")
            if len(lista_carreras) == 0:
                print(Fore.YELLOW+"¡¡¡NO HAY CARRERAS REGISTRADAS AUN***")
                pause
            else:
                for carreras in lista_carreras:
                    print(carreras)
                nombre_carrera = validar_cadenas(input("Ingrese el nombre de la carrera->"))
                for carreras in lista_carreras:
                    if nombre_carrera == carreras.get_nombre():
                        condicion_salida = "si"
                        while condicion_salida != "no":
                            estudiante = alumno1()
                            
                            if len(lista_alumnos) == 0:
                                matricula_alumno = validar_numeros(input("Ingrese la matricula de alumno->"))
                                estudiante.set_matricula(matricula_alumno)

                                nombre_alumno = validar_cadenas(input("Ingrese el nombre de alumno->"))
                                estudiante.set_nombre_alumno(nombre_alumno)

                                dia_nacimiento = validar_numeros(input("Dia nacimiento->"))
                                mes_nacimiento = validar_numeros(input("Mes nacimiento->"))
                                anio_nacimiento = validar_numeros(input("Año nacimiento->"))
                                fecha_nacimiento_alumno = datetime(anio_nacimiento,mes_nacimiento,dia_nacimiento)
                                estudiante.set_fecha_nacimiento(fecha_nacimiento_alumno)

                                fecha_ingreso_alumno = datetime.now()
                                print(Fore.GREEN+"Fecha de ingreso->",fecha_ingreso_alumno)
                                estudiante.set_fecha_ingreso(fecha_ingreso_alumno)

                                genero_alumno = validar_cadenas(input("Genero->"))
                                estudiante.set_genero(genero_alumno)

                                ciudad_alumno = validar_cadenas(input("Ciudad->"))
                                estudiante.set_ciudad(ciudad_alumno)
                                

                                carreras.set_alumnos(estudiante)
                                lista_alumnos.append(estudiante)
                                borrarPantalla()
                                print(matricula_alumno,nombre_alumno,fecha_nacimiento_alumno,fecha_ingreso_alumno,genero_alumno,ciudad_alumno,sep="\n",end="\n")
                                print(Fore.GREEN+"***ESTUDIANTE REGISTRADO CON EXITO***",end="\n\n")
                                pause()
                                salir = validar_cadenas(input("Registrar otro alumno? si/no->"))
                                if salir == "si":
                                    condicion_salida = "si"
                                else:
                                    condicion_salida = "no"
                            else:
                                
                                for matricula in lista_alumnos:
                                    matricula_alumno = validar_numeros(input("Ingrese la matricula de alumno->"))
                                    if matricula_alumno == matricula.get_matricula():
                                        print(Fore.YELLOW+"***ESTA MATRICULA YA EXISTE***")
                                        pause()
                                        continue
                                    estudiante.set_matricula(matricula_alumno)
                                    nombre_alumno = validar_cadenas(input("Ingrese el nombre de alumno->"))
                                    estudiante.set_nombre_alumno(nombre_alumno)
                                    dia_nacimiento = validar_numeros(input("Dia nacimiento->"))
                                    mes_nacimiento = validar_numeros(input("Mes nacimiento->"))
                                    anio_nacimiento = validar_numeros(input("Año nacimiento->"))
                                    fecha_nacimiento_alumno = datetime(anio_nacimiento,mes_nacimiento,dia_nacimiento)
                                    estudiante.set_fecha_nacimiento(fecha_nacimiento_alumno)
                                    fecha_ingreso_alumno = datetime.now()
                                    print(Fore.GREEN+"Fecha de ingreso->",fecha_ingreso_alumno)
                                    estudiante.set_fecha_ingreso(fecha_ingreso_alumno)
                                    genero_alumno = validar_cadenas(input("Genero->"))
                                    estudiante.set_genero(genero_alumno)
                                    ciudad_alumno = validar_cadenas(input("Ciudad->"))
                                    estudiante.set_ciudad(ciudad_alumno)
                                    
                                    carreras.set_alumnos(estudiante)
                                    lista_alumnos.append(estudiante)
                                    borrarPantalla()
                                    print(matricula_alumno,nombre_alumno,fecha_nacimiento_alumno,fecha_ingreso_alumno,genero_alumno,ciudad_alumno,sep="\n",end="\n")
                                    print(Fore.GREEN+"***ESTUDIANTE REGISTRADO CON EXITO***",end="\n\n")
                                    pause()
                                    salir = validar_cadenas(input("Registrar otro alumno? si/no->"))
                                    if salir == "si":
                                        condicion_salida = "si"
                                    else:
                                        condicion_salida = "no"
                                        break
                                else:
                                    print(Fore.YELLOW+"***ESTA MATRICULA NO EXISTE***")
                                    pause()
                else:
                    print(Fore.YELLOW+"¡¡¡ESTA CARRERA NO EXISTE***")  
            

        elif opcion == 5:
            """
            Previamente a registrar un alumno a una materia, debe estar registrada una materia y una carrera ademas
            de tener alumnos registrados a una carrera.
            Mediante la matricula del alumno lo inscribimos a la materia
            """
            borrarPantalla()
            print("***REGISTRAR ALUMNOS DE UNA MATERIA***")
            if len(lista_carreras) == 0:
                print(Fore.YELLOW+"¡¡¡NO HAY CARRERAS REGISTRADAS!!!")
                pause()
            else:
                for carreras in lista_carreras:
                    print(carreras)

                buscar_carrera = validar_cadenas(input("Ingrese la carrera->"))

                for carreras in lista_carreras:
                    if buscar_carrera == carreras.get_nombre():
                        if len(carreras.get_materias()) == 0:
                            print(Fore.YELLOW+"¡¡¡NO HAY MATERIAS REGISTRADAS!!!")
                            pause()
                        else:
                            for materias in carreras.get_materias():
                                print(materias)

                            nombre_materia = validar_cadenas(input("Ingrese el nombre de la materia->"))
                            for materias in carreras.get_materias():
                                if nombre_materia ==  materias.get_nombre_mat():
                                    matricula_alumno = validar_numeros(input("Ingrese la matricula del alumno->"))
                                    for matricula in lista_alumnos:
                                        materias.agregar_alumno(matricula)
                                        print(Fore.GREEN+"Alumno registrado con exito en la materia {}".format(materias.get_nombre_mat()))
                                        pause()
                                        break
                                    else:
                                        print(Fore.YELLOW+"***ÉSTA MATRICULA NO EXISTE***")
                                        pause()
                                        break
                                    break
                                

        elif opcion == 6:
            """
            Previamente a asignar una materia a un profesor, debe estar registrado un profesor
            debe haber carreras registradas y materias registradas.
            Mediante el numero de empleado del profesor le asignamos una materia.
            """
            borrarPantalla()
            print("***ASIGNAR MATERIA A PROFESOR***")
            if len(lista_carreras) == 0:
                print(Fore.YELLOW+"¡¡¡NO HAY CARRERAS REGISTRADAS!!!")
                pause()
            elif len(lista_empleado) == 0:
                print(Fore.YELLOW+"¡¡¡NO HAY MAESTROS REGISTRADOS!!!")
                pause()
            else:
                for carreras in lista_carreras:
                    print(carreras)

                nombre_carrera = validar_cadenas(input("Ingrese la carrera->"))

                for carreras in lista_carreras:
                    if nombre_carrera == carreras.get_nombre():
                        if len(carreras.get_materias()) == 0:
                            print(Fore.YELLOW+"¡¡¡NO HAY MATERIAS REGISTRADAS!!!")
                            pause()
                            break
                        else:
                            for materias in carreras.get_materias():
                                print(materias)

                            nombre_materia = validar_cadenas(input("Ingrese la materia->"))
                            for materias in carreras.get_materias():
                                if  nombre_materia == materias.get_nombre_mat():
                                    no_empleado = int(input("Ingrese el numero de empleado"))
                                    for empleado in lista_empleado:
                                        if empleado.get_no_empleado() == no_empleado:
                                            materias.set_titular(empleado)
                                            print(Fore.GREEN+"Maestro registrado con exito en la materia {}".format(materias.get_nombre_mat()))
                                            pause()
                                            break
                        



        elif opcion == 7:
            """
            Accedemos a la lista carreras e imprimos sus elementos
            """
            borrarPantalla()
            print("***LISTAR CARRERAS***")
            if len(lista_carreras) == 0:
                print(Fore.YELLOW+"¡¡¡NO HAY CARRERAS REGISTRADAS!!!")
                pause()
            else:
                for carreras in lista_carreras:
                    print(carreras)
                pause()


        elif opcion == 8:
            """
            Previamente a listar materias, deben existir carreras registradas.
            """

            borrarPantalla()
            print("***LISTAR MATERIAS DE UNA CARRERA***")
            if len(lista_carreras) == 0:
                print(Fore.YELLOW+"¡¡¡NO HAY CARRERAS REGISTRADAS!!!")
                pause()
            else:
                for carreras in lista_carreras:
                    if len(carreras.get_materias()) == 0:
                        print(Fore.YELLOW+"¡¡¡NO HAY MATERIAS REGISTRADAS!!!")
                        pause()
                        break
                    else:
                        for carreras in lista_carreras:
                            print(carreras)

                        materias_carrera =  validar_cadenas(input("Ingrese la carrera->"))
                        for carreras in lista_carreras:
                            if materias_carrera == carreras.get_nombre():
                                print("***{}***".format(carreras.get_nombre()))
                                for materias in carreras.get_materias():
                                    print(materias)
                            pause()
                        break


        elif opcion == 9:
            """
            Previamente a listar los alumnos, debe existir una carrera registrada
            y mediante un metodo get() extraemos los alumnos de la carrera
            """
            borrarPantalla()
            print("***LISTAR ALUMNOS DE UNA CARRERA***")
            if len(lista_carreras) == 0:
                print(Fore.YELLOW+"¡¡¡NO HAY CARRERAS REGISTRADAS!!!")
                pause()
            else:
                for carreras in lista_carreras:
                    print(carreras)

                alumno_carrera = validar_cadenas(input("Ingrese la carrera->"))
                for carreras in lista_carreras:
                    if alumno_carrera == carreras.get_nombre():
                        print("***{}***".format(carreras.get_nombre()))
                        for alumnos in carreras.get_alumnos():
                            print(alumnos)
                        pause()
                        continue
                else:
                    print(Fore.YELLOW+"¡¡¡ESTA CARRERA NO EXISTE***")  
                    pause()


        elif opcion == 10:
            """
            Previamente a listar los aslumnos de cierta materia, deben existir materias y carreras
            registradas
            """
            borrarPantalla()
            print("***LISTAR ALUMNOS DE UNA MATERIA***")
            if len(lista_carreras) == 0:
                print(Fore.YELLOW+"¡¡¡NO HAY CARRERAS REGISTRADAS AUN!!!!")
                pause()
            else:
                for carreras in lista_carreras:
                    print(carreras)

                nombre_carrera = validar_cadenas(input("Nombre carrera->"))
                for carreras in lista_carreras:
                    if carreras.get_nombre() == nombre_carrera:
                        if len(carreras.get_materias()) == 0:
                            print(Fore.YELLOW+"¡¡¡NO HAY MATERIAS REGISTRADAS A ESTA CARRERA!!!!")
                            pause()
                        else:
                            for materias in carreras.get_materias():
                                print(materias)
                

                            nombre_materia = validar_cadenas(input("Ingrese la materia->"))
                            for materias in carreras.get_materias():
                                if materias.get_nombre_mat() == nombre_materia:
                                    for alumnos in materias.listar_alumnos():
                                        print(alumnos)
                                    pause()
                                    break
                            else:
                                print(Fore.YELLOW+"¡¡¡ESTA MATERIA NO EXISTE!!!")
                    

        elif opcion == 11:
            """
            Previamente a listar las materias que imparte un profesor
            deben existir carreras y materias registradas.
            Mediante el numero de empleado del profesor, listamos las materias
            asignadas a su numero de empleado.
            """
            borrarPantalla()
            print("***LISTAR MATERIAS DE UN PROFESOR***")
            if len(lista_empleado) == 0:
                print(Fore.YELLOW+"¡¡¡NO HAY MAESTROS REGISTRADOS!!!")
                pause()
            else:
                no_empleado = int(input("Ingrese el numero de empleado->"))
                for empleado in lista_empleado:
                    if no_empleado == empleado.get_no_empleado():
                        for carreras in lista_carreras:
                            for materias in carreras.get_materias():
                                print(materias)
                    pause()
                else:
                    print(Fore.YELLOW+"¡¡¡Este numero de empleado no exite!!!")
                    pause()
            

        elif opcion == 12:
            """
            Finalizamo el programa
            """
            break


                


if __name__  == "__main__":
    main()