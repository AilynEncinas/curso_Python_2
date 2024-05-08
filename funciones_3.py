productos={
    'arroz':58,
    'gaseosa':50,
    'trigo':25,
    'arina':100
}
def porcentaje(numero,porcentaje):
    resultado =numero*(porcentaje/100)
    return resultado

#interar mi lista y calcular el IVA acumulado
#       for clave, valor en diccionario.items();

listas=[]

def total(lista):
    total=0
    for producto, precio in lista.items():
        total +=porcentaje(precio,13)
    return total
total_iva=total(productos)
print(total_iva)