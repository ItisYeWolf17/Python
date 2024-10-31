class Persona:
    
    #Si a un atributo no se le pone _ despues del self es publico
    #Si se pone un _ por ejemplo self._nombre quiere decir que es protegido (Se usa en herencia)
    #Si se ponen dos __ por ejemplo self.__nombre quiere decir que es privado
    
    def __init__(self, nombre=None, apellido=None, edad=None, email=None):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__edad = edad
        self.__email = email
        
    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self, nombre):
        self.__nombre = nombre
    
    def get_apellido(self):
        return self.__apellido
    
    def set_apellido(self, apellido):
        self.__apellido = apellido
        
    def get_edad (self):
        return self.__edad
    
    def set_edad(self, edad):
        self.__edad = edad
        
    def get_email(self):
        return self.__email
    
    def set_email(self, email):
        self.__email = email
        
    def __str__(self):
        return f'''Persona:
                Nombre: {self.__nombre}
                Apellido: {self.__apellido}
                Edad: {self.__edad}
                Email: {self.__email}'''
                
    def crearPersona(self):
        temp = 0
        nombre = str(input("Ingrese el nombre de la persona: "))
        apellido = str(input("Ingrese los apellidos de la persona: "))
        edad = 0
        while temp != 1:
            try:
                edad = int(input("Ingrese la edad de la persona: "))
                
                if(edad > 0):
                    temp = 1
                        
            except:
                input("La edad ingresada no es valida, intente de nuevo. Presione enter para continuar...")
        
        email = str(input("Ingrese el correo de la persona: "))
        
        p = Persona(nombre,apellido,edad,email)
        
        return p
        