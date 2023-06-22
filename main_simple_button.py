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
simpleButton = SimpleButton()

# Loop FRAMES_PER_SECOND times (per second)
while True:

    # Check for and handle events
    for event in pygame.event.get():
        # Clicked the close button? Quit pygame and end the program
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Onto holding the cursor over the button
        if event.type == pygame.MOUSEMOTION:
            if simpleButton.button_rect.collidepoint(event.pos):
                simpleButton.handle_events(event.type)

        if event.type == pygame.MOUSEMOTION:
            if not simpleButton.button_rect.collidepoint(event.pos):
                simpleButton.handle_events(event.type)

        # Onto pressing down on the button
        if event.type == pygame.MOUSEBUTTONDOWN:
            if simpleButton.button_rect.collidepoint(event.pos):
                simpleButton.handle_events(event.type)

        # Onto releasing the button
        if event.type == pygame.MOUSEBUTTONUP:
            if simpleButton.button_rect.collidepoint(event.pos):
                simpleButton.handle_events(event.type)

    # draw new window with (possibly) updated button
    window.fill(BLACK)
    window.blit(*simpleButton.draw(window))
    pygame.display.update()

    # Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)  # make pygame wait
