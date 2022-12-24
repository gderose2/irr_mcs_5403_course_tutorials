#!/usr/bin/env python3
import math

# Circle class example
class Circle():
    # Set attributes
    unit = 'cm'
    
    # Instance attribute
    def __init__(self, xc, yc, radius):
        self.x_center = xc
        self.y_center = yc
        self.radius = radius

    # Methods
    def area(self):
        a = math.pi * self.radius**2.0
        return a

    def cylinder_vol(self, height):
        volume = self.area() * height
        return volume

if __name__ == '__main__':
    # Define a circle object
    my_circle = Circle(1, 2, 1)
    print('Circle area = %.2f %s^2' % (my_circle.area(), my_circle.unit) )
    print('Cylinder Volume = %.2f %s^3' % ( my_circle.cylinder_vol(2.0),
                                            my_circle.unit) )

