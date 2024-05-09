import csv
with open(r'C:\Users\itic\Desktop\Python_3\archivos\ventas.csv','r') as archivo:
    dtos_csv=csv.DictReader(archivo)
    for fila in dtos_csv:
        print(fila)