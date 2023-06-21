# refactoring procedural approach for ballbouncing screensafer from template_06
# into OOP code

# 1 - Import packages
import pygame
from pygame.locals import *
import sys

from Ball import Ball
from settings import WINDOW_WIDTH, WINDOW_HEIGHT, FRAMES_PER_SECOND, BLACK

# Initialize window and ball object
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()
ball = Ball()

# Loop FRAMES_PER_SECOND times (per second)
while True:

    # Check for and handle events
    for event in pygame.event.get():
        # Clicked the close button? Quit pygame and end the program
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # update ball position
    ball.update()

    # Clear the window before drawing it again
    window.fill(BLACK)

    # Draw the window elements
    window.blit(*ball.draw())

    # Update the window
    pygame.display.update()

    # Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)  # make pygame wait
