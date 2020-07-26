print('¿ T E   E N C U E N T R O   L A   R A I Z   C U A D R A D A ?')
objetivo= int(input('Dime el numero:'))
metodo= int(input('''
    Que metodo quieres?
    (1) = Enumeracion
    (2) = Aproximacion
    (3) = Busqueda Binaria
    '''))

epsilon = 0.01
paso = epsilon**2
bajo = 0.0
alto = max(1.0, objetivo)
respuesta = 0.0
respuesta_bin = (alto+bajo)/2

def enumeracion(respuesta, objetivo):
    while (respuesta)**2 < objetivo:
        respuesta += 1
    if respuesta**2 == objetivo:
        print(f'La raiz cuadrada de {objetivo} es {respuesta} por medio de enumeracion')

    else:
        print(f'El {objetivo} no tiene una raiz cuadrada por medio de enumeracion')  

def aproximacion(respuesta, objetivo, epsilon, paso) :
    while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
        respuesta += paso

    if abs(respuesta**2 - objetivo) >= epsilon:
        print(f'No se encontro la raiz cuadrada de {objetivo} por medio de aproximacion')

    else:
        print(f'La raiz cuadrada de {objetivo} es {respuesta} por medio de aproximacion')

def busq_Bin(respuesta, objetivo, epsilon, bajo, alto):
    while abs(respuesta**2 - objetivo) >=epsilon:
        if respuesta**2 < objetivo:
            bajo = respuesta
        else:
            alto = respuesta

        respuesta = (alto+bajo)/2

    print(f'La raiz cuadrada de {objetivo} es {respuesta} por medio de busqueda binaria')


if metodo == 1:
    enumeracion(respuesta, objetivo)

if metodo == 2 :
    aproximacion(respuesta, objetivo, epsilon, paso)

if metodo == 3 :
    busq_Bin(respuesta_bin, objetivo, epsilon, bajo, alto)

