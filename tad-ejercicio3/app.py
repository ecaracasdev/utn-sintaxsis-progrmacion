from datetime import date 
from tadAgenda import *
from tadCita import *
from tadCola import *
from utils import *

respuesta = 'si'
isValidDate = False
counter = 0
agenda = crearAgenda()

agenda = [
    ['elias', 'osde', '2e0322', datetime(2022, 6, 13), time(15,30)],
    ['simon', 'osde', '323249029', datetime(2022, 6, 11), time(15,30)],
    ['michelle', 'osde', '323249029', datetime(2022, 6, 11), time(15,30)],
    ['janme', 'ho', '323249029', datetime(2022, 6, 13), time(15,30)],
    ['juan', 'la', '323249029', datetime(2022, 6, 11), time(15,30)],
    ['jose', 'be', '323249029', datetime(2022, 6, 13), time(15,30)]
]

while respuesta == 'si':
    opcion = int(input("""
        Seleccione la opcion para la operacion que desea realizar:
        0. Agregar cita
        1. Modificar fecha y hora de la cita
        2. Eliminar cita
        3. Listado de citas
        4. Pasar todas las citas de un día a otro día determinado
        5. Eliminar todas las citas de una obra social
        6. Generar cola con todos los nombres y obra social de pacientes que se atienden en un dia
    """))
    if opcion == 0: # agregar cita
        cita = crearCita()
        print(f'Ingresar informacion de la cita \n')
        nombre = input('Nombre: ') 
        obraSocial = input('Obra Social: ')
        telefono = input('Telefono: ')

        while isValidDate == False:
            fecha = input('Fecha (dd/mm/yyyy) : ')
            hora = input('Hora (HH:MM): ')
            if validarFecha(fecha) & validarHora(hora):
                fechaFormateada = fechaParser(fecha)
                horaFormateada = horaParser(hora)
                cargarCita(cita, nombre, obraSocial, telefono, fechaFormateada, horaFormateada)
                agregarCita(agenda, cita)
                isValidDate = True
            else:
                print('formato de fecha u hora invalidos por favor cargue la informacion nuevamente\n')
    if opcion == 1: # modificar fecha
        
        nombrePaciente = input(
            'introduzca el nombre del paciente que desea modificar la fecha y hora: \n')
       
        for i in range(0, tamanio(agenda)):
            citaRecuperada = recuperarCita(agenda, i)
            if verNombre(citaRecuperada) == nombrePaciente:
                while isValidDate == False:
                    print(f'fecha y hora antes de modificar la cita: {verFecha(citaRecuperada)} , {verHora(citaRecuperada)}')
                    otraFecha = input('introduzca la nueva fecha de la cita (dd/mm/yyyy): ')
                    otraHora = input('introduzca la nueva Hora de la cita (HH:MM): ')
                    if validarFecha(otraFecha) & validarHora(otraHora):
                        otraFechaFormateada = fechaParser(otraFecha)
                        otraHoraFormateada = horaParser(otraHora)
                        modificarFechaHora(citaRecuperada, otraFechaFormateada, otraHoraFormateada)
                        print(f'fecha y hora despues de modificar la cita: {verFecha(citaRecuperada)} , {verHora(citaRecuperada)}')
                        isValidDate = True
                    else:
                        print('formato de fecha u hora invalidos por favor cargue la informacion nuevamente\n')
    if opcion == 2: # eliminar un item de la lista
        nombrePaciente = input('Introduzca el nombre del paciente que desea cancelar su cita: \n')
        for i in range(0, tamanio(agenda)):
            citaRecuperada = recuperarCita(agenda,i)
            indexToRemove = 0
            if verNombre(citaRecuperada) == nombrePaciente:
                indexToRemove = i
        eliminarCita(agenda, indexToRemove)
    if opcion == 3: # listar elementos
        for i in range(0, tamanio(agenda)):
            print(f'paciente {i+1}: {recuperarCita(agenda,i)}')
    if opcion == 4: # pasar citas a otro dia
        while isValidDate == False:
            fechaActual = input('Ingrese la fecha que desea modificar (dd/mm/yyyy): ')
            fechaNueva = input('Ingrese la nueva fecha (dd/mm/yyyy): ')
            horaNueva = input('Ingrese la nueva hora (HH:MM): ')
           
            if validarFecha(fechaActual) & validarFecha(fechaNueva) & validarHora(horaNueva):
                fechaActualFormateada = fechaParser(fechaActual)
                fechaNuevaFormateada = fechaParser(fechaNueva)
                horaNuevaFormateada = horaParser(horaNueva)
        
                for i in range(0, tamanio(agenda)):
                    citaRecuperada = recuperarCita(agenda,i)
                    if verFecha(citaRecuperada) == fechaActualFormateada:
                        print('cita por modificar')
                        print(citaRecuperada)
                        modificarFechaHora(citaRecuperada, fechaNuevaFormateada, horaNuevaFormateada)
                        print('cita modificada: ')
                        print(citaRecuperada)
                
                isValidDate = True
            else:
                print('formato de fecha u hora invalidos por favor cargue la informacion nuevamente\n')
    if opcion == 5: # eliminar elementos por obra social
        obraSocial = input('Introduzca el nombre de la obra social de la cual desea borrar las citas: \n')
        agenda = eliminarCitasPorObraSocial(agenda,obraSocial)
    if opcion == 6: #cola de todos los nombre y obra social que se atienden en un dia
        print('generar cola')
        newCola = crearCola()
        print(newCola)
        for cita in agenda:
            encolar(newCola, [verNombre(cita),verObraSocial(cita)])
        print(f'cola con todos los nombre y obra sociales: {newCola}')
    else:
        respuesta = 'no'

    respuesta = input('Desea realizar otra operacion? si/no \n')
    counter = counter+1
