"""
The file that implements a Slash
"""

from random import choice

# Used in the interpolation to desired orientation
UPDATE_FACTOR = 0.2

# Two decorators that are used to perform the overhead in tracking slashes
def apply_to(l):
    """
    A decorator that applies a function to every item in a list
    """
    def to_all(func):
        def f(*args, **kwargs):
            for i in list(l):
                func(i, *args, **kwargs)
        return f
    return to_all

def apply_rand(l):
    """
    A decorator that picks a random element from a list and applies a function to it
    """
    def do_rand(func):
        def f(*args, **kwargs):
            func(choice(l), *args, **kwargs)
        return f
    return do_rand

class Slash(object):
    """
    The Slash object. It tracks its position and length, and the class itself
    tracks the instances and provides static methods to interact with them.
    """

    # Used to statically track instances
    slashes = []

    def __init__(self, x, y, length_):
        self.x = x
        self.y = y
        self.dir = 0
        # True or False depending on the two possible states
        self.target = False
        # multiply by sqrt(2) so that the caller only needs to provide a base
        # length
        self.length_ = length_ * sqrt(2)
        # make sure the instance is tracked
        self.slashes.append(self)
    
    # randomly flip a Slash instance
    @staticmethod
    @apply_rand(slashes)
    def flip_one(self):
        self.target = not self.target
    
    # update all Slash instances
    @staticmethod
    @apply_to(slashes)
    def update(self):
        if self.target:
            self.dir = lerp(self.dir, QUARTER_PI, UPDATE_FACTOR)
        else:
            self.dir = lerp(self.dir, HALF_PI + QUARTER_PI, UPDATE_FACTOR)
    
    # draw all Slash instances
    @staticmethod
    @apply_to(slashes)
    def draw(self):
        pushMatrix()
        translate(self.x, self.y)
        rotate(self.dir)
        line(-self.length_ / 2.0, 0, self.length_ / 2.0, 0)
        popMatrix()
