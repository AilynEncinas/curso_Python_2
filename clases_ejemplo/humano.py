class Humano():
    def __init__(self,edad,nombre):
        self.edad = edad
        self.nombre = nombre
    def saludar(self):
        print(f'Hola soy {self.nombre} tengo {self.edad}')