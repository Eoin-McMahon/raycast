from p5 import *
from wall import Wall
from ray import Ray
from source import Source
from absl import flags

FLAGS = flags.FLAGS

flags.DEFINE_boolean('auto', False, 'Moves the source particle automatically')

walls = []
auto_move = FLAGS.auto

x_off = 0
y_off = 10000

def setup():
    width = 500
    height = 500
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
    global x_off
    global y_off

    noise_pos = Vector(noise(x_off) * width, noise(y_off) * height)
    mouse_pos = Vector(mouse_x, mouse_y)

    source_pos = noise_pos if (auto_move==True) else mouse_pos

    source = Source(source_pos)
    background(0) # Set the background to black

    for wall in walls:
        wall.show()    
    
    # source.update(mouse_x, mouse_y)
    source.update(source_pos)
    source.show()
    source.cast(walls)

    x_off += 0.01
    y_off += 0.01


if __name__ == '__main__':
    run()
