import pygame
import random
from settings import WINDOW_WIDTH, WINDOW_HEIGHT, BALL_WIDTH_HEIGHT

class Ball():
    def __init__(self, window):
        self.MAX_WIDTH = WINDOW_WIDTH - BALL_WIDTH_HEIGHT
        self.MAX_HEIGHT = WINDOW_HEIGHT - BALL_WIDTH_HEIGHT

        self.window = window
        self.image = pygame.image.load('images/ball.png')
        self.ballX = random.randrange(self.MAX_WIDTH)
        self.ballY = random.randrange(self.MAX_HEIGHT)
        self.xSpeed = random.randint(1,5)
        self.ySpeed = random.randint(1,5)

    def update(self):
        # updates position of ball

        if (self.ballX < 0) or (self.ballX >= self.MAX_WIDTH):
            self.xSpeed = -self.xSpeed

        if (self.ballY < 0) or (self.ballY >= self.MAX_HEIGHT):
            self.ySpeed = -self.ySpeed

        self.ballX = self.ballX + self.xSpeed
        self.ballY = self.ballY + self.ySpeed

        return self

    def draw(self):
        # returns everything needed to draw a ball object in a window

        #return self.image, (self.ballX, self.ballY)
        return self.window.blit(self.image, (self.ballX, self.ballY))
