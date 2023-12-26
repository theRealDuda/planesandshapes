"""This module is a simulation of a plane with shapes on it
"""
from copy import deepcopy

PI = 3.14159

class Shape:
    """ Class implementing a parent shape class"""
    name = 'generic shape'
    color = 'black'

    def __init__(self):
        pass

    def __str__(self) -> str:
        return "This is a parent shape class."

    def perimeter(self):
        """Virtual function for calculating the perimeter of a shape""" 

    def area(self):
        """Virtual function for calculating the area of a shape"""

    def set_color(self, color):
        """Setter for the color attribute. Accepts a string: color"""
        self.color = color


class Plane:
    """Shape class, used to store shape objects
    """
    stuff = []

    def __init__(self):
        pass

    def remove_shape(self, num):
        removed_shape = -1
        if len(self.stuff) > 0:
            while not str(removed_shape).isdigit()\
                    or 0 > int(removed_shape)\
                    or int(removed_shape) >= len(self.stuff):
                removed_shape = num
            self.stuff.pop(int(removed_shape))
        else:
            return 0
        
    def get_rect_points(self, points):
        """Function for getting a formatted list
        for the initializaton of a Rectangle object"""
        flag = False
        cycles = -1
        while not flag:
            for point in points:
                if len(point) != 2:
                    return 0
                for coord in point:
                    if not coord.lstrip("-").isdigit():
                        return 0
            flag = True
        return points

    def get_circle_info(self, data):
        """Function for getting a formatted list
        for the initializaton of a Circle object"""
        info = []
        flag = False
        while not flag:
            centre = data[0]
            radius = data[1]
            if len(centre) != 2:
                return 0
            for item in centre:
                if not item.rstrip("-").isdigit():
                    return 0
            if not radius.isdigit():
                return 0
            flag = True
        info = [centre, radius]
        return info

    def add_shape(self, shape, text):
        """Function for the addition of a shape"""
        shape_chosen = shape
        if shape_chosen == '1':
            circleinf = self.get_circle_info(text)
            new = Circle(circleinf[0], circleinf[1])
            self.stuff.extend([new])
        if shape_chosen == '2':
            rectinf = self.get_rect_points(text)
            if not rectinf:
                return 0
            else:
                new = Rectangle()
                new.set_vertices(rectinf)
                self.stuff.extend([new])

    def __str__(self):
        if self.stuff == []:
            return "No shapes!"
        rstr = ''
        for i in self.stuff:
            rstr+= i.__str__()
        return rstr

    def get_shapes(self):
        """Getter for all shapes in a plane"""
        return self.stuff


class Rectangle(Shape):
    """Class implementing a Rectangle Shape object"""

    vertices = [[0, 0], [0, 0], [0, 0], [0, 0]]

    def __init__(self):
        self.name = "Rectangle"

    def set_vertices(self, points):
        """Setter for vertices attribute of a Rectangle object.
        Requires a string formatted as "x y; x y;x y;x y"
        """
        points = [[int(j) for j in i] for i in points]
        points.sort(key=lambda x: x[0])
        self.vertices = points

    def get_vertices(self):
        """Getter for the vertices attribute"""
        return self.vertices

    def calc_sides(self):
        """Method for calculating the sides of a Rectangle"""
        calc_base = self.get_vertices()[0:2]
        calc_base.sort(key=lambda member: member[1])
        point_x, point_y = calc_base
        other = self.get_vertices()[2:4]
        other.sort(key=lambda member: member[1])
        point_z = other[0]
        lside = ((point_x[0] - point_y[0])**2
                 + (point_x[1] - point_y[1])**2)**0.5
        bottom = ((point_x[0] - point_z[0])**2
                  + (point_x[1] - point_z[1])**2)**0.5
        return lside, bottom

    def perimeter(self):
        """Method for calculating the perimeter of a Rectangle"""
        sides = self.calc_sides()
        return (sides[0] + sides[1])*2

    def area(self):
        """Method for calculating the area of a Rectangle"""
        sides = self.calc_sides()
        return sides[0] * sides[1]

    def __str__(self):
        retstr = f"A rectangle with points in\
{self.vertices}, color {self.color},\
perimeter {self.perimeter():.3f}, area {self.area():.3f}"
        return retstr


class Circle(Shape):
    """Class implementing a Circle Shape object"""

    radius = 0
    centre = [0, 0]

    def __init__(self, centre, radius=0 ):
        self.name = "Circle"
        self.radius = radius
        self.centre = deepcopy(centre)

    def set_radius(self, radius):
        """Setter for the radius attribute
        Requires a integer.
        """
        self.radius = int(radius)

    def set_centre(self, coord_x, coord_y):
        """Setter for the centre attribute.
        Requires an array: [x, y]
        """
        self.centre = [int(coord_x), int(coord_y)]

    def perimeter(self):
        """Method for calculating the perimeter of a Circle"""
        return 2 * PI * int(self.radius)

    def area(self):
        """Method for calculating the area of a Circle"""
        return PI * (int(self.radius)**2)

    def __str__(self) -> str:
        info = "A circle with a centre in {}\
, radius {}, color {}, perimeter {:.3f}, area {:.3f}"
        return info.format(self.centre, self.radius,\
                            self.color, self.perimeter(), self.area())

