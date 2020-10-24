####################################################################################
# ========================
# Part 1: Vector and Complex Numbers
# ========================

# In this exercise you will use what you have learned to implement a Vector
# class and a complex number class.

# ========================
# The Vector class
# ========================

# Write definitions for a class called Vector.
# Your definition should include a constructor,  __str__, values for the x and y
# coordinates, and methods for addition and subtraction of vectors, scalar multiplication,
# length, and comparison.
import math

class Vectors(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    #addition
    def __add__(self, other):
        return Vectors(self.x + other.x, self.y + other.y)

    #subtraction
    def __sub__(self, other):
        return Vectors(self.x - other.x, self.y - other.y)
    
    #multiplication
    def __mul__(self, other):
        return self.x*other.x + self.y*other.y

    def __abs__(self):
        return math.sqrt(self.x**2 + self.y**2)
    
    #length, will always be two for a valid vector in this project
    def __len__(self):
        return 2
    
    #checks for comparison    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    #our toString
    def __str__(self):
        return '(%g, %g)' % (self.x, self.y)

   
#Complex Numbers: Derived Class from vectors

class Complex(Vectors):

    def __init__(self, x, y):
        super(Complex, self).__init__(x, y)
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
print(-c2)
print(c1)
print(c2.conjugate())
print(c1 * c2)
