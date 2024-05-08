import csv
with open('ventas.csv','r') as archivo:
    dtos_csv=csv.DictReader(archivo)
    for fila in dtos_csv:
        print(fila)