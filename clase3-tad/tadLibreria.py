libreria = []

def crearLibreria():
    return libreria


def agregarLibro(libreria, libro):
    libreria.append(libro)


def recuperarLibro(libreria,i):
    return libreria[i]


def eliminarLibro(libreria, libro):
    return libreria.remove(libro)


def tamanio(libreria):
    return len(libreria)