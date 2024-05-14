### este código proporciona una estructura para administrar tiendas y productos, permitiendo la creación, gestión y venta de productos dentro de diferentes tipos de tiendas.

## Definición de Clases:

Se define una clase Producto para representar los productos, con atributos como nombre, precio y stock, y métodos para crear y modificar productos.
Se define una clase Tienda como una clase base para representar las tiendas, con atributos como nombre, costo de delivery y una lista de productos. Incluye métodos para ingresar productos, listar productos existentes y realizar ventas.
Se definen clases hijas de Tienda para representar diferentes tipos de tiendas, como Restaurante, Supermercado y Farmacia, que heredan los métodos de Tienda y pueden agregar funcionalidades adicionales específicas para cada tipo de tienda.
Funciones del Programa Principal:

Se proporcionan funciones para crear una instancia de tienda (crear_tienda()) y para ingresar un nuevo producto (ingresar_producto()).
La función principal main() ejecuta un bucle interactivo que permite al usuario realizar varias acciones:
Crear una nueva tienda.
Ingresar productos en la tienda.
Listar los productos existentes en la tienda.
Realizar ventas de productos.
Salir del programa.
En resumen, el código proporciona una estructura básica para administrar tiendas y productos, permitiendo al usuario crear tiendas, agregar productos, realizar ventas y visualizar la información de los productos en la consola.
