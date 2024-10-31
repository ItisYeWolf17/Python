from Nodo import Nodo 

class Pila:
    
    def __init__(self, top:Nodo = None):
        self.__top = top
    
    def vacio(self):
        if self.__top == None:
            return True
        else:
            return False
    
    def agregar_contenedor(self, p):
        aux = Nodo(p)
        if self.vacio():
            self.__top = aux
        else:
            aux.set_next(self.__top)
            self.__top = aux
            
    def imprimir(self):
        concat = "----- Pila -----\n"
        
        if not self.vacio():
            aux = self.__top
            
            while aux != None:
                concat += str(aux.get_dato()) + "\n"
                aux = aux.get_next()
        
        input(concat + "\nPresione enter para continuar....")

