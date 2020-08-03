from p5 import *

class Ray():
    def __init__(self, x, y):
        self.pos = Vector(x, y)
        self.dir = Vector(1,0)

    def show(self):
        stroke(255);
        translate(self.pos.x, self.pos.y)
        line((0, 0), (self.dir.x * 10, self.dir.y * 10))

    def set_direction(self, x, y):
        self.dir.x = x - self.pos.x
        self.dir.y = y - self.pos.y
        self.dir.normalize()


    def cast(self, wall):
        # wall geometry
        x1 = wall.a.x
        x2 = wall.b.x
        y1 = wall.a.y
        y2 = wall.b.y

        # ray geometry
        x3 = self.pos.x
        y3 = self.pos.y
        x4 = self.pos.x + self.dir.x
        y4 = self.pos.y + self.dir.y

        # https://en.wikipedia.org/wiki/Line%E2%80%93line_intersection
        top_for_t = (x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)
        top_for_u = (x1 - x2) * (y1 - y3) - (y1 - y2) * (x1 - x3)
        bottom = (x1-x2) * (y3-y4) - (y1-y2) * (x3-x4)

        # ray and wall are parallel
        if bottom == 0:
            return

        t = top_for_t / bottom
        u = - (top_for_u / bottom)

        if t > 0 and t < 1 and u > 0:
            return True
        
        return



