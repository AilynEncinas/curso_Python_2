#============= E J E M P L O ===============
#===========================================
#lista=[1,1,2,3,3,1,4,8,3]

#lista=['diccionario','diccionario','objeto']
#for numero in lista:
#    print(numero);
#for i in range(len(lista)):
#    print(numero[i]);
#============= E J E M P L O  1 ================
listas=[1,1,2,3,3,1,4,8,3]
lista_unica=[]
print('Lista original')
print(listas)
for numero in listas:
    if(numero not in lista_unica):
        lista_unica.append(numero)
print('Lista sin re peticiones')
print(lista_unica)
lista_unica_2=set(listas)
print(lista_unica_2)
print(type(lista_unica_2))
#===============================================
#============= E J E M P L O  2 ================
grupo1=set('abracadabra')
grupo2=set('alacazam')
print(grupo1)
print(grupo2)
print(grupo2-grupo1)
print(grupo2 | grupo1)#Sacara las letras de los dos grupos sin repetirce
print(grupo2 & grupo1)#Saca lo que se repite entre los dos
print(grupo1 ^ grupo2)#Saca todo menos lo que se repite
#===============================================
#============= E J E M P L O  3 ================