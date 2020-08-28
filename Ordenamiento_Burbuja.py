import random

def Burbuja(lista):
    n = len(lista)

    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

if __name__ == '__main__':
    tamano_lista = int(input('De que tamaño quieres que sea la lista: '))
    print('''
    __D I M E   E L   R A N G O__
    ''')
    R_inf = int(input('R_inferior = '))          
    R_sup = int(input('R_superior = '))          

    lista = ([random.randint(R_inf, R_sup) for i in range(tamano_lista)])
    print(lista)
    print(Burbuja(lista))