def crearCola():
    c = []
    return c


def encolar(cola, elemento):
    cola.append(elemento)

def desencolar(cola):
    elemento = cola.pop()
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
    
def mostrarCola(cola):
    for i in range(0, len(cola)):
        if i == 0:
            print("{0:<10} {1:<12}".format('Nombre', 'Obra Social'))
        print("{0:<10} {1:<12}".format(cola[i][0], cola[i][1]))
