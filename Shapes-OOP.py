from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self):
        self.unit = "meters"
    
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass
    @abstractmethod
    def display(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius
    
    def area(self):
        ar = (3.14159 * (self.radius)**2)
        return "Area: {:.2f} {} squared".format(ar, self.unit)
    
    def perimeter(self):
        circumference = (2 * 3.14159 * self.radius)
        return "Perimeter: {:.2f} {} squared".format(circumference, self.unit)
    
    def display(self):
        return "Circle - Radius: {} {}".format(self.radius, self.unit)

class Rectangle(Shape):
    def __init__(self, height, width):
        super().__init__()
        self.height = height
        self.width = width
    
    def area(self):
        ar = self.height * self.width
        return "Area: {:.2f} {} squared".format(ar, self.unit)
    
    def perimeter(self):
        per = 2 * (self.height + self.width)
        return "Perimeter: {:.2f} {} squared".format(per, self.unit)
    
    def display(self):
        return "Rectangle - Width: {} {}, Height: {} {}".format(self.width, self.unit, self.height, self.unit)


cir = Circle(2)
rect = Rectangle(23, 10)

print(cir.display())
print(cir.area())
print(cir.perimeter()+"\n")

print(rect.display())
print(rect.area())
print(rect.perimeter())
