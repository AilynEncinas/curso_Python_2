#╔═╗╝║╚
#===============================================
#============= E J E M P L O  1 ================
#============= F U N C I O N E S ================
'''
    def                 name               (n)             :                                          ╔══════════════════════════════════════╗
 definicion     nombre de la funcion    parametros     delimitador                                    ║    Nota: la funcion devuelve algo    ║    valores                                                                                              ╚══════════════════════════════════════╝

 │
'''
def suma(a,b):
    c=a+b
    return c
resultado=suma(7,5)
print(resultado)
#===============================================
#============= E J E M P L O  2 ================
#================ M E T O D O ==================
def suma(a,b):                                                                                        #╔══════════════════════════════════════╗
    c=a+b                                                                                             #║  Nota: El metodo no devuelve nada    ║
    print(c)                                                                                          #╚══════════════════════════════════════╝

suma(8,6)

#====================================================
#============= E J E R C I C I O   1 ================
#================== M E T O D O =====================
def fibonacci(lim):
    a=0
    b=1
    limite=lim
    while a<limite:
        print(a, end=' ')    
        a,b=b,a+b
print('Ingresa tu limite')
lim=int(input())
print(fibonacci(lim))
#====================================================
#============= E J E R C I C I O   1 ================
#================  F U N C I O N ====================
def fibonacci2(lim):
    fibo=[]
    a=0
    b=1
    limite=lim
    while a<limite:
        fibo.append(a)    
        a,b=b,a+b
    return(fibo)
print('Ingresa tu limite')
limi=int(input())
serie_fibonacci=fibonacci2(lim)
print(serie_fibonacci)