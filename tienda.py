from producto import Producto  # Importa la clase Producto


class Tienda:
    def __init__(self, nombre, costo_delivery):
        # Constructor de la clase Tienda
        self.__nombre = nombre  # Nombre de la tienda (privado)
        self.__costo_delivery = (
            costo_delivery  # Costo de delivery de la tienda (privado)
        )
        self.__productos = []  # Lista de productos de la tienda (privado)

    def ingresar_producto(self, producto):
        # Método para ingresar un producto a la tienda
        for p in self.__productos:
            if p.nombre == producto.nombre:
                # Si el producto ya existe, se modifica su stock
                p.modificar_stock(producto.stock)
                print("====================================================")
                print(f"El producto {producto.nombre} ya existe en la tienda.")
                print("====================================================")
                return
        else:
            # Si el producto no existe, se añade a la lista de productos de la tienda
            self.__productos.append(producto)
            print("====================================================")
            print(
                f"Producto {producto.nombre} ingresado exitosamente con stock de : {producto.stock} unidades."
            )
            print("====================================================")

    def listar_productos(self):
        # Método para listar los productos de la tienda
        lista = ""
        for p in self.__productos:
            lista += f"Nombre: {p.nombre}, Precio: {p.precio}, Stock : {p.stock}\n"
            # Modificaciones adicionales dependiendo del tipo de tienda
            if isinstance(self, Supermercado):
                if p.stock < 10:
                    lista += " (Pocos productos disponibles)"
            elif isinstance(self, Farmacia):
                if p.precio > 15000:
                    lista += " (Envío gratis al solicitar este producto)"
            lista += "\n"
        return (
            lista.strip()
        )  # Retorna la lista de productos como un string sin espacios adicionales

    def realizar_venta(self, nombre_producto, cantidad):
        # Método para realizar una venta
        for p in self.__productos:
            if p.nombre == nombre_producto:
                # Busca el producto por su nombre
                if isinstance(self, Restaurante):
                    # No se modifica el stock en un restaurante
                    pass
                else:
                    # Se modifica el stock del producto dependiendo de la cantidad
                    if cantidad <= 3 and p.stock >= cantidad:
                        p.modificar_stock(-cantidad)
                    elif isinstance(self, Farmacia) or isinstance(self, Supermercado):
                        if p.stock >= cantidad:
                            p.modificar_stock(-cantidad)
                        else:
                            p.modificar_stock(-p.stock)
                break


class Restaurante(Tienda):
    # Clase para el tipo de tienda Restaurante
    pass


class Supermercado(Tienda):
    # Clase para el tipo de tienda Supermercado
    pass


class Farmacia(Tienda):
    # Clase para el tipo de tienda Farmacia
    pass
