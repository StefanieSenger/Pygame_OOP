# Class for a SimpleTextn

import pygame
from pygame.locals import *


class SimpleText():

    def __init__(self, window, text, pos):
        # user can chose position as a tuple

        self.text = text
        self.pos = pos
        self.window = window

        pygame.font.init()
        myfont = pygame.font.SysFont('Comic Sans MS', 30)
        self.text_surface = myfont.render (self.text, True, (255, 0, 0))


    def change_text(self, new_text):
        self.text = new_text
        myfont = pygame.font.SysFont('Comic Sans MS', 30)
        self.text_surface = myfont.render (self.text, True, (255, 0, 0))

        #return self


    def draw(self):
        # returns text in given window position

        return self.window.blit(self.text_surface, self.pos)
