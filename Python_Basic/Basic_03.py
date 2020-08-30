def longitud(palabra):
    palabra = palabra.replace(' ','')
    return print(f'Tu string tiene {len(palabra)} letras')

def suma_iniciales(nombre, apellido, comida, pais):
    return print(f'''    Nombre: {nombre.title()}
    Apellido: {apellido.title()}
    Pais: {pais.title()}
    Tu nombre es {nombre.title()} {apellido.title()} y tu comida favorita es {comida}''')

def fragmento(frase, r_inicial, r_final):
    return print(palabra[r_inicial-1:r_final])
    
def Upp_Low(pal_1, pal_2):
    return print(f'{pal_1.upper()} {pal_2.lower()}')

def if_nombre(nombre, apellido):
    if len(nombre) > 5:
        return print(f'Hola {nombre.title()} \n')
    else: 
       return print(f'Hola {nombre.title()} {apellido.title()} \n')
    
def pig_latin(palabra):
    vocales = ['a', 'e', 'i', 'o', 'u']
    if palabra.lower()[0] in vocales:
        palabra += 'way'
        print(palabra)
    else:
        palabra = palabra[1:] + palabra[0] + 'ay'
        print(palabra.title())

if __name__ == "__main__":
    palabra = input('Dime una palabra: ')
    longitud(palabra)

    print('\n Todo lo que respondas ponlo todo en minusculas')
    nombre = input(' Cual es tu nombre? \n')
    apellido = input(' Cual es tu apellido? \n')
    comida = input('Cual es tu comida favorita? \n')
    pais = input('De que pais eres? \n')
    suma_iniciales(nombre, apellido, comida, pais)

    print('\n Fragmentemeos una frase')
    palabra = input('Dime una frase de mas de 10 letras \n')
    r_inicial = int(input('Dime el numero por donde iniciar: '))
    r_final = int(input('Dime el numero por donde terminar: '))
    fragmento(palabra, r_inicial, r_final)

    print('\n Dime 2 palabras')
    pal_1 = input('primera palabra: ')
    pal_2 = input('segunda palabra: ')
    Upp_Low(pal_1, pal_2)

    if_nombre(nombre, apellido)

    palabra_pig = input('\n Dime un palabra y la paso a Pig Latin \n')
    pig_latin(palabra_pig)
    