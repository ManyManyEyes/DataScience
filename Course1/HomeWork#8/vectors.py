class Vector:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    def __add__(self, operand):
        return Vector(self.a+operand.a,
                      self.b+operand.b,
                      self.c+operand.c)
    def __mul__(self, operand):
        return Vector(self.a*operand,
                      self.b*operand,
                      self.c*operand)
    def __abs__(self):
        return (self.a**2+self.b**2+self.c**2)**.5
    
    def __bool__(self):
        return self.__abs__()>0

    def __str__(self):
        return f"{self.a},{self.b},{self.c}"

        
