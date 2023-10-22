from Producto import Producto


productos_dict = {}

def Menu():

    init = int(input("Ingresa 1 para iniciar la ejecucion: "))

    while init != 0:

        opc = int(input("Ingresa 1 para registrar un producto\n"
              "Ingresa 2 para listar los productos\n"
              "Ingresa 3 para salir\n"))

        if opc == 1:
            producto = Producto(None,None,None,None,None,None)
            producto.registrar_producto()
            productos_dict[producto.id] = producto
        elif opc == 2:
            for producto_id,producto in productos_dict.items():
                producto.imprimir_productos()
        elif opc == 3:
            print("Hasta luego!!")
            init=0

Menu()