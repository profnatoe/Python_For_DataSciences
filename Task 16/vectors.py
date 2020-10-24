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

   
