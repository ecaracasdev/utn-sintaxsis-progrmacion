from tadAgenda import *
from tadCita import *

respuesta = 'si'
counter = 0
libreria = crearAgenda()

while respuesta == 'si':
    opcion = int(input("""
        Seleccione la opcion para la operacion que desea realizar:
        0. Agregar cita
        1. Modificar fecha y hora de la cita
        2. Eliminar cita
        3. Listado de citas
        4. Pasar la cita a otro dia
        5. Eliminar todas las citas de una obra social
        6. Generar cola con todos los nombres y obra social de pacientes que se atienden en un dia
    """))
    if opcion == 0:
        cita = crearCita()
        print(f'Ingresar informacion de la cita \n')
        nombre = input('Nombre: ')
        obraSocial = input('Obra Social: ')
        telefono = input('Telefono: ')
        fecha = input('Fecha: ')
        hora = input('Hora: ')
        cargarCita(cita, nombre, obraSocial, telefono, fecha, hora)
        agregarCita(agenda, cita)
    if opcion == 1:
        nombrePaciente = input(
            'introduzca el nombre del paciente que desea modificar la fecha y hora: \n')
        for i in range(0, tamanio(agenda)):
            citaRecuperada = recuperarCita(agenda, i)
            if citaRecuperada[0] == nombrePaciente:
                print(
                    f'fecha y hora antes de modificar la cita: {citaRecuperada[3]} , {citaRecuperada[4]}')
                otraHora = int(input('introduzca la nueva Hora de la cita'))
                otraFecha = int(input('introduzca la nueva fecha de la cita'))
                modificarFechaHora(citaRecuperada, otraFecha, otraHora)
                print(
                    f'fecha y hora despues de modificar la cita: {citaRecuperada[3]} , {citaRecuperada[4]}')
    if opcion == 2:
        print('hola')
    if opcion == 3:
        for i in range(0, tamanio(agenda)):
            print(f'paciente {i+1}: {recuperarCita(agenda,i)}')
    if opcion == 4:
        print('kfewkfwe')
    # if opcion == 5:
    else:
        print('adios')
        respuesta = 'no'

    respuesta = input('Desea realizar otra operacion? si/no \n')
    counter = counter+1
