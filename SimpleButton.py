import pygame
from pygame.locals import *
from settings import WINDOW_WIDTH, WINDOW_HEIGHT

class SimpleButton():

    def __init__(self):
        self.image = pygame.image.load('images/buttonUp.png')
        self.button_rect = self.image.get_rect()

        self.button_rect.centerx = WINDOW_WIDTH//2
        self.button_rect.centery = WINDOW_HEIGHT//2

        self.onmouseover_shown = False


    def handle_events(self, event):
        # change the image for the button upon pressing and releasing

        if event == pygame.MOUSEMOTION:
            self.onmouseover_shown = True
            print('Cursor moved over button.')

        if event == pygame.MOUSEBUTTONDOWN:
            self.image = pygame.image.load('images/buttonDown.png')
            print('Button pressed down.')

        if event == pygame.MOUSEBUTTONUP:
            self.image = pygame.image.load('images/buttonUp.png')
            print('Button released.')


    def draw(self, window):
        # returns everything needed to draw a button object in a window

        # shows onmouseover action for the duration of 30 frames
        if self.onmouseover_shown:
            i = 0
            while i < 31:
                font = pygame.freetype.SysFont(None, 24)
                click_text = "Click!"
                font.render_to(window, (self.button_rect.centerx + 30, self.button_rect.centery - 40), click_text, (255, 255, 255))
                i += 1
        return self.image, self.button_rect
