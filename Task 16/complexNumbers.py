class Complex:

    def __init__(self, x, y):
        self.re = x
        self.im = y
    
    def __str__(self):
        return "{} {} {}i".format(self.re, '+' if self.im >= 0 else '-', abs(self.im))

    #returns a conjugate of the original complex number
    def conjugate(self):
        return Complex(self.re, -self.im)

    #multiply
    def __mul__(self, other):
        re = self.re * other.re - self.im * other.im
        im = self.im * other.re + self.re * other.im
        return Complex(re, im)


    #The following methods are not required in this project. The implementation is for learning purposes.

    #for Addition
    def __add__(self, other):
        return Complex(self.re + other.re, self.im + other.im)
    
    #for subtraction
    def __sub__(self, other):
        return Complex(self.re - other.re, self.im - other.im)
    
    #for negation
    def __neg__(self):
        return Complex(-self.re, -self.im)

   
#Tests
c1 = Complex(10, 20)
c2 = Complex(1, -2)
print(c1 + c2)
print(c1 - c2)
print(-c1)
print(c1)
print(c1.conjugate())
print(c1 * c2)
