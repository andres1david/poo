class animales:
    def __init__(self, especie, raza, nombre):
        self.especie = especie
        self.raza = raza
        self.nombre = nombre

    def se_mueve(self):
        print("se mueve en distintas direcciones")
    def sonido(self):
        print("ladra")
    def info(self):
        print("es un", self.especie, "de raza", self.raza, "y se llama", self.nombre )


def set_nombre(self, nombre):
    self.__nombre = nombre

def get_raza(self, raza):
    return self.__raza 

animal = animales("perro", "pastor alemas", "rocky")
animal.se_mueve()
animal.sonido()
animal.info()

class perros(animales):
    def __init__(self, especie, raza, nombre, edad):
        super().__init__(especie, raza, nombre)
        self.edad = edad

    def ladra(self):
        print("tiene una edad de", self.edad)

ladra = perros("perro", "pastor aleman", "rocky", 2)
ladra.ladra()

