from p5 import *
from wall import Wall

w = Wall(300, 100,300,300)
def setup():
    size(640, 360)  # Size should be the first statement
    w = Wall(300, 100,300,300)
    

def draw():
    background(0) # Set the background to black
    w.show()

if __name__ == '__main__':
    run()
