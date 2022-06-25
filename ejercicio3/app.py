import time as t
from tadAgenda import *
from tadCita import *
from tadCola import *
from utils import *
from constants import *



def listaCitas(agenda):
    print(APPOINMENT_LIST)
    for i in range(0, tamanio(agenda)):
        if i == 0:
            print("{0:<10} {1:<12} {2:<12} {3:<12} {4:<10}".format('Nombre', 'Obra Social', 'Telefono', 'Fecha', 'Hora'))
        cita = recuperarCita(agenda,i)
        print("{0:<10} {1:<12} {2:<12} {3:<12} {4:<10}".format(verNombre(cita), verObraSocial(cita), verTelefono(cita), verFecha(cita), verHora(cita)))
    
def eliminarDeLaAgenda(agenda): 
    nombrePaciente = input(SEARCH_BY_NAME)
    citaAEliminar = []
    for i in range(0, tamanio(agenda)):
        citaRecuperada = recuperarCita(agenda,i)
        if verNombre(citaRecuperada) == nombrePaciente:
            citaAEliminar = citaRecuperada        
    eliminarCita(agenda, citaAEliminar)

def validOption(option):
    match = re.findall('[0-9]+',option)
    if len(match) > 0:
        return True
    return False

def main():
    respuesta = 'si'
    isValidDate = False
    agenda = crearAgenda()
    agenda = DEFAULT_DATA
    while respuesta == 'si':
        opcion = input(MENU_MESSAGE)
        
        if validOption(opcion) == False:
            print(INVALID_OPTION)
        
        if opcion == '1': # agregar cita
            cita = crearCita()
            print(ADD_APPOINMENT)
            nombre = input(ADD_NAME) 
            obraSocial = input(ADD_OB)
            telefono = input(ADD_TELEPHONE)

            while isValidDate == False:
                fecha = input(ADD_DAY)
                hora = input(ADD_HOUR)
                if validarFecha(fecha) & validarHora(hora):
                    fechaFormateada = fechaParser(fecha)
                    horaFormateada = horaParser(hora)
                    cargarCita(cita, nombre, obraSocial, telefono, fechaFormateada, horaFormateada)
                    agregarCita(agenda, cita)
                    listaCitas(agenda)
                    isValidDate = True
                else:
                    print(INVALID_DATE)

        if opcion == '2': # modificar fecha
            isValidDate = False
            nombrePaciente = input(PACIENT_NAME)
        
            for i in range(0, tamanio(agenda)):
                citaRecuperada = recuperarCita(agenda, i)
                if verNombre(citaRecuperada) == nombrePaciente:
                    while isValidDate == False:
                        print(f'\nfecha y hora antes de modificar la cita: {verFecha(citaRecuperada)}  {verHora(citaRecuperada)}\n')
                        otraFecha = input(ADD_NEW_DATE)
                        otraHora = input(ADD_NEW_HOUR)
                        if validarFecha(otraFecha) & validarHora(otraHora):
                            otraFechaFormateada = fechaParser(otraFecha)
                            otraHoraFormateada = horaParser(otraHora)
                            modificarFechaHora(citaRecuperada, otraFechaFormateada, otraHoraFormateada)
                            print(f'\nfecha y hora despues de modificar la cita: {verFecha(citaRecuperada)} , {verHora(citaRecuperada)}\n')
                            isValidDate = True
                        else:
                            print(INVALID_DATE)

        if opcion == '3': # eliminar un item de la lista
            listaCitas(agenda)
            eliminarDeLaAgenda(agenda)
            listaCitas(agenda)

        if opcion == '4': # listar elementos
            listaCitas(agenda)

        if opcion == '5': # pasar citas a otro dia
            isValidDate = False
            listaCitas(agenda)
            while isValidDate == False:
                fechaActual = input(DATE_TO_UPDATE)
                fechaNueva = input(ADD_NEW_DATE)
            
                if validarFecha(fechaActual) & validarFecha(fechaNueva):
                    fechaActualFormateada = fechaParser(fechaActual)
                    fechaNuevaFormateada = fechaParser(fechaNueva)
                    print(UPDATED_APPOINMENT_LIST)
                    for i in range(0, tamanio(agenda)):
                        citaRecuperada = recuperarCita(agenda,i)
                        if verFecha(citaRecuperada) == fechaActualFormateada:
                            modificarFecha(citaRecuperada, fechaNuevaFormateada)
                            if i == 0:
                                print("{0:<10} {1:<12} {2:<12} {3:<12} {4:<10}".format('Nombre', 'Obra Social', 'Telefono', 'Fecha', 'Hora'))
                            print("{0:<10} {1:<12} {2:<12} {3:<12} {4:<10}".format(verNombre(citaRecuperada), verObraSocial(citaRecuperada), verTelefono(citaRecuperada), verFecha(citaRecuperada), verHora(citaRecuperada)))
                    isValidDate = True
                else:
                    print(INVALID_DATE)

        if opcion == '6': # eliminar elementos por obra social
            listaCitas(agenda)
            obraSocial = input(SEARCH_BY_OB)
            agendaActualizada = eliminarCitasPorObraSocial(agenda,obraSocial)
            agenda = agendaActualizada
            listaCitas(agenda)

        if opcion == '7': #cola de todos los nombre y obra social que se atienden en un dia
            print("\nGENERANDO COLA CON NOMBRES Y OBRA SOCIAL...\n")
            newCola = crearCola()
            for cita in agenda:
                encolar(newCola, [verNombre(cita),verObraSocial(cita)])
            
            mostrarCola(newCola)

            while not esVacia(newCola):
                desencolar(newCola)

        if validOption(opcion):
            respuesta = input(END_MENU)

if __name__ == "__main__":
    main()