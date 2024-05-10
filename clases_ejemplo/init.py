from humano import Humano 
from humano_2 import Humano2
marco = Humano(nombre='Marco', edad=26)
marco.saludar()

elisa = Humano(nombre='Elisa', edad=22)
elisa.saludar()

eduardo = Humano2()
eduardo.crear(  edad=25, 
                nombre='Eduardo', 
                estatura=1.7, 
                genero='Masculino')
ana = Humano2()
ana.crear(  edad=18, 
                nombre='Ana', 
                estatura=1.6, 
                genero='Femenino')
eduardo.saludar()
ana.saludar()