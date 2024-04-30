#####################################################################################################################
############################################      Condicional   IF     ##############################################
#####################################################################################################################
numero=input('Ingresa un numero entero:  ')
numero=int(numero)
if (numero%2==0) and (numero%2<50):
    print(f'El numero {numero} es par y es menor a 50')
elif (numero%2==0) and (numero%2>50):
    print(f'El numero {numero} es par y es mayor a 50')
else:
    print(f'El numero {numero} es impar')