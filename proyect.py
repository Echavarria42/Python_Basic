from Vectorial.math_basic import promedio 

nota_prom = 5

def prob_Alumno_Maestro(lista):
    return promedio([promedio(lista),nota_prom])


if __name__ == '__main__':
    print(prob_Alumno_Maestro([5,4,3,4,5,4.5,3.5,2,2.3,1]))


