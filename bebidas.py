class bebida:
    def __init__(self, sabor, cantidad):
        self.sabor = sabor
        self.cantidad = cantidad

    def jugo(self):
        print("jugo")
    def info(self):
        print("hit sabor a", self.sabor, "que contenga", self.cantidad)
    

def set_sabor(self, sabor):
    self.__sabor = sabor

def get_cantidad(self, cantidad):
    return self.__cantidad 


bebidas = bebida("mango", "250ml")
bebidas.jugo()
bebidas.info()

class gaseosa(bebida):
    def __init__(self, sabor, cantidad):
        super(gaseosa).__init__(sabor, cantidad)

    def burbugea(self):
        print("burbugea")

class jugomango(bebida):
    def __init__(self, sabor, cantidad, precio):
        super().__init__(sabor, cantidad)
        self.precio = precio

    def calidad(self):
        print(f"el jugo tiene un precio de {self.precio}")

jugo = jugomango("mango", "250ml", 2000)
jugo.calidad()

