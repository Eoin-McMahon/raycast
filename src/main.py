from p5 import *
from wall import Wall
from ray import Ray
from source import Source
from absl import flags, app
from util import remap_number_range

FLAGS = flags.FLAGS
flags.DEFINE_boolean('auto', False, 'Moves the source particle automatically')
flags.DEFINE_integer('rays', 45, 'Moves the source particle automatically', lower_bound=0)

walls = []

x_off = 0
y_off = 10000

auto_move = False

def main(argv):
    run()

def setup():
    size(600,600)

    # Set up some inner walls
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
    global auto_move
    auto_move = FLAGS.auto

    # If cursor is outside of window boundary
    outside_boundary = (mouse_x >= width or mouse_x <= 0)\
                    or (mouse_y >= height or mouse_y <= 0)

    # if mouse outside window, move automatically
    if outside_boundary:
        auto_move = True
    
    # determine new position of source
    noise_pos = Vector(noise(x_off) * width, noise(y_off) * height)
    mouse_pos = Vector(mouse_x, mouse_y)
    source_pos = noise_pos if (auto_move==True) else mouse_pos

    # create source
    source = Source(source_pos, FLAGS.rays)
    
    # dynamically elect background colour
    color_mode("HSB")
    x_colour = remap_number_range(source_pos.x, 0, width, 0, 255);
    y_colour = remap_number_range(source_pos.y, 0, width, 0, 255);
    background(int(x_colour + y_colour / 4), 180, 200)  # Set the background to black
    
    for wall in walls:
        wall.show()    
    
    source.update(source_pos)
    source.cast(walls)

    x_off += 0.01
    y_off += 0.01


if __name__ == '__main__':
    app.run(main)
