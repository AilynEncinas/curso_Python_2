import operaciones
productos={
    'cereales': 58,
    'carne':150,
    'gaseosas':84,
    'arroz':259,
    'papel':78,
    'maletas':598
}
iva=(operaciones.calcular(productos,operaciones.porcentaje))
desc=(operaciones.calcular(productos,operaciones.descuent))

print(f'Iva:{iva}')