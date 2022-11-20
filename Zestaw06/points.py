# Marlena Gryt
# Python 2022/2023
# Zd 6.2 

import math

# Klasa reprezentujaca punkty na plaszczyznie.
class Point:
    
    def __init__(self, x, y):  
        self.x = x
        self.y = y

    def __str__(self):             
        return '({}, {})'.format(self.x, self.y)

    def __repr__(self):            
        return 'Point({}, {})'.format(self.x, self.y)

    def __eq__(self, other):        
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):        
        return not self == other

    # Punkty jako wektory 2D.
    def __add__(self, other):      
        return Point(self.x + other.x, self.y + other.y)
        
    def __sub__(self, other):       
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other):       
        return self.x * other.x + self.y * other.y

    def cross(self, other):         
        return self.x * other.y - self.y * other.x

    def length(self):              
        return math.sqrt(pow(self.x, 2) + pow(self.y, 2))

    def __hash__(self):
        return hash((self.x, self.y)) 
