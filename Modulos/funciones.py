import os

def agregarProducto(ventas):
    temp = 0
    while temp != 1:
        nombre_producto = str(input("Ingrese el nombre del producto: "))
        if(nombre_producto.strip() != ""):
            temp = 1
        else:
            input("Debe ingresar un nombre valido, presione enter para continuar....")
    temp = 0
    
    while temp != 1:
        try:
            cantidad_ventas = int(input("Ingrese la cantidad de ventas del producto: "))
            
            if(cantidad_ventas >= 0):
                temp = 1
            else:
                input("Debe ingresar una cantidad valida, presione enter para continuar....")
        except:
            input("El dato ingresado no es valido, intente de nuevo. Presione enter para continuar")
    
    temp = 0
    
    while temp != 1:
        try:
            precio = float(input("Ingrese el precio unitario del producto: "))
            
            if(precio >= 0):
                temp = 1
            else:
                input("Debe ingresar una cantidad valida, presione enter para continuar....")
        except:
            input("El dato ingresado no es valido, intente de nuevo. Presione enter para continuar")
    
    
    venta = {"producto" : nombre_producto.strip().lower(), "ventas": cantidad_ventas, "precio": precio}
    
    ventas.append(venta)  
    
def mostrarProductos(ventas):
    concat = "------------- Lista de Productos -------------\n" 
    for x in ventas:
        concat += "Nombre Producto: " + x['producto']
        concat += "\n\tCantidad de Ventas: " + str(x['ventas'])
        concat += "\n\tPrecio Unitario: $" + str(x['precio'])
        concat += "\n\n"
    
    print(concat)
    input("Presione enter para continuar....")
    
def ingresosProductos(ventas):
    concat = "------------- Ingresos por Productos -------------\n" 
    for x in ventas:
        concat += "Nombre Producto: " + x['producto']
        concat += "\n\tIngresos generados: " + str(x['ventas'] * x['precio'])
        concat += "\n\n"
    
    print(concat)
    input("Presione enter para continuar....")
    
def ingresosTotales(ventas):
    concat = "------------- Ingresos Totales -------------\n" 
    for x in ventas:
        ingresos = x['ventas'] * x['precio']
        concat += "Nombre Producto: " + x['producto']
        concat += "\n\tIngresos generados: " + str(ingresos)
        concat += "\n\t..............."
        concat += "\n\n"
    
    concat += "Total\t\t$" + str(ingresos)
    
    print(concat)
    input("Presione enter para continuar....")
    
    
def productoMayorIngresos(ventas):
    mayor = -1
    producto = {}
    for x in ventas:
        ingresos = x['ventas'] * x['precio']

        if mayor < ingresos:
            mayor = ingresos
            producto = x
    
    concat = "------------- Producto de Mayor Ingreso -------------\n" 
    concat += "Nombre Producto: " + producto['producto']
    concat += "\n\tIngresos generados: " + str(ingresos)
    concat += "\n\t..............."
    
    print(concat)
    input("Presione enter para continuar....")
    
    
def limpiarConsola():
    if os.name == 'nt': 
        os.system('cls')
    else:  
        os.system('clear')
         