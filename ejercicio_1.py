print('Ingresa tu nombre')
nom=str(input())
print('Ingresa tu genero')
gen=str(input())
if(gen=='femenino' or gen=='masculino'):
    if gen.lower()=='femenino':
        if nom[0].lower()<'m':
            print('Estas en el grupo A')
        else:
            print('Estas en el grupo B')
    else:
        if nom[0].lower()<'n':
            print('Estas en el grupo A')
        else:
            print('Estas en el grupo B')
else:
    print('El genero que ingresaste no es correcto');