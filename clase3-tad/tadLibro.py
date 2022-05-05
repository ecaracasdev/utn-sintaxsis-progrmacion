
def crearLibro():
    libro = ["","","",0]
    return libro


def cargarLibro(libro, nombre, editorial, autor, precio):
    libro[0] = nombre
    libro[1] = editorial
    libro[2] = autor
    libro[3] = precio


def verNombre(libro):
    return libro[0]


def verEditorial(libro):
    return libro[1]


def verAutor(libro):
    return libro[2]


def verPrecio(libro):
    return libro[3]

def modificarPrecio(libro, otroPrecio):
    libro[3] = otroPrecio

def incrementarPorEditorial(libro):
    libro[3] = libro[3] + 0.15*libro[3]