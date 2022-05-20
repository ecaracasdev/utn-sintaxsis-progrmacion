def crearCola():
    c = []
    return c


def encolar(cola, elemento):
    cola.append(elemento)

def desencolar(cola):
    elemento = cola.pop(1)
    return elemento

def esVacia(cola):
    if cola == []:
        return True
    else:
        return False

def copiarCola(cola1, cola2):
    while not esVacia(cola1):
        elemento = desencolar(cola1)
        encolar(cola2, elemento)

