from clases_control_escolar import *
from datetime import datetime

lista_carreras = []
lista_empleado = []

def menu_principal():
     print("1)Registrar carrera",
     "2)Registrar profesor",
     "3)Registrar materias a carrera",
     "4)Registrar alumno a carrera",
     "5)Inscribir alumno a materia",
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


def main():
    while True:
        lista_materias = []
        especialidad = carrera()
        opcion = menu_principal()
        if opcion == 1:
            print("***REGISTRAR CARRERA***")
            nombre_carrera = input("Ingrese el nombre de la carrera->")
            especialidad.set_nombre(nombre_carrera)
            lista_carreras.append(especialidad)
            continue
        
        elif opcion == 2:
            maestro = profesor()
            print("***REGISTRAR PROFESOR***")
            if len(lista_empleado) == 0:
                numero_maestro = int(input("Ingrese el numero de empleado/profesor->"))
                nombre_maestro = input("Ingrese el nombre del profesor->")
                fecha_registro = datetime.now()
                print("¡¡¡NOTA!!!","La fecha de ingreso es la fecha actual({}) en la cual se realiza el resgistro".format(fecha_registro),
                sep="\n",end="\n\n")
                maestro.set_nombre(nombre_maestro)
                maestro.set_no_empleado(numero_maestro)
                maestro.set_fecha_ingreso(fecha_registro)
                lista_empleado.append(maestro)
                print("***Empleado registrado con exito***",end="\n\n")
                continue
            elif len(lista_empleado) > 0:
                condicion_salida = True
                while condicion_salida:
                    numero_maestro = int(input("Ingrese el numero de empleado/profesor->"))
                    for i in lista_empleado:
                        if numero_maestro == i.get_no_empleado():
                            print("¡¡¡ESTE NUMERO DE MAESTRO YA EXISTE!!!")
                            condicion_salida = True
                            break
                        else:
                            nombre_maestro = input("Ingrese el nombre del profesor->")
                            fecha_registro = datetime.now()
                            print("¡¡¡NOTA!!!","La fecha de ingreso es la fecha actual({}) en la cual se realiza el resgistro".format(fecha_registro),
                            sep="\n",end="\n\n")
                            maestro.set_nombre(nombre_maestro)
                            maestro.set_no_empleado(numero_maestro)
                            maestro.set_fecha_ingreso(fecha_registro)
                            lista_empleado.append(maestro)
                            print("***Empleado registrado con exito***",end="\n\n")
                            condicion_salida = False
                            break


        elif opcion == 3:
            condicion_salida = "1"
            print("***REGISTRAR MATERIAS A CARRERA***")
            for i in lista_carreras:
                print(i.get_nombre(),end="\n\n")

            buscar_carrera = input("Ingrese la carrera->")

            for i in lista_carreras:
                if buscar_carrera == i.get_nombre():
                    while condicion_salida != "-1":
                        #maestro = profesor()
                        nombre_materia = input("Nombre materia->")
                        if nombre_materia != "-1":
                            asignatura = materia()
                            asignatura.set_nombre(nombre_materia)
                            #lista_materias.append(asignatura)
                            #nombre_maestro = input("Nombre profesor->")
                            #numero_maestro = int(input("Numero de maestro->"))
                            #maestro.set_nombre(nombre_maestro)
                            #maestro.set_no_empleado(numero_maestro)
                            #asignatura.set_titular(maestro)
                            #i.agregar_materia(asignatura)
                            lista_materias.append(asignatura)
                            i.set_materias(lista_materias)
                            condicion_salida = "1"
                        else:
                            #i.set_materias(lista_materias)
                            condicion_salida = "-1"
                            break
            else:
                print("¡¡¡ÉSTA CARRERA NO EXISTE!!!")


        elif opcion == 6:
            asignatura = materia()
            print("***ASIGNAR MATERIA A PROFESOR***")
            buscar_carrera = input("Ingrese la carrera->")
            for i in lista_carreras:
                if buscar_carrera == i.get_nombre():
                    nombre_materia = input("Nombre materia->")
                    for j in i.listar_materias():
                        if nombre_materia == j.get_nombre_mat():
                            numero_empleado = input("Ingrese el numero de empleado a asignar a esta materia->")
                            for k in lista_empleado:
                                if numero_empleado == k.get_no_empleado():
                                    asignatura.set_titular(k)


            else:
                print("¡¡¡ESTA CARRERA NO EXISTE!!!")



        elif opcion == 7:
            print("***LISTA DE CARRERAS***")
            for i in lista_carreras:
                print(i.get_nombre())
            continue

        elif opcion == 8:
            print("***LISTA DE MATERIAS POR CARRERA****")
            for i in lista_carreras:
                print(i.get_nombre())

            listar_materias = input("Ingrese la carrera->")

            for i in lista_carreras:
                if listar_materias == i.get_nombre():
                    print("***",i.get_nombre(),"***")
                    for j in i.get_materias():
                        print("Nombre materia->",j.get_nombre_mat())
                        print("Titular->",j.get_titular().get_nombre_prof())
                else:
                    print("¡¡¡ÉSTA CARRERA NO EXISTE!!!")


        elif opcion == 12:
            break
                


if __name__  == "__main__":
    main()