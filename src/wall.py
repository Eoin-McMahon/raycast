from p5 import *

class Wall():
    def __init__(self, x1, y1, x2, y2):
        self.a = Vector(x1, y1, 0.0)
        self.b = Vector(x2, y2, 0.0)

    def show(self):
        push_style()
        stroke(255)
        stroke_weight(2);
        stroke_cap(ROUND);
        line((self.a.x, self.a.y), (self.b.x, self.b.y))
        pop_style()


