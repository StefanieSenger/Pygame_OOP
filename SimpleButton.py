# Class for a SimpleButton

import pygame
from pygame.locals import *


class SimpleButton():

    def __init__(self, window, pos):
        # user can chose position as a tuple, button image is a default

        self.window = window
        self.image = pygame.image.load('images/buttonUp.png')
        self.button_rect = self.image.get_rect()

        pos_centerx, pos_centery = pos
        self.button_rect.centerx = pos_centerx
        self.button_rect.centery = pos_centery

        self.onmouseover_shown = False
        self.ball_action_started = False


    def handle_events(self, event):
        # change the image for the button upon pressing and releasing

        # Onto moving the cursor
        if event.type == pygame.MOUSEMOTION:
            if self.button_rect.collidepoint(event.pos):
                self.onmouseover_shown = True
                print('Cursor moving over button.')
            else:
                self.onmouseover_shown = False
                print('Cursor not moving over the button.')

        # Onto pressing down on the button
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.button_rect.collidepoint(event.pos):
                self.image = pygame.image.load('images/buttonDown.png')
                print('Button pressed down.')

        # Onto releasing the button
        if event.type == pygame.MOUSEBUTTONUP:
            if self.button_rect.collidepoint(event.pos):
                self.image = pygame.image.load('images/buttonUp.png')
                print('Button released.')

                # every time the button is released we start or stop the ball
                # action
                if not self.ball_action_started:
                    self.ball_action_started = True
                else:
                    self.ball_action_started = False
                # print(self.ball_action_started)


    def draw(self):
        # returns window object with simpleButton object and "click_text" drawn
        # into it

        # shows onmouseover action if cursor is over button
        if self.onmouseover_shown:
           font = pygame.freetype.SysFont(None, 24)
           click_text = "Click!"
           font.render_to(self.window, (self.button_rect.centerx + 30, self.button_rect.centery - 40), click_text, (255, 255, 255))

        return self.window.blit(self.image, self.button_rect)
