# -*- coding: utf-8 -*-

# 03/06/2022
# father class
class Poligon:
    def __init__(self, number_of_sides):
        self.n     = number_of_sides
        self.sides = [0 for i in range(number_of_sides)]
        
    def read_sides(self):
        self.sides = [float(input("Inform the side {} size: ".format(i+1) ))
                      for i in range(self.n)]
    
    def show_sides(self):
        for i in range(self.n):
            print("Side {} has the size of {}.".format(i+1, self.sides[i]) )
            
## Test the class
#pentagon = Poligon(5)
#pentagon.read_sides()
#pentagon.show_sides()

# doughter class
class Triangle(Poligon):
    def __init__(self):
        Poligon.__init__(self, 3)
    
    def calculate_area(self):
        a, b, c = self.sides
        s = (a + b + c)/2
        area = ( s*(s-a)*(s-b)*(s-c) )**0.5
        print('The triangle area is %0.2f' %area)
        return area

## Test the class
#triangle = Triangle()
#triangle.read_sides()
#triangle.calculate_area()

class Rectangle(Poligon):
    def __init__(self):
        Poligon.__init__(self, 4)
            
    def read_sides(self):
        self.sides = [float(input("Inform the side {} size: ".format(i+1) ))
                      for i in range(2)]
    
    def calculate_area(self):
        a, b = self.sides
        area = a*b
        print('The triangle area is %0.2f' %area)
        return area

    def calculate_diagonal(self):
        a, b = self.sides
        diagonal = (a**2 + b**2)**0.5
        print('The diagonal is {}.'.format(diagonal))
        return diagonal
        
## Test the class
#rectangle = Rectangle()
#rectangle.read_sides()
#rectangle.calculate_area()
#rectangle.calculate_diagonal()

class RectangleTriangle(Triangle):        
    def isRectangleTriangle(self):
        h  = max(self.sides)
        c1 = min(self.sides)
        c2 = (h**2 - c1**2)**0.5
        if (c2 in set( self.sides )):
            print('Yes, it is a triangle rectangle.')
            return True
        else:
            return False
            print('No, it is not a triangle rectangle.')
            
## Test the class
triangle = RectangleTriangle()
triangle.read_sides()
triangle.calculate_area()
triangle.isRectangleTriangle()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        