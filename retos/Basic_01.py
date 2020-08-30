def volver(name):   
    print(f'Quieres volver a hacer otra actividad?')
    desicion_x = input('''(1) Si    (2) No, bye\n''')

    if desicion_x == "1":
        print(actividad(name))
    else: print('ok! bye XD')

def sumar(a,b):
    resultado = a + b
    print(f'{a} + {b} = {resultado}')
    return resultado

def restar(a,b):
    resultado = a + b
    print(f'{a} - {b} = {resultado}')
    return resultado

def dividir(a,b):
    if a > b and b != 0:
        print(f'En numero {b} esta {a/b} veces en {a}')
    elif b > a and a != 0:
        print(f'En numero {a} esta {b/a} veces en {b}')
    elif a == b:
        print(f'{a} y {b} son el mismo numero, asi que estan una vez sobre si mismos')
    elif a > b and b == 0 or b > a and a == 0:
        print(f'Como el menor es 0, en Matematicas daria indeterminado o Infinito')
    

def cal_div(total, num_personas, porcentaje):
    propina = (total * porcentaje)/100
    cada_persona = (total + propina)/num_personas
    print(f'\nA cada persona le toca dar {cada_persona}')

def pasar(dias):
    horas = dias * 24
    minutos = horas * 60
    segundos = minutos * 60
    print(f'''
    {dias} dias son:
    {horas} horas
    {minutos} minutos
    {segundos} segundos
    ''')

def kilometros(millas):
    if millas == 1:
        print('Una millas = 1.609344')
    else:
        km = millas * 1.609344
        print(f'Esas {millas} millas son {km} kilometros')
    


def actividad(name):
    print(f'{name}, Que quieres hacer?')

    actividad = input('''
    (1) Sumar un par de numeros
    (2) Resta pizzas
    (3) Sumamos 2 y lo Multiplicamos por otro
    (4) Edad pasada y Futura
    (5) Dividir la cuenta
    (6) Calculando días
    (7) Convirtiendo Millas
    (8) Dividir
    ''')

    if actividad == '1':
        num_1 = float(input('1° numero: '))
        num_2 = float(input('2° numero: '))
        sumar(num_1,num_2)
        volver(name)

    elif actividad == '2':
        print('''llegaste a una fiesta, Tu llevas la pizza''')
        revanadas_llevadas = float(input('Cuantas revanadas de pizza llevas? \n'))
        desicion_2 = input('''Despues de un rato veo:
        (1) Que sobraron...      (2)Que se comieron...
        ''')

        if desicion_2 == "1":
            sobraron = float(input('Que sobraron: '))
            comidas = revanadas_llevadas - sobraron
            print(f'Se comieron {comidas} revanadas. WOW! ')
        elif desicion_2 == "2":
            comidas = float(input('Que se comieron: '))
            sobraron = revanadas_llevadas - comidas
            print(f'Aun sobran {sobraron} revanada' )
        else:
            print(f'Entonces aqui hacemos referencia a la famosa frase: \n "Solo se, que Nada se" ')

        volver(name)

    elif actividad == '3':
        print('Sumamos')
        num_1 = float(input('1° numero: '))
        num_2 = float(input('2° numero: '))
        print('Multiplicado por:')
        num_3 = float(input('3° numero: '))
        resultado = sumar(num_1,num_2) * num_3
        print(f'Y lo anterior multiplicado por {num_3} es: {resultado}')
        volver(name)

    elif actividad == '4':
        edad_actual = int(input('Cual es tu edad actual?  '))
        atras = int(input('Cuantos años quieres que volvamos?  '))   
        adelante = int(input('Cuantos años quieres que agregemos?  '))

        print(f' {name} en la actualidad tienes {edad_actual}. \nHace {atras} años tenias {edad_actual - atras} años.\n En {adelante} años tendras {edad_actual + adelante}')
        volver(name) 

    elif actividad == '5':
        print('Vas con tus amigos a tu restaurante favorito y acuerdan dividir la cuenta.')
        total = float(input('Cuanto tuvieron que pagar?\n'))
        personas = int(input('Entre cuantas personas dividimos la cuenta?\n'))
        propina = float(input('Cuanto porcentaje se dejara de propina?\n'))
        cal_div(total, personas, propina)
        volver(name)

    elif actividad == '6':
        dias = int(input('Dime el numero de dias\n'))
        pasar(dias) 
        volver(name)

    elif actividad == '7':
        print('Pasemos millas a Kilometros') 
        millas = float(input('Cuantas millas pasamos? \n'))
        kilometros(millas)
        volver(name)

    elif actividad == '8':
        print('Dime 2 numeros')
        num_1 = float(input('1° numero: '))
        num_2 = float(input('2° numero: '))
        dividir(num_1,num_2)
        volver(name)


if __name__ == "__main__":
    print('''Hola, Preparado para los retos?''')
    name = input('Cual es tu nombre? \n')
    print(f'Ok! {name} tienes algun apellido? \n')
    desicion_1 = input('''(1) Si     (2) No\n''')

    if desicion_1 == "1":
        last_name = input('Cual es?\n')
        print(f'{name} {last_name}, estoy a sus ordenes.')
    else:
        print(f'Esta bien! entonces solo {name}\n')
    
    actividad(name)