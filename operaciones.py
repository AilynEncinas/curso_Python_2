import csv
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
def leer_csv(ruta):
    resultado=[]
    with open(ruta,'r') as archivo:
        dtos_csv=csv.DictReader(archivo)
        for fila in dtos_csv:
            resultado.append(fila)
    return resultado
def registrar_csv(fila,ruta):
    data=leer_csv(ruta)
    id = data[-1]['id']
    id= int(id)
    id += 1
    #id=int(data[-1]['id'])+1  
    fila['id']=id
    with open(ruta,'a', newline='') as archivo:
        escritura=csv.DictWriter(archivo,fieldnames=fila.keys())
        escritura.writerow(fila)