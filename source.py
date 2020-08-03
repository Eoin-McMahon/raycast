from p5 import *
from ray import Ray
from wall import Wall

class Source:
    def __init__(self):
        self.pos = Vector(width / 2, height / 2)
        self.rays = []
        for i in range(360):
            ray = Ray(self.pos, radians(i))
            self.rays.append(ray)

    def show(self):
        fill(255)
        circle((self.pos.x, self.pos.y), 8)
        for ray in self.rays:
            ray.show()

    def cast(self, walls):
        for ray in self.rays:
            closest = None
            maximum = 100000000
            for wall in walls:
                pt = ray.cast(wall)
                if (pt):
                    d = Vector.dist(self.pos, pt)
                    if d < maximum:
                        record = d
                        closest = pt

            if closest:
                stroke(255, 100)
                line((self.pos.x, self.pos.y), (closest.x, closest.y))

    def update(self, x, y):
        self.pos = Vector(x,y)
