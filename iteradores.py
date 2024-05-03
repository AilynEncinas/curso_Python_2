num=[1,2,3,4,5,6,7,8,9,10]#Lista de numeros
animales=['Perro','Gato','Tigre'] #Lista de animales
for num in num:#Para mostrar cada elemento de la lista 'num'
    print('el numero es: '+str(num)+' y su potencia es: '+str(num**2))#Para mostrar cada elemento de la lista mas su potencia

for i in range(len(animales)):#Para mostrar cada elemento de la lista
    print(f'{i} .- {animales[i]}')#Para mostrar cada elemento junto a  la posicion que ocupa este

################################################################
#########################  R A N G O S #########################
################################################################
for i in range(2,10,2):#Como se entiende lo que esta entre los parentecis (2,10,2) la primera parte dice (2,10'del 2 hasta el 10',2'de dos en dos')
    print(i)#Se imprimira los numeros del 2 al 10 de dos en dos
#########################################################################################
#########################  I N S T A N C I A R      A R R A Y S #########################
#########################################################################################
potencias=[x**2 for x in range(1,11)]#Para la creacion de arrays se utilizara range(1,11)'este tomara los numeros que se encuentran del 0 hasta    el 10 que es un numero antes del 11'
print(potencias)

lista=[]
for x in range(1,11):
    lista.append(x**2)
print(lista)


################################################################
########################  E J E M P L O ########################
################################################################
#Dada a una lista de edades mostra las que son menores de edad y las que son Mayores de edad
edades=[3,45,12,18,17,2,98,25,64,16,51]

for edad in edades:
    if edad>=18:
        print(f'{edad} es mayor de edad')
    else:
        print(f'{edad} es menor de edad');
################################################################
##########################  T A R E A ##########################
################################################################
#Crear un programa quue imprima un tablero de tamaño variable
print('ingresa el tamaño que sera tu tablero')
tam=int(input())
for i in range(tam):
    for j in range(tam):
        if(i%2==0 and j%2==0):
            print('#', end=' ')
        if(i%2!=0 and j%2!=0):
            print(' ', end='#')
    print();