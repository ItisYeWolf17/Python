import Persona

class Nodo:
    
    def __init__(self, dato: Persona, next=None): #None hace que un atributo sea opcional
        self.__dato = dato
        self.__next = next
    
    def get_dato(self):
        return self.__dato
    
    def set_dato(self, dato):
        self.__dato = dato
        
    def get_nombre(self):
        return self.__next
    
    def set_nombre(self, next):
        self.__next = next
        
