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
    funciones.limpiar_consola()
    try:
        
        menu = int(input("Ingrese lo que desea hacer:\n\t1.Agregar Producto\n\t"+ 
                        "2.Mostrar Productos\n\t3.Total de ingresos por producto\n\t" +
                        "4.Ingreso total de ventas\n\t5.Producto con mayor ingreso" + 
                        "\n\t0.Salir\nSeleccione del 1 - 0 lo que desea hacer: "))
        
        match menu:
            case 1:
                funciones.agregar_producto(ventas)
            case 2:
                funciones.mostrar_productos(ventas)
            case 3:
                funciones.ingresos_productos(ventas)
            case 4:
                funciones.ingresos_totales(ventas)
            case 5:
                funciones.producto_mayor_Ingresos(ventas)
            case 0:
                print("Gracias por usar...")
                break
    except:
        input("Debe ingresar una opcion valida, presione enter para continuar...")

