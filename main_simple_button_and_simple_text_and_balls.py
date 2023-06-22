# Main file for displaying the SimpleButton in a new window

import pygame
from pygame.locals import *
import sys

from SimpleButton import SimpleButton
from SimpleText import SimpleText
from Ball import Ball
from settings import WINDOW_WIDTH, WINDOW_HEIGHT, FRAMES_PER_SECOND, BLACK

# Initialize window, button object, text object and ball objects
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

simpleButton = SimpleButton(window = window, pos = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2))

simpleTextHeader = SimpleText(window = window, text = "This isn't a header", pos = (WINDOW_WIDTH//4, WINDOW_HEIGHT//8))
simpleTextFooter = SimpleText(window = window, text = "This isn't a footer", pos = (WINDOW_WIDTH//4, WINDOW_HEIGHT//8*7))

ball_list = [Ball(window) for i in range(10)]

counter = 0

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


    # when button object is released, start or stop ball action
    # (Ball().ball_action_started)
    if simpleButton.ball_action_started:
        for ball in ball_list:
            ball.update()

    # change text for every loop (so that it is a counter)
    simpleTextHeader.change_text(f"{counter} many loops completed")

    # draw new window with (possibly) updated button
    window.fill(BLACK)
    simpleButton.draw()
    if simpleButton.ball_action_started:
        for ball in ball_list:
            ball.draw()
    simpleTextHeader.draw()
    simpleTextFooter.draw()
    pygame.display.update()

    # update counter
    counter += 1

    # Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)  # make pygame wait
