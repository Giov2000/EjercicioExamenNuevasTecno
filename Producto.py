

class Producto:
    def __init__(self,id,nombre,descripcion,costo,cantidad,precio_de_venta):
        self._id = id
        self._nombre = nombre
        self._descripcion = descripcion
        self._costo = costo
        self._cantidad = cantidad
        self._precio_de_venta = precio_de_venta

    @property
    def id(self):
        return self._id

    @property
    def nombre(self):
        return self._nombre

    @property
    def descripcion(self):
        return self._descripcion

    @property
    def costo(self):
        return self._costo

    @property
    def cantidad(self):
        return self._cantidad

    @property
    def precio_de_venta(self):
        return self._precio_de_venta

    @id.setter
    def id(self, id):
        self._id = id

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @descripcion.setter
    def descripcion(self, descripcion):
        self._descripcion = descripcion

    @costo.setter
    def costo(self, costo):
        self._costo = costo

    @cantidad.setter
    def cantidad(self, cantidad):
        self._cantidad = cantidad

    @precio_de_venta.setter
    def precio_de_venta(self, precio_de_venta):
        self._precio_de_venta = precio_de_venta

    def registrar_producto(self):
        self._id = input("Ingrese el id del producto: ")
        self._nombre = input("Ingrese el nombre del producto: ")
        self._descripcion = input("Ingrese la descripcion del producto: ")
        self._costo = float(input("Ingrese el costo del producto: "))
        self.cantidad = input("Ingrese la cantidad del producto: ")
        #Margen de venta = 20%
        self._precio_de_venta = self._costo/(1-0.2)

    def imprimir_productos(self):
        print(f"Id: {self._id}, Nombre: {self._nombre}, Descripcion: {self._descripcion}, Costo: {self._costo}, Cantidad: {self.cantidad}, "
              f"Precio de venta: {self._precio_de_venta} ")

