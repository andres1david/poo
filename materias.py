class materia:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
    
    def imprimir(self):
        print("materia: ", self.nombre)
        print("nota: ", self.nota)
        print("")

materia1 = materia("matematica", 2)
materia2 = materia("artes", 5)
materia3 = materia("sociales", 3)

def set_nombre(self, nombre):
    self.__nombre = nombre

def get_nota(self, nota):
    return self.__nota

materia1.imprimir()
materia2.imprimir()
materia3.imprimir()


class puntos_extra(materia):
    def __init__(self, nombre, nota, puntos):
        super().__init__(nombre, nota)
        self.puntos = puntos

    def cuantos(self):
        print(f"se le otoegaron  {self.puntos} puntos extra")

puntos_extra1 = puntos_extra("matematicas", 2, 5)

puntos_extra1.cuantos()