from clases_control_escolar import *
from datetime import date
from datetime import datetime
from colorama import init, Fore, Back, Style
init(autoreset=True)

lista_carreras = []
lista_empleado = []
lista_alumnos = []
def menu_principal():
     print("1)Registrar carrera",#
     "2)Registrar profesor",#
     "3)Registrar materias a carrera",#
     "4)Registrar alumno a carrera",#
     "5)Inscribir alumno a materia",#
     "6)Asignar materia a profesor",
     "7)Listar Carerras",#
     "8)Listar materias de una carrera",#
     "9)Listar alumnos de una carrera", #
     "10)Listar alumnos inscritos a una materia",#
     "11)Listar materias de un profesor",#
     "12)Salir",#
     sep="\n",end="\n\n")
     opcion = int(input("Ingrese la opcion deseada->"))
     return opcion


def main():
    while True:
        lista_materias = []
        opcion = menu_principal()


        if opcion == 1:
            print("***REGISTRAR CARRERA***")
            condicion_salida = "si"
            while condicion_salida != "no":
                especialidad = carrera()
                if len(lista_carreras) == 0:
                    nombre_carrera = input("Ingrese el nombre de la carrera->")
                    especialidad.set_nombre(nombre_carrera)
                    lista_carreras.append(especialidad)
                    print(Fore.GREEN+"***CARRERA REGISTRADA CON EXITO***")
                    salir = input("Registrar otra carrera? si/no->")
                    if salir == "si":
                        condicion_salida = "si"
                    else:
                        condicion_salida = "no"
                else:
                    nombre_carrera = input("Ingrese el nombre de la carrera->")
                    for carreras in lista_carreras:
                        if nombre_carrera != carreras.get_nombre():
                            especialidad.set_nombre(nombre_carrera)
                            lista_carreras.append(especialidad)
                            print(Fore.GREEN+"***CARRERA REGISTRADA CON EXITO***")
                            salir = input("Registrar otra carrera? si/no->")
                            if salir == "si":
                                condicion_salida = "si"
                                
                            else:
                                condicion_salida = "no"
                                break
                    else:
                        print(Fore.YELLOW+"¡¡¡Esta carrera ya existe!!!")


        elif opcion == 2:
            maestro = profesor()
            print("***REGISTRAR PROFESOR***")
            if len(lista_empleado) == 0:
                numero_profesor = int(input("Ingrese el número de profesor/empleado->"))
                nombre_profesor = input("Ingrese el nombre del profesor->")
                fecha_ingreso = datetime.now()
                print("***NOTA***","Fecha de ingreso {}".format(fecha_ingreso))
                maestro.set_no_empleado(numero_profesor)
                maestro.set_nombre(nombre_profesor)
                maestro.set_fecha_ingreso(fecha_ingreso)
                lista_empleado.append(maestro)
                print(Fore.GREEN+"***EMPLEADO REGISTRADO CON EXITO***")
            else:
                numero_profesor = int(input("Ingrese el número de profesor/empleado->"))
                for profe in lista_empleado:
                    if numero_profesor != profe.get_no_empleado():
                        nombre_profesor = input("Ingrese el nombre del profesor->")
                        fecha_ingreso = datetime.now()
                        print("***NOTA***","Fecha de ingreso {}".format(fecha_ingreso))
                        maestro.set_no_empleado(numero_profesor)
                        maestro.set_nombre(nombre_profesor)
                        maestro.set_fecha_ingreso(fecha_ingreso)
                        lista_empleado.append(maestro)
                        print(Fore.GREEN+"***EMPLEADO REGISTRADO CON EXITO***")
                        break
                else:
                    print(Fore.YELLOW+"***ESTE NUMERO DE EMPLEADO YA EXISTE***")


        elif opcion == 3:
            print("***REGISTRAR MATERIAS A CARRERA***")
            if len(lista_carreras) == 0:
                print(Fore.YELLOW+"¡¡¡AUN NO HAY MATERIAS REGISTRADAS!!!")
            else:
                for carreras in lista_carreras:
                    print(carreras,end="\n\n")

                nombre_carrera = input("Ingrese el nombre de la carrera->")
                for carreras in lista_carreras:
                    if nombre_carrera == carreras.get_nombre():
                        condicion_salida = "si"
                        while condicion_salida != "no":
                            asignatura = materia()
                            if len(carreras.get_materias()) == 0:
                                nombre_materia = input("Ingrese el nombre de la materia->")
                                asignatura.set_nombre_mat(nombre_materia)
                                carreras.set_materias(asignatura)
                                print(Fore.GREEN+"***MATERIA AGREGADA CON EXITO***")
                                salir = input("Registrar otra materia? si/no->")
                                if salir == "si":
                                    condicion_salida = "si"
                                    
                                else:
                                    condicion_salida = "no"
                                    break
                            else:
                                nombre_materia = input("Ingrese el nombre de la materia->")
                                for materias in carreras.get_materias():
                                    if nombre_materia == materias.get_nombre_mat():
                                        print(Fore.YELLOW+"***ESTA MATERIA YA EXISTE")
                                    else:
                                        asignatura.set_nombre_mat(nombre_materia)
                                        carreras.set_materias(asignatura)
                                        print(Fore.GREEN+"***MATERIA AGREGADA CON EXITO***")
                                        salir = input("Registrar otra materia? si/no->")
                                        if salir == "si":
                                            condicion_salida = "si"
                                            
                                        else:
                                            condicion_salida = "no"
                                            break
                else:
                    print("¡¡¡ESTA CARRERA NO EXISTE***")        


        elif opcion == 4:
            
            print("***REGISTRAR ALUMNO A CARRERA***")
            if len(lista_carreras) == 0:
                print(Fore.YELLOW+"¡¡¡NO HAY CARRERAS REGISTRADAS AUN***")
            else:
                for carreras in lista_carreras:
                    print(carreras)
                nombre_carrera = input("Ingrese el nombre de la carrera->")
                for carreras in lista_carreras:
                    if nombre_carrera == carreras.get_nombre():
                        condicion_salida = "si"
                        while condicion_salida != "no":
                            estudiante = alumno1()
                            
                            if len(lista_alumnos) == 0:
                                matricula_alumno = int(input("Ingrese la matricula de alumno->"))
                                estudiante.set_matricula(matricula_alumno)

                                nombre_alumno = input("Ingrese el nombre de alumno->")
                                estudiante.set_nombre_alumno(nombre_alumno)

                                dia_nacimiento = int(input("Dia nacimiento->"))
                                mes_nacimiento = int(input("Mes nacimiento->"))
                                anio_nacimiento = int(input("Año nacimiento->"))
                                fecha_nacimiento_alumno = datetime(anio_nacimiento,mes_nacimiento,dia_nacimiento)
                                estudiante.set_fecha_nacimiento(fecha_nacimiento_alumno)

                                fecha_ingreso_alumno = datetime.now()
                                print(Fore.GREEN+"Fecha de ingreso->",fecha_ingreso_alumno)
                                estudiante.set_fecha_ingreso(fecha_ingreso_alumno)

                                genero_alumno = input("Genero->")
                                estudiante.set_genero(genero_alumno)

                                ciudad_alumno = input("Ciudad->")
                                estudiante.set_ciudad(ciudad_alumno)
                                

                                carreras.set_alumnos(estudiante)
                                lista_alumnos.append(estudiante)
                                print(Fore.GREEN+"***ESTUDIANTE REGISTRADO CON EXITO***",end="\n\n")
                                salir = input("Registrar otro alumno? si/no->")
                                if salir == "si":
                                    condicion_salida = "si"
                                else:
                                    condicion_salida = "no"
                            else:
                                
                                for matricula in lista_alumnos:
                                    matricula_alumno = int(input("Ingrese la matricula de alumno->"))
                                    if matricula_alumno == matricula.get_matricula():
                                        print(Fore.YELLOW+"***ESTA MATRICULA YA EXISTE***")
                                        continue
                                    estudiante.set_matricula(matricula_alumno)
                                    nombre_alumno = input("Ingrese el nombre de alumno->")
                                    estudiante.set_nombre_alumno(nombre_alumno)
                                    dia_nacimiento = int(input("Dia nacimiento->"))
                                    mes_nacimiento = int(input("Mes nacimiento->"))
                                    anio_nacimiento = int(input("Año nacimiento->"))
                                    fecha_nacimiento_alumno = datetime(anio_nacimiento,mes_nacimiento,dia_nacimiento)
                                    estudiante.set_fecha_nacimiento(fecha_nacimiento_alumno)
                                    fecha_ingreso_alumno = datetime.now()
                                    print(Fore.GREEN+"Fecha de ingreso->",fecha_ingreso_alumno)
                                    estudiante.set_fecha_ingreso(fecha_ingreso_alumno)
                                    genero_alumno = input("Genero->")
                                    estudiante.set_genero(genero_alumno)
                                    ciudad_alumno = input("Ciudad->")
                                    estudiante.set_ciudad(ciudad_alumno)
                                    
                                    carreras.set_alumnos(estudiante)
                                    lista_alumnos.append(estudiante)
                                    print(Fore.GREEN+"***ESTUDIANTE REGISTRADO CON EXITO***",end="\n\n")
                                    salir = input("Registrar otro alumno? si/no->")
                                    if salir == "si":
                                        condicion_salida = "si"
                                    else:
                                        condicion_salida = "no"
                                        break
                                else:
                                    print(Fore.YELLOW+"***ESTA MATRICULA NO EXISTE***")
                else:
                    print(Fore.YELLOW+"¡¡¡ESTA CARRERA NO EXISTE***")  
            

        elif opcion == 5:
            print("***REGISTRAR ALUMNOS A MATERIA***")
            if len(lista_carreras) == 0:
                print(Fore.YELLOW+"¡¡¡NO HAY CARRERAS REGISTRADAS!!!")
            else:
                for carreras in lista_carreras:
                    print(carreras)

                buscar_carrera = input("Ingrese la carrera->")

                for carreras in lista_carreras:
                    if buscar_carrera == carreras.get_nombre():
                        if len(carreras.get_materias()) == 0:
                            print(Fore.YELLOW+"¡¡¡NO HAY MATERIAS REGISTRADAS!!!")
                        else:
                            for materias in carreras.get_materias():
                                print(materias)

                            nombre_materia = input("Ingrese el nombre de la materia->")
                            for materias in carreras.get_materias():
                                if nombre_materia ==  materias.get_nombre_mat():
                                    matricula_alumno = int(input("Ingrese la matricula del alumno->"))
                                    for matricula in lista_alumnos:
                                        materias.agregar_alumno(matricula)
                                        print(Fore.GREEN+"Alumno registrado con exito en la materia {}".format(materias.get_nombre_mat()))
                                        break
                                    else:
                                        print(Fore.YELLOW+"***ÉSTA MATRICULA NO EXISTE***")
                                        break
                                    break
                                

        elif opcion == 6:
            print("***ASIGNAR MATERIA A PROFESOR***")
            if len(lista_carreras) == 0:
                print(Fore.YELLOW+"¡¡¡NO HAY CARRERAS REGISTRADAS!!!")
            elif len(lista_empleado) == 0:
                print(Fore.YELLOW+"¡¡¡NO HAY MAESTROS REGISTRADOS!!!")
            else:
                for carreras in lista_carreras:
                    print(carreras)

                nombre_carrera = input("Ingrese la carrera->")

                for carreras in lista_carreras:
                    if nombre_carrera == carreras.get_nombre():
                        if len(carreras.get_materias()) == 0:
                            print(Fore.YELLOW+"¡¡¡NO HAY MATERIAS REGISTRADAS!!!")
                            break
                        else:
                            for materias in carreras.get_materias():
                                print(materias)

                            nombre_materia = input("Ingrese la materia->")
                            for materias in carreras.get_materias():
                                if  nombre_materia == materias.get_nombre_mat():
                                    no_empleado = int(input("Ingrese el numero de empleado"))
                                    for empleado in lista_empleado:
                                        if empleado.get_no_empleado() == no_empleado:
                                            materias.set_titular(empleado)
                                            print(Fore.GREEN+"Maestro registrado con exito en la materia {}".format(materias.get_nombre_mat()))
                                            break
                        



        elif opcion == 7:
            print("***LISTAR CARRERAS***")
            if len(lista_carreras) == 0:
                print(Fore.YELLOW+"¡¡¡NO HAY CARRERAS REGISTRADAS!!!")
            else:
                for carreras in lista_carreras:
                    print(carreras)


        elif opcion == 8:
            print("***LISTAR MATERIAS DE UNA CARRERA***")
            if len(lista_carreras) == 0:
                print(Fore.YELLOW+"¡¡¡NO HAY CARRERAS REGISTRADAS!!!")
            else:
                for carreras in lista_carreras:
                    if len(carreras.get_materias()) == 0:
                        print(Fore.YELLOW+"¡¡¡NO HAY MATERIAS REGISTRADAS!!!")
                        break
                    else:
                        for carreras in lista_carreras:
                            print(carreras)

                        materias_carrera =  input("Ingrese la carrera->")
                        for carreras in lista_carreras:
                            if materias_carrera == carreras.get_nombre():
                                print("***{}***".format(carreras.get_nombre()))
                                for materias in carreras.get_materias():
                                    print(materias)
                        break


        elif opcion == 9:
            print("***LISTAR ALUMNOS DE UNA CARRERA***")
            if len(lista_carreras) == 0:
                print(Fore.YELLOW+"¡¡¡NO HAY CARRERAS REGISTRADAS!!!")
            else:
                for carreras in lista_carreras:
                    print(carreras)

                alumno_carrera = input("Ingrese la carrera->")
                for carreras in lista_carreras:
                    if alumno_carrera == carreras.get_nombre():
                        print("***{}***".format(carreras.get_nombre()))
                        for alumnos in carreras.get_alumnos():
                            print(alumnos)
                        continue
                else:
                    print(Fore.YELLOW+"¡¡¡ESTA CARRERA NO EXISTE***")  


        elif opcion == 10:
            print("***LISTAR ALUMNOS DE UNA MATERIA***")
            if len(lista_carreras) == 0:
                print(Fore.YELLOW+"¡¡¡NO HAY CARRERAS REGISTRADAS AUN!!!!")
            else:
                for carreras in lista_carreras:
                    print(carreras)

                nombre_carrera = input("Nombre carrera->")
                for carreras in lista_carreras:
                    if carreras.get_nombre() == nombre_carrera:
                        if len(carreras.get_materias()) == 0:
                            print(Fore.YELLOW+"¡¡¡NO HAY MATERIAS REGISTRADAS A ESTA CARRERA!!!!")
                        else:
                            for materias in carreras.get_materias():
                                print(materias)
                

                            nombre_materia = input("Ingrese la materia->")
                            for materias in carreras.get_materias():
                                if materias.get_nombre_mat() == nombre_materia:
                                    for alumnos in materias.listar_alumnos():
                                        print(alumnos)
                                    break
                            else:
                                print(Fore.YELLOW+"¡¡¡ESTA MATERIA NO EXISTE!!!")
                    

        elif opcion == 11:
            print("***LISTAR MATERIAS DE UN PROFESOR***")
            if len(lista_empleado) == 0:
                print(Fore.YELLOW+"¡¡¡NO HAY MAESTROS REGISTRADOS!!!")
            else:
                no_empleado = int(input("Ingrese el numero de empleado->"))
                for empleado in lista_empleado:
                    if no_empleado == empleado.get_no_empleado():
                        for carreras in lista_carreras:
                            for materias in carreras.get_materias():
                                print(materias)
                else:
                    print(Fore.YELLOW+"¡¡¡Este numero de empleado no exite!!!")
            

        elif opcion == 12:
            break


                


if __name__  == "__main__":
    main()