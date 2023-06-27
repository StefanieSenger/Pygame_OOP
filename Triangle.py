# Class for a random Triangle

import pygame
from pygame.locals import *

from Shape import Shape


class Triangle(Shape):

    def __init__(self, window):
        super().__init__(window)

    def draw(self):
        pygame.draw.polygon(self.window, self.color, ((self.square_x, self.square_y),
                                                      (self.square_x + self.size, self.square_y ),
                                                      (self.square_x, self.square_y + self.size))
        )
