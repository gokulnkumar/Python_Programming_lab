from graphics import circle, rectangle
from graphics.threeDgraphics import cuboid
from graphics.threeDgraphics.sphere import area as sphere_area
from graphics.threeDgraphics.sphere import perimeter as sphere_perimeter

print("Rectangle Area ",rectangle.area(10, 50))
print("Rectangle Perimeter ",rectangle.perimeter(10, 50))

print("Circle Area " ,circle.area(10))
print("Circle Perimeter ",circle.perimeter(10))

print("Cuboid Area ",cuboid.area(2, 3, 5))
print("Cuboid Perimeter ",cuboid.perimeter(2, 3, 5))

print("Sphere Area ",sphere_area(25))
print("Sphere Perimeter ",sphere_perimeter(25))