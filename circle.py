class Circle:
    def __init__(self, diameter):
        self.diameter = diameter

    @property # returns value as attribute "getter"
    def radius(self):
        return self.diameter / 2


    @radius.setter # allows to set attribute from outside "setter"
    def radius(self, radius):
        self.diameter = radius * 2




small = Circle(10)
print(small.diameter)
print(small.radius)
small.radius = 10
print(small.diameter)
print(small.radius)
