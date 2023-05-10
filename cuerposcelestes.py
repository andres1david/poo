class cuerpo_celestes:
    def __init__(self, temperatura, tamaño, gravedad):
        self.temperatura = temperatura
        self.tamaño = tamaño
        self.gravedad = gravedad

    def estrella(self):
        print("el solo es una estrella")
    def informacion(self):
        print("tine una temperatura de", self.temperatura, "tine un tamaño de", self.tamaño, "y su gravedad es", self.gravedad)

def set_temperarura(self, temperatura):
    self.__temperatura = temperatura

def get_tamaño(self, tamaño):
    return self.__tamaño 



cuerpo_celeste = cuerpo_celestes("5.772k", "696,340", "274 m/s2")
cuerpo_celeste.estrella()
cuerpo_celeste.informacion()

class planetas(cuerpo_celestes):
    def __init__(self, temperatura, tamaño, gravedad, poblacion):
        super().__init__(temperatura, tamaño, gravedad)
        self.poblacion = poblacion

    def tierra(self):
        print("la temperatura de la tierra probien de la luz solar, tiene un tamaño de", self.tamaño, "fuerza de gravedad de ", self.gravedad, "y una poblacion de", self.poblacion)

tierra = planetas("x", "6,371 km", "9.807 m/s²", "7.888 miles de millones ")
tierra.tierra()