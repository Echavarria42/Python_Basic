print('****************************************')
print('     __D I M E   U N   N U M E RO__')
print('****************************************')
numero = int(input('Introduce el número a convertir a binario: '))



def binario(number):
    binario = ''
    while number > 0:
    #Le añado  el  residuo  de la operacion de el numero/2 dado que en cualquiera de las  ocasiones  me  dara 0 v 1
        binario = str(number % 2) + binario

    #Divido el numero descartando el residuo haciendolo mas pequeño en cada iteracion   
        number = number // 2
    return str(number) + binario

print(binario(numero))


'''Ejemplo
    73 : 2 = 36; Resto: 1
    36 : 2 = 18; Resto: 0 
    18 : 2 = 9; Resto: 0
    9 : 2 = 4; Resto: 1
    4 : 2 = 2; Resto: 0
    2 : 2 = 1; Resto: 0

    1001001

    Se lee de abajo hacia arriba y se 
    le agrega 1 ya que no podemos 
    seguir dividiendo entre dos, 
    pues el cociente es uno. 
'''







