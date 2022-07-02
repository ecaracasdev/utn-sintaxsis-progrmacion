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
    i=0
    while i < len(agenda):
        if agenda[i][1] == obraSocial:
            agenda.remove(agenda[i])
        else:
            i+=1
    return agenda