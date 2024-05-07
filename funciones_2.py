def porcentaje(num,por=10):
    res=por * (num/100)
    return res
print('Ingresa el numero del que quieres sacar un porcentaje')
num=int(input())
print('Ingresa el porcentaje')
por=int(input())
resultado=porcentaje(num,por)
print(f'Tu resultado es {resultado}')

def aplicar_lista(listas):
    resultado_porcentaje=[]
    for numero in listas:
        resultado=porcentaje(numero)
        resultado_porcentaje.append(resultado)
    return resultado_porcentaje

#print('Ingresa el tamaño de la lista')
#tam_lis=int(input())
listas=[50,10,512,45]
resultado_porcentaje=aplicar_lista(listas)
print(resultado_porcentaje)