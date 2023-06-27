# Class for a random Circle

import pygame
from pygame.locals import *

from Shape import Shape

class Circle(Shape):

    def __init__(self, window):
        super().__init__(window)

    def draw(self):
        pygame.draw.circle(self.window, self.color, (self.square_x , self.square_y), self.size, 0)
