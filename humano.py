class  hombre:
    def __init__(self, nombre, edad, profecion):
        self.nombre = nombre
        self.edad = edad
        self.profecion = profecion
        
    def empezar_saluda(self):
        print("hola.")
    def presentarse(self):
        print("me llamo", self.nombre, "tengo", self.edad, "y soy", self.profecion)

def set_nombre(self, nombre):
    self.__nombre = nombre

def set_edad(self, edad):
    self.__edad = edad


humano = hombre("juan", "20", "policia")

humano.empezar_saluda()
humano.presentarse()

class hijo(hombre):
    def __init__(self, nombre, edad, profecion, estudia):
        super().__init__(nombre, edad, profecion)
        self.estudia = estudia

    def niño(self):
        print(f"el tiene {self.edad} y estas en el {self.estudia}")

hijo1 = hijo("tengo", "5", "d1", "coleguio")
hijo1.niño()
