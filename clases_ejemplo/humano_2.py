class Humano2():
    def crear(self, edad, nombre, estatura, genero):
        self.estatura_c = estatura
        self.genero_c = genero
        self.edad_c = edad
        self.nombre_c = nombre

    def saludar(self):
        print(f'Hola soy {self.nombre_c} tengo {self.edad_c} año.')
        print(f'Estatura: {self.estatura_c}  genero: {self.genero_c}')