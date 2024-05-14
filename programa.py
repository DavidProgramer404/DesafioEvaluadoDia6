from tienda import Restaurante, Supermercado, Farmacia, Producto  # Importa las clases necesarias

def crear_tienda():
    # Función para crear una instancia de tienda
    nombre = input("Ingrese el nombre de la tienda: ")
    costo_delivery = float(input("Ingrese el costo de delivery: "))
    tipo = input("Ingrese el tipo de tienda (Restaurante/Supermercado/Farmacia): ").lower()

    if tipo == "restaurante":
        return Restaurante(nombre, costo_delivery)
    elif tipo == "supermercado":
        return Supermercado(nombre, costo_delivery)
    elif tipo == "farmacia":
        return Farmacia(nombre, costo_delivery)
    else:
        print("Tipo de tienda no válido. Intente de nuevo.")
        return crear_tienda()

def ingresar_producto():
    # Función para ingresar un producto
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    stock = int(input("Ingrese el stock del producto: "))
    return Producto(nombre, precio, stock)

def main():
    # Función principal
    tienda = crear_tienda()  # Crea una instancia de tienda

    while True:
        # Loop principal del programa
        print("\n¿Qué desea hacer?")
        print("1. Ingresar producto")
        print("2. Listar productos")
        print("3. Realizar venta")
        print("4. Salir")
        opcion = input("Ingrese el número de la opción: ")

        if opcion == "1":
            producto = ingresar_producto()  # Ingresa un nuevo producto
            tienda.ingresar_producto(producto)  # Llama al método de la tienda para ingresar el producto
        elif opcion == "2":
            print("\nProductos existentes:")
            print(tienda.listar_productos())  # Llama al método de la tienda para listar los productos
        elif opcion == "3":
            nombre_producto = input("Ingrese el nombre del producto a vender: ")
            cantidad = int(input("Ingrese la cantidad a vender: "))
            tienda.realizar_venta(nombre_producto, cantidad)  # Llama al método de la tienda para realizar una venta
        elif opcion == "4":
            break  # Sale del programa
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()  # Ejecuta la función principal si el script se ejecuta directamente
