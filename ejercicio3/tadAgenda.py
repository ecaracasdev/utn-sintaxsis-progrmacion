agenda = []

def crearAgenda():
    return agenda


def agregarCita(agenda, paciente):
    agenda.append(paciente)


def tamanio(agenda):
    return len(agenda)


def recuperarCita(agenda,i):
    return agenda[i]


def eliminarCita(agenda, index):
    return agenda.remove(index)

def eliminarCitasPorObraSocial(agenda, obraSocial):
    newAgenda = []
    for cita in agenda:
        if cita[1] != obraSocial:
            newAgenda.append(cita)
    agenda = newAgenda.copy()
    return agenda