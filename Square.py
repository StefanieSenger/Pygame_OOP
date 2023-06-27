# Class for a random Square

import random
import pygame
from pygame.locals import *

from settings import WINDOW_WIDTH, WINDOW_HEIGHT
from Shape import Shape


class Square(Shape):

    def __init__(self, window):
        super().__init__(window)

    def draw(self):
        pygame.draw.rect(self.window, self.color, (self.square_x , self.square_y, self.size, self.size), 0)

    def __eq__(self, other):
        if type(other) is not Square:
            raise TypeError('Type must be of class Square.')
        if self.color == other.color:
            return True
        else:
            return False



# for testing
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
square1 = Square(window)
square2 = Square(window)
#print(dir(square1))

import inspect
source_code = inspect.getsource(square1.__eq__)
#print(source_code)

print(square1 == square2)

print(square1.__repr__)
print(str(square1))
print(square1)
