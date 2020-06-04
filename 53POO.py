#!/usr/bin/env python
# coding=utf-8
class Line(object):
    def __init__(self,coord1,coord2):
        self.coord1 = coord1
        self.coord2 = coord2
    def distance(self):
        x1,y1 = self.coord1
        x2,y2 = self.coord2
        return ((x2-x1)**2 + (y2-y1)**2 )**0.5
    def slope(self):
        x1,y1 = self.coord1
        x2,y2 = self.coord2
        return float((y2-y1))/(x2-x1)


#----------------------

class Cylinder(object):
    def __init__(self,height=1,radius=1):
        self.height = height
        self.radius = radius
    def volume(self):
        return self.height * (3.14) * (self.radius)**2
    def surface_area(self):
        top = (3.14) * (self.radius)**2
        return 2 * top + 2 * 3.14 * self.radius * self.height

#----------------------Problema 1

coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1,coordinate2)
print("distance %.3f" % li.distance())
print("slope %.3f" % li.slope())

#----------------------Problema 2
c = Cylinder(2,3)
print("volume %.3f" % c.volume())
print("surface_area %.3f" % c.surface_area())