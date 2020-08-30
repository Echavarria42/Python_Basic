import math

def multiplicar(a,b):
    print(a*b)
    return (a*b)

def redondiar(num, dig):
    if dig == 0:
        return print(int(num))
    else:
        a = round(num, dig)
        return print(a)

def raiz(a):
    return print(round((a**0.5),3))

def circulo(radio):
    return (math.pi*(radio**2))

def cilindro(radio, altura):
    return (circulo(radio) * altura)

def entero_residuo(num, divisor):
    entero = int(num // divisor)
    residuo = num - (entero*divisor) 
    if entero == 1 and residuo == 0:
        print(f'Son los mismos numeros')
    elif residuo == 0:
        print(f'El numero {divisor} esta {entero} veces, sin residuo')
    else:
        print(f'El numero {divisor} esta {entero} veces, y sobra {residuo}')

def area_perimetro(num_lados, distancia_lado):
    perimetro = num_lados*distancia_lado
    a = 360/num_lados
    apotema = (distancia_lado/2)/math.tan(math.radians(a/2))
    area = (perimetro * apotema)/2
    print(f'Perimetro = {perimetro} \nArea = {area}')

if __name__ == "__main__":
    print('Dime 2 numeros para multiplicar')
    num_1 = float(input('1° Numero: '))
    num_2 = float(input('2° Numero: '))
    num_mult = multiplicar(num_1, num_2)

    dig = int(input('\n¿A cuantas cifras aproximo? \n'))
    redondiar(num_mult, dig) 

    num_3 = float(input('\nDime un numero, Le saco raiz cuadrada: '))
    raiz(num_3) 

    radio = float(input('\nDime el radio de un circulo: '))
    print(f'El area del circulo es: {circulo(radio)}')

    print('\nTe calculo el volumen de un cilindro')
    radio_cilindro = float(input('Dime el radio de la base\n'))
    altura_cilindro = float(input('Dime la altura del cilindro\n'))
    print(f'El volumen del cilindro es: {cilindro(radio_cilindro, altura_cilindro)}') 

    entero = float(input('Dime un numero: '))
    divisor = float(input('Dime por que numero lo divido: '))
    entero_residuo(entero, divisor)

    print('\nTe digo el area y el perimetro de cualquier poligono regular')
    numero_lados = float(input('Dime cuantos lados tiene: '))
    lado = float(input('Cuanto mide cada lado: '))
    area_perimetro(numero_lados,lado)