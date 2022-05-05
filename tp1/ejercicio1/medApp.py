from tadMedicamento import *

def main():
    print('Menu trabajar con medicamentos')

    respuesta = 1
    while respuesta == 1:
        medicamento = crearMed()
        print(""" seleccione una opcion 
                1.mostrar medicamento
        """)
        opcion = input('ingrese la opcion deseada')
        if (int(opcion)==1):
            nombreGenerico = input('Ingresar el nombre generico:\n')
            nombreComercial = input('Ingresar el nombre comercial:\n')
            laboratorio = input('Ingresar laboratorio:\n')
            precio = input('Ingresar precio:\n')
            cargarMed(medicamento, nombreGenerico, nombreComercial, laboratorio, precio)
            print(f'Nombre comercial: {verNomCom(medicamento)}')
        respuesta = int(input('desea continuar 1 para si 0 para no'))


if __name__ == "__main__":
    main()