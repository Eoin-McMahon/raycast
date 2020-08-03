from p5 import *
from wall import Wall
from ray import Ray

wall = Wall(300, 100,300,300)
ray = Ray(100,200)

def setup():
    size(640, 360)  # Size should be the first statement
    

def draw():
    background(0) # Set the background to black
    wall.show()
    ray.show()
    ray.set_direction(mouse_x, mouse_y)

if __name__ == '__main__':
    run()
