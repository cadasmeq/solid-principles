# Open Closed : A software entity must be open to its expansion, and closed to its modification. - Tools: Inheritance and polymorfism.
# Abierto Cerrado : Una entidad de software debe quedar abierta para su expansión y cerrada para su modificación. - Herramientas: Herencia y polimorfismo.



# Bad
class Rectangle:
    width = number
    height = number

class AreaCalculator:
    def computeArea(self, rectangles):
        area = 0
        for shape in rectangles:
            area += shape.width * shape.height
        return area

"""
Now i want to expanse my class to compute area from triangles.
"""

class AreaCalculator:
    def computeArea(self, rectangles):
        area = 0
        for shape in rectangles: 
            if shape == "Rectangle":
                area += shape.width * shape.height
            elif shape == "Triangle":
                area += shape.width * shape.height/2 # It smells
        return area


# Correct
class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    width = 100
    height = 100

    def area(self):
        return self.width * self.height

class Triange(Shape):
    width = 100
    height = 100
    def area(self):
        return self.width * self.height/2