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
def calcular(lista,funcion):
    total=0
    for producto,precio in lista.items():
        total+=funcion(precio)
    return total