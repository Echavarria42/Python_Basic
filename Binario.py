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
