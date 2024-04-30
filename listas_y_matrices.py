#####################################################################################################################
#############################################           Listas        ###############################################
#####################################################################################################################
impares= [1,3,5,7,9,11,13,15,17,19]
print(impares)#Con este print podemos ver la lista entre corchetes
print (type(impares))#Para ver el tipo de dato
print(impares[4])#Nos mostrara el elemento en la posicion 4
print(impares[-6])#Nos mostrara el elemento en la posicion -6(ya que esta en negativo la cuenta es desde atras y se empieza por el -1)
print(impares[:4])#Desde el inicio hasta mostrar 4 elementos
print(impares[4:])#Despues del cuarto elemento se imprimira
print(impares[4:6])#Para sacar un intervalo(los valores del centro)
print(impares[-4:-1])#Para sacar un intervalo con negativos
lista_alfanumerica=['a',1,'b',2,'c',3]
print(lista_alfanumerica)#Con este print podemos ver la lista entre corchetes sin ningun problema
print(len(lista_alfanumerica))#Con este print podemos ver el tamaño de la lista
medio=len(lista_alfanumerica)//2#Para calcular el medio de la lista
print(lista_alfanumerica[medio])#Para imprimir el medio

#Experimento Will
print('SE SACA DE LOS 4 ELEMENTOS HASTA EL FINAL')
print(impares[4:])
print('SE DEVUELVE DESDE EL INICIO HASTA 8 ELEMENTOS')
print(impares[:8])
print('Union')
print(impares[4::8])#Devuelve el primer elemento del intervalo entre la lista(9,11,12,15)
#Fin del experimento

impares.reverse()#Para imprimir la lista alrevez
#La funcion reverse se opera sobre la varioable y esta devuelve un valor si esta funcion es usada cuando se asigna a una variable como se 'num= impares.reverse()' esto generara un error y devolvera un calor null o 'NONE'
print(impares)

#####################################################################################################################
############################################           Matrices        #############################v################
#####################################################################################################################
print('Matrices:  ')
matriz=[
    [1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13,14,15]
]
#Para imprimir una matriz se tiene dos espacio entre conchetes despues de la matriz por ejem: 'matriz[][]' en este caso ls valores que se imprimiran sera la fila y la posicion, pero tambien se puede imprimir toda una fila por ejem 'matriz[]'
print(matriz[1])#Mostrara toda la fila 1
print(matriz[1][2])#Mostrara la fila 1 y la el elemento que se encuentra en la posicion 2