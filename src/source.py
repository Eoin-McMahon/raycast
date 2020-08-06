from p5 import *
from ray import Ray
from wall import Wall

class Source:
    def __init__(self, pos, num_rays):
        self.pos = pos
        self.rays = []
        ray_step = 360//num_rays

        for i in range(0,360, ray_step):
            ray = Ray(self.pos, radians(i))
            self.rays.append(ray)

    def cast(self, walls):
        for i, ray in enumerate(self.rays):
            closest = None
            record = 1000000
            for wall in walls:
                pt, d = ray.cast(wall)                
                if pt != None:
                    if d < record:
                        record = d
                        closest = pt
            if closest != None:
                push_style()
                stroke(255, 200)
                line((self.pos.x, self.pos.y), (closest.x, closest.y))
                pop_style()

    def update(self, new_pos):
        self.pos = new_pos
