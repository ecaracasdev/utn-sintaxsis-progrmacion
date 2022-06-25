from datetime import datetime, time 

DEFAULT_DATA = [
    ['elias', 'osde', '2213521895', datetime(2022, 6, 13).strftime('%d/%m/%Y'), time(15,30).strftime('%H:%M')],
    ['simon', 'osde', '2213521896', datetime(2022, 6, 11).strftime('%d/%m/%Y'), time(15,30).strftime('%H:%M')],
    ['miche', 'osde', '2213521897', datetime(2022, 6, 11).strftime('%d/%m/%Y'), time(15,30).strftime('%H:%M')],
    ['janme', 'ioma', '2213521898', datetime(2022, 6, 13).strftime('%d/%m/%Y'), time(15,30).strftime('%H:%M')],
    ['juan', 'ioma', '2213521892', datetime(2022, 6, 11).strftime('%d/%m/%Y'), time(15,30).strftime('%H:%M')],
    ['jose', 'ioma', '2213521891', datetime(2022, 6, 13).strftime('%d/%m/%Y'), time(15,30).strftime('%H:%M')]
]

MENU_MESSAGE = """
         _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
        |                                                                                                        |
        |                                   ***  MENU ***                                                        |
        |                                                                                                        |
        |       1. Agregar cita                                                                                  |
        |       2. Modificar fecha y hora de la cita                                                             |
        |       3. Eliminar cita                                                                                 |
        |       4. Listado de citas                                                                              |
        |       5. Pasar todas las citas de un día a otro día determinado                                        |
        |       6. Eliminar todas las citas de una obra social                                                   |
        |       7. Generar cola con todos los nombres y obra social de pacientes que se atienden en un dia       |
        |                                                                                                        |
        |           Seleccione una opcion para continuar                                                         |
        |_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ | 

    """

APPOINMENT_LIST = '''
               LISTADO DE CITAS POR PACIENTE 
        '''
    
UPDATED_APPOINMENT_LIST = '''
                LISTADO DE CITAS MODIFICADAS
'''


ADD_APPOINMENT = '\n Ingresar información de la cita \n'
ADD_NAME = 'Nombre: '
ADD_OB = 'Obra Social: '
ADD_TELEPHONE = 'Télefono: '
ADD_DAY = 'Fecha (dd/mm/yyyy) : '
ADD_HOUR = 'Hora (HH:MM): '

ADD_NEW_DATE = '\nintroduzca la nueva fecha de la cita (dd/mm/yyyy): \n'
ADD_NEW_HOUR = '\nintroduzca la nueva hora de la cita (HH:MM): \n'

PACIENT_NAME = '\nintroduzca el nombre del paciente que desea modificar su cita: \n'

DATE_TO_UPDATE = '\nIngrese la fecha que desea modificar (dd/mm/yyyy): \n'

END_MENU = '\n\nDesea realizar otra operacion? si/no \n'

SEARCH_BY_OB = '\n Introduzca el nombre de la obra social de la cual desea borrar las citas: \n'

SEARCH_BY_NAME = '\n Introduzca el nombre del paciente que desea cancelar su cita: \n'


INVALID_DATE = '\nformato de fecha u hora invalidos por favor cargue la informacion nuevamente\n'

INVALID_OPTION = '\nseleccione una opcion correcta: '