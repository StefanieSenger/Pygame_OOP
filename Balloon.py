import pygame
import random
from settings import WINDOW_WIDTH, WINDOW_HEIGHT, BALL_WIDTH_HEIGHT, N_BALLOONS

from SimpleButton import SimpleButton

class Balloon():
    balloons_remaining = N_BALLOONS

    def __init__(self, window, size):
        self.MAX_WIDTH = WINDOW_WIDTH - BALL_WIDTH_HEIGHT
        self.MAX_HEIGHT = WINDOW_HEIGHT - BALL_WIDTH_HEIGHT

        self.window = window

        if size == 'large':
            self.image = pygame.image.load('images/redBalloonLarge.png')
        elif size == 'medium':
            self.image = pygame.image.load('images/redBalloonMedium.png')
        elif size == 'small':
            self.image = pygame.image.load('images/redBalloonSmall.png')

        self.balloon_rect = self.image.get_rect()
        self.balloonX = random.randrange(self.MAX_WIDTH)
        self.balloonY = random.randrange(self.MAX_HEIGHT)
        self.xSpeed = random.randint(1,2)
        self.ySpeed = random.randint(1,2)

        self.showing = False
        self.to_be_deleted = False


    def update(self ):
        # updates position of ball

        if (self.balloonX < 0) or (self.balloonX >= self.MAX_WIDTH):
            self.xSpeed = -self.xSpeed

        if (self.balloonY < 0) or (self.balloonY >= self.MAX_HEIGHT):
            self.ySpeed = -self.ySpeed

        self.balloonX= self.balloonX + self.xSpeed
        self.balloonY = self.balloonY + self.ySpeed

        return self

    def handle_events(self, event):
        # delete object upon pressing and releasing

        pop_sound = pygame.mixer.Sound('sounds/balloonPop.wav')

        # only handle events if the balloon object is already showing
        if self.showing:
            # get current position of object
            current_pos = pygame.Rect(self.balloonX, self.balloonY, self.MAX_WIDTH, self.MAX_HEIGHT)

            # Onto moving the cursor
            if event.type == pygame.MOUSEMOTION:
                #current_pos = pygame.Rect(self.balloonX, self.balloonY, self.MAX_WIDTH, self.MAX_HEIGHT)
                if current_pos.collidepoint(event.pos):
                    print('Cursor moving over Balloon.')
                else:
                    print('Cursor not moving over Balloon.')

            # Onto releasing click
            if event.type == pygame.MOUSEBUTTONUP:
                if current_pos.collidepoint(event.pos):
                    pop_sound.play()
                    if not Balloon.balloons_remaining < 1:
                        Balloon.balloons_remaining -= 1
                    # delete object
                    self.to_be_deleted = True
                    self.__del__()

    def __del__(self):
        print('Balloon object deleted.')

    def draw(self):
        # returns everything needed to draw a ball object in a window

        return self.window.blit(self.image, (self.balloonX, self.balloonY))
