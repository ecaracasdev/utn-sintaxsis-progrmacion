agenda = []

def crearAgenda():
    return agenda


def agregarCita(agenda, paciente):
    agenda.append(paciente)


def tamanio(agenda):
    return len(agenda)


def recuperarCita(agenda,i):
    return agenda[i]


def eliminarCita(agenda, cita):
    return agenda.remove(cita)