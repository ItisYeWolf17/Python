from Persona import Persona
from Pila import Pila

pila = Pila()
p = Persona()

menu = -1

while menu != 0:
    try:
        menu = int(input("1.Agregar Persona\n2.Mostrar Informacion\n0.Salir\nIngrese lo que desea hacer: "))
        
        match menu:
            case 1:
                pila.agregar_contenedor(p.crearPersona())
                
            case 2:
                pila.imprimir()
            
            case 0:
                break
            
            case _:
                print("Se ingreso una opcion incorrecta")
                
    except:
        input("debe digitar una opcion valida....")