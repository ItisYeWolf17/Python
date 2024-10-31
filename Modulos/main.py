##Imagina que tienes una tienda en línea y deseas analizar las ventas de tus productos.
#Escribe un programa en Python que calcule:
#El total de ingresos generados por cada producto.
#l ingreso total de todas las ventas.
#El producto que generó más ingresos.

#Salida esperada:
#El programa debe imprimir el ingreso total por producto, el ingreso total general y el producto con mayor ingreso.
import funciones

ventas = [];
menu = -1;

while menu != 0:
    funciones.limpiarConsola()
    try:
        
        menu = int(input("Ingrese lo que desea hacer:\n\t1.Agregar Producto\n\t"+ 
                        "2.Mostrar Productos\n\t3.Total de ingresos por producto\n\t" +
                        "4.Ingreso total de ventas\n\t5.Producto con mayor ingreso" + 
                        "\n\t0.Salir\nSeleccione del 1 - 0 lo que desea hacer: "))
        
        match menu:
            case 1:
                funciones.agregarProducto(ventas)
            case 2:
                funciones.mostrarProductos(ventas)
            case 3:
                funciones.ingresosProductos(ventas)
            case 4:
                funciones.ingresosTotales(ventas)
            case 5:
                funciones.productoMayorIngresos(ventas)
            case 0:
                print("Gracias por usar...")
                break
    except:
        input("Debe ingresar una opcion valida, presione enter para continuar...")

