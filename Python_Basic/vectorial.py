from math_basic import multiplicar

class Vector:

    def __init__(self, vector):
        self.dimencion = len(vector)
        self.vector = vector
    
    def sumar(self, vector):
        if self.dimencion == vector.dimencion:
            solution = [self.vector[i] + vector.vector[i] for i in range(self.dimencion)]           
            return solution
    
    def restar(self, vector):
        if self.dimencion == vector.dimencion:
            solution = [self.vector[i] - vector.vector[i] for i in range(self.dimencion)]           
            return solution
    
    def prod_punto(self, vector):
        solution = 0
        for i in range(self.dimencion):
            solution += (multiplicar([self.vector[i], vector.vector[i]]))
        return solution  
    
    def mul_escalar(self, escalar):
        solution = [self.vector[i] * escalar for i in self.vector]
        return solution

class Matriz:

    def __init__(self, matriz):
        self.dimencion = len(matriz)
        self.matriz = matriz
    
    def sumar(self, matriz):
        solution = [Vector(self.matriz[i]).sumar(  Vector(matriz.matriz[i])  ) for i in range(self.dimencion)]
        return solution
    
    def restar(self, matriz):
        solution = [Vector(self.matriz[i]).restar(  Vector(matriz.matriz[i])  ) for i in range(self.dimencion)]
        return solution


    def mul_escalar(self, escalar):
        solution = [ Vector(i).mul_escalar(escalar) for i in self.matriz]
        return solution  

if __name__ == '__main__':
    v_1 = Vector([1,1,1])
    v_2 = Vector([2,2,2])
    v_3 = Vector([3,3,3])

    m_1 = Matriz([[1,1,1],[1,1,1],[1,1,1]])
    m_2 = Matriz([[2,2,2],[2,2,2],[2,2,2]])
    m_3 = Matriz([[3,3,3],[3,3,3],[3,3,3]])

    print(m_1.mul_escalar(5))

