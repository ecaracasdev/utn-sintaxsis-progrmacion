from tadLibro import *
from tadLibreria import *

respuesta = 'si'
counter=0
libreria = crearLibreria()

while respuesta == 'si':
    opcion = int(input("""
        Seleccione la opcion para la operacion que desea realizar:
        0. Cargar libros automaticamente de una lista previamente creada
        1. Cargar libros a la libreria
        2. Mostrar todos los libros de la libreria
        3. Mostrar cuantos libros hay en la libreria
        4. Modificar el precio de un libro
        5. Incrementar el precio de un libro
    """))
    if opcion == 0:
        listaLibros = [
            ['libro1','editorial1','autor1',1000],
            ['libro2','editorial2','autor2',2000],
            ['libro3','editorial3','autor3',3000],
            ['libro4','editorial4','autor4',4000],
        ]
        for i in listaLibros:
            libro = crearLibro()
            agregarLibro(libreria, i)
    if opcion == 1:
        cantidad_libros = input('Porfavor introduzca la cantidad de libros que desea cargar en la libreria: \n')

        for i in range(int(cantidad_libros)):
            libro = crearLibro()
            print(f'Ingresar info del libro {i+1}: \n')
            nombre = input('Nombre: ')
            editorial = input('Editorial: ')
            autor = input('Autor: ')
            precio = int(input('Precio: '))
            cargarLibro(libro, nombre, editorial, autor, precio)
            agregarLibro(libreria,libro)
            print('libro cargado correctamente\n')
    if opcion == 2:
        # mostrar los libros de la libreria
        for i in range(0,tamanio(libreria)):
            print(f'libro numero {i+1}: {recuperarLibro(libreria,i)}')
    if opcion == 3:
        print(f'Hay {tamanio(libreria)} libros')
    if opcion == 4:
        nombreLibro = input('introduzca el nombre del libro que desea modificar: \n')
        for i in range(0,tamanio(libreria)):
            libroRecuperado = recuperarLibro(libreria,i)
            if libroRecuperado[0] == nombreLibro:
                print(f'precio antes de modificar el libro: {libroRecuperado[3]}')
                otroPrecio = int(input('introduzca el nuevo precio del libro'))
                modificarPrecio(libroRecuperado, otroPrecio)
                print(f'precio despues de modificar el libro: {libroRecuperado[3]}')
    if opcion == 5:
        editorialAmodificar = input('Introduzca la editorial que desea modificar \n')
        for i in range(0,tamanio(libreria)):
            libroRecuperado = recuperarLibro(libreria,i)
            if libroRecuperado[1] == editorialAmodificar:
                print(f'precio antes de modificar el libro: {libroRecuperado[3]}')
                incrementarPorEditorial(libroRecuperado)
                print(f'precio despues de modificar el libro: {libroRecuperado[3]}')
    else:
        print('adios')
        respuesta = 'no'
    
    respuesta = input('Desea realizar otra operacion? si/no \n')
    counter=counter+1

