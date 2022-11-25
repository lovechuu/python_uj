# Marlena Gryt
# Python 2022/2023
# Zd 7.3

from points import Point

# Klasa reprezentująca prostokąty na płaszczyźnie.
class Rectangle:

    def __init__(self, x1, y1, x2, y2):
        if x1 >= x2 or y1 >= y2:
            raise ValueError("Invalid vertices values")
        else:
            self.pt1 = Point(x1, y1)
            self.pt2 = Point(x2, y2)

    def __str__(self): 
        return '[({}, {}), ({}, {})]'.format(self.pt1.x, self.pt1.y, self.pt2.x, self.pt2.y)

    def __repr__(self): 
        return 'Rectangle({}, {}, {}, {})'.format(self.pt1.x, self.pt1.y, self.pt2.x, self.pt2.y)

    def __eq__(self, other): 
         return self.pt1 == other.pt1 and self.pt2 == other.pt2

    def __ne__(self, other): 
        return not self == other

    def center(self): 
        return Point((self.pt1.x + self.pt2.x) / 2, (self.pt1.y + self.pt2.y) / 2)

    def area(self): 
        return abs(self.pt1.x - self.pt2.x) * abs(self.pt1.y - self.pt2.y)

    def move(self, x, y): 
         return Rectangle(self.pt1.x + x, self.pt1.y + y, self.pt2.x + x, self.pt2.y + y)

    def intersection(self, other): 
        x1 = max(self.pt1.x, other.pt1.x)
        y1 = max(self.pt1.y, other.pt1.y)
        x2 = min(self.pt2.x, other.pt2.x)
        y2 = min(self.pt2.y, other.pt2.y)
        if x1 >= x2 and y1 >= y2:
            raise ValueError("No intersection")
        else:
            return Rectangle(x1, y1, x2, y2)

    def cover(self, other): 
        return Rectangle(min(self.pt1.x, other.pt1.x), min(self.pt1.y, other.pt1.y), max(self.pt2.x, other.pt2.x), max(self.pt2.y, other.pt2.y))

    def make4(self):            
        rect1 = Rectangle(self.pt1.x, self.center().y, self.center().x, self.pt2.y)
        rect2 = Rectangle(self.pt1.x, self.pt1.y, self.center().x, self.center().y)
        rect3 = Rectangle(self.center().x, self.pt1.y, self.pt2.x, self.center().y)
        rect4 = Rectangle(self.center().x, self.center().y, self.pt2.x, self.pt2.y)
        return rect1, rect2, rect3, rect4
