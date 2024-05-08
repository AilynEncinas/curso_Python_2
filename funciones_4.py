#
#            Ejercicio 1
#
productos={
    'arroz':58,
    'gaseosa':50,
    'trigo':25,
    'arina':100
}
def porcentaje(numero,porcentaje=13):
    resultado =numero*(porcentaje/100)
    return resultado

#Que calcule un despuento
def descuent(num):
    if(num>100):
        resultado=porcentaje(num,15)
    else:
        resultado=porcentaje(num,5)
    
    return resultado
print('Ingresa in numero')
num=int(input())
total_des=descuent(num)
print(f'El descuento es de {total_des}')
#
#            Ejercicio 2
#
def calcular(lista,funcion):
    total=0
    for producto,precio in lista.items():
        total+=funcion(precio)
    return total
print(calcular(productos,descuent))