# Main file for displaying the SimpleButton in a new window

import pygame
from pygame.locals import *
import sys

from SimpleButton import SimpleButton
from settings import WINDOW_WIDTH, WINDOW_HEIGHT, FRAMES_PER_SECOND, BLACK

# Initialize window and button object
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()
simpleButton = SimpleButton(window = window, pos = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2))

# Loop FRAMES_PER_SECOND times (per second)
while True:

    # Check for and handle events
    for event in pygame.event.get():

        # if close button clicked: quit pygame and end the program
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # all the other events are handled by the class method
        simpleButton.handle_events(event)


    # draw new window with (possibly) updated button
    window.fill(BLACK)
    simpleButton.draw()
    pygame.display.update()

    # Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)  # make pygame wait
