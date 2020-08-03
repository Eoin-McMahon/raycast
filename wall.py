from p5 import *

class Wall():
    def __init__(self, x1, y1, x2, y2):
        self.a = Vector(x1, y1)
        self.b = Vector(x2, y2)

    def show(self):
        stroke(255)
        line((self.a.x, self.a.y), (self.b.x, self.b.y))


