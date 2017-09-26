"""
Python processing project to display a random, changing "10PRINT" style maze.
Inspired by Daniel Shiffman's video:
https://youtu.be/bEyTZ5ZZxZs
It randomly chooses slashes to change orientation, and each slash then
interpolates towards its desired position. It features quite a heavily OO model
for the maze and the slashes.
"""

from Slash import Slash

SLASH_LENGTH = 30.0
CHANGES_PER_SECOND = 10

def setup():
    size(1280, 720)
    stroke(255)
    for x in xrange(0, width, int(SLASH_LENGTH)):
        for y in xrange(0, height, int(SLASH_LENGTH)):
            # only need to initialise it, the class statically tracks instances
            # already
            Slash(x, y, SLASH_LENGTH)

def draw():
    saveFrame("data/10print-vid-######.png")
    background(0)
    for _ in xrange(CHANGES_PER_SECOND):
        Slash.flip_one()
    
    Slash.update()
    Slash.draw()