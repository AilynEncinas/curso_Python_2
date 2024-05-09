import operaciones


print('--------------------------------------------------------------------------------------------')
ruta=r'C:\Users\itic\Desktop\Python_3\archivos\ventas.csv'
nueva_veta={
    'id': 0,
    'codigo_cliente':100000,
    'cliente':'Gabriel',
    'producto':'Papas Fritas',
    'precio':68,
    'descuento':'',
    'iva':''
}
operaciones.registrar_csv(nueva_veta,ruta)


lectura = True
while lectura:
    accion = input('Deseas agregar? (si/no) ')
    if (accion == 'si'):
        nueva_venta={}
        nueva_venta['id']=int(input(' '))
        nueva_venta['codigo_cliente']=int(input('ingresa tu codigo:    '))
        nueva_venta['cliente']=str(input('Ingresa el nombre del cliente:    '))
        nueva_venta['producto']=str(input('Ingresa el producto que deseas comprar:    '))
        nueva_venta['precio']=int(input('Ingresa su precio:    '))
        
        operaciones.registrar_csv(nueva_venta,ruta)
        terminar=True
        while terminar==False or terminar==True:
            terminar=input('Deseas terminar(si/no)')
            if(terminar=='si'):
                lectura=False
            elif(terminar=='no'):
                lectura=True
            else:
                print('No ingresaste una opcion valida')

            
    elif(accion=='no'):
        print()
        lectura = False
    else:
        print('No ingresaste una opcion valida')