class Rectangle:

    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    
    def compare(self, other):
        """  Return True if other > self else False """
        a1 = self.area()
        a2 = other.area()
        return True if a2 > a1 else False


    def area(self):
        return self.length * self.breadth
    
    def perimeter(self):
        return 2 * (self.length + self.breadth)

rectangle_1 = Rectangle(10, 5)
rectangle_2 = Rectangle(10, 5)

print("Rectangle 1 Area:" , rectangle_1.area())
print("Rectangle 1 Perimeter:" , rectangle_1.perimeter())

print("Rectangle 2 Area:" , rectangle_2.area())
print("Rectangle 2 Perimeter:" , rectangle_2.perimeter())

print(rectangle_1.compare(rectangle_2))
