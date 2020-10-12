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



if __name__ == '__main__':
    v_1 = Vector([1,1,1])
    v_2 = Vector([2,2,2])
    v_3 = Vector([3,3,3])


    print(v_1.restar(v_2))

