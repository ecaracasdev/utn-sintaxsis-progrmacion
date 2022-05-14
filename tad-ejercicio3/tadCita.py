def crearCita():
    cita = ["","","","",""] # [nombre, obraSocial, telefono, fecha de la cita, hora de la cita]
    return cita


def cargarCita(cita, nombre, obraSocial, telefono, fecha, hora):
    cita[0] = nombre
    cita[1] = obraSocial
    cita[2] = telefono
    cita[3] = fecha
    cita[4] = hora

def modificarFechaHora(cita, otraFecha, otraHora):
    cita[3] = otraFecha
    cita[4] = otraHora
