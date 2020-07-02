def mayor_menor(a,b):
    if a > b: print(f'{a} es mayor que {b}')
    elif a < b: print(f'{b} es mayor que {a}')
    elif a == b: print('Son el mismo numero')

def rango_estable(limite,num):
    if num < limite : print(f'El numero {num} se encuentra en el rango')
    elif limite < num: print(f'El numero {num} excede el limite permitido')
    elif  limite == num : print('Estas en el limite, cuidado')

def rango_cambiante(lim_1,lim_2,comparacion):
    if lim_1 < lim_2:
        lim_inferior = lim_1
        lim_superior = lim_2
    elif lim_2 < lim_1:
        lim_inferior = lim_2
        lim_superior = lim_1
    elif lim_1 == lim_2 and comparacion == lim_1: return print('Encerio? los 3 iguales?')
    elif lim_1 == lim_2 and comparacion < lim_1: return print(f'{comparacion} es menor a {lim_1}')
    elif lim_1 == lim_2 and comparacion > lim_1: return print(f'{comparacion} es mayor a {lim_1}')

    if comparacion < lim_superior and comparacion > lim_inferior:
        print(f'{comparacion} esta dentro del rango de {lim_inferior} y {lim_superior}')
    elif comparacion > lim_superior: print(f'{comparacion} sobrepasa a {lim_superior} por {comparacion - lim_superior}')
    elif comparacion < lim_inferior: print(f'{comparacion} esta por debajo del limite')
    elif comparacion == lim_inferior and comparacion != lim_superior : print('Cuidado estas en el limite mas bajo')
    elif comparacion == lim_superior and comparacion != lim_inferior : print('Wow! estas apunto de salirte del limite')
    else: print('Intenta poner bien los numeros la proxima vez')

def i_like_turtles(animal):
    animal = animal.lower()
    animal = animal.replace(" ", "")
    if animal== 'tortuga' or animal == 'tortugas': print('Tambien me gustan las tortugas')
    else: print('Ese animal es genial, pero prefiero las tortugas')

def clima():
    print('Solo responsi si o no a las preguntas')
    desicion_1 = input('\nPregunta, Esta lloviendo? \n')
    if desicion_1.lower() == 'si':
        desicion_1_2 = input('\nY dime, hace mucho viento? \n')
        if desicion_1_2.lower() == 'si' :
            print('\nSi hace mucho viento, sera dificil salir con una sobrilla')
        elif desicion_1_2.lower() == 'no':
            print('\nSi vas a salir lleva contigo una sombrilla')
        
    elif desicion_1.lower() == 'no':
        desicion_2_2 = input('\nAsi que es un dia fresco? \n') 
        if desicion_2_2.lower() == 'si' :
            print('\nQue clima tan agradable')
        elif desicion_2_2.lower() == 'no':
            print('\nLo mejor sera buscar una piscina')
    else:
        print('\n Entonces "Solo se que nada se"')

    print('Que tengas un bonito dia')

def edad_permitida(edad):
    if edad > 30: print('Nunca es tarde para aprender. Que curso tomaremos?')
    elif edad >= 18 and edad < 30: print('Es un momento excelente para impulsar tu carrera.')
    elif edad < 18: print('Sabes hacia donde dirigir tu futuro? Seguro puedo ayudarte.')
    
def mensajes_numerados(numero):
    if numero == '1':
        print('Hoy aprenderemos sobre prorgamación')
    elif numero == '2':
        print('¿Qué tal tomar un curso de marketing digital?')
    elif numero == '3':
        print('Hoy es un gran día para comenzar a aprender de diseño')
    elif numero == '4':
        print('¿Y si aprendemos algo de negocios online?')
    elif numero == '5':
        print('Veamos un par de clases sobre producción audiovisual')
    elif numero == '6':
        print('Tal vez sea bueno desarrollar una habilidad blanda en Platzi')
    else:
        print('No tengo un mensajito para eso')


    

