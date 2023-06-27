# Abstract Shape class for shapes like Square, Triangle and Circle

from abc import ABC, abstractmethod
import random
from pygame.locals import *
import pygame

from settings import WINDOW_WIDTH, WINDOW_HEIGHT

class Shape(ABC):

    def __init__(self, window):
        self.window = window
        self.color = random.choice([(0,0,255), (0,255,0), (255,0,0)])
        self.size = random.randint(20,100)
        self.MAX_WIDTH = WINDOW_WIDTH - self.size
        self.MAX_HEIGHT = WINDOW_HEIGHT - self.size
        self.square_x = random.randrange(self.MAX_WIDTH)
        self.square_y = random.randrange(self.MAX_HEIGHT)
        self.type = self.__class__.__name__

    def get_type(self):
        return self.type

    @abstractmethod
    def draw(self):
        raise NotImplementedError

# for testing
'''pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
square1 = Shape(window) # should not be instantializable'''
