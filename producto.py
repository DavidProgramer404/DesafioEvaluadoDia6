class Producto:
    def __init__(self, nombre, precio, stock=0):
        # Constructor de la clase Producto
        self.__nombre = nombre  # Nombre del producto (privado)
        self.__precio = precio  # Precio del producto (privado)
        self.__stock = stock    # Stock del producto (privado)

    @property
    def nombre(self):
        # Getter para el nombre del producto
        return self.__nombre

    @property
    def precio(self):
        # Getter para el precio del producto
        return self.__precio

    @property
    def stock(self):
        # Getter para el stock del producto
        return self.__stock

    def modificar_stock(self, cantidad):
        # Método para modificar el stock del producto
        if cantidad < 0:
            self.__stock = 0  # Si la cantidad es negativa, asigna 0 al stock
        else:
            self.__stock += cantidad  # Incrementa el stock por la cantidad proporcionada
