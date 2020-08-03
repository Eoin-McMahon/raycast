from p5 import *
from wall import Wall
from ray import Ray
from source import Source

walls = []
source = Source()

def setup():
    width = 600
    height = 600
    size(width, height)  # Size should be the first statement

    for i in range(5):
        x1 = random_uniform(width, 0)
        x2 = random_uniform(width, 0)
        y1 = random_uniform(height, 0)
        y2 = random_uniform(height, 0)
        walls.append(Wall(x1, y1, x2, y2))

    # outer walls
    walls.append(Wall(0, 0, width, 0))
    walls.append(Wall(width, 0, width, height))
    walls.append(Wall(width, height, 0, height))
    walls.append(Wall(0, height, 0, 0))


def draw():
    background(0) # Set the background to black
    for wall in walls:
        wall.show()
    
    source.update(mouse_x, mouse_y)
    source.show()
    source.cast(walls)

if __name__ == '__main__':
    run()
