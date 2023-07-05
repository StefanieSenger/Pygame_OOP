# Main file for playing the Balloon Game

import pygame
from pygame.locals import *
import random
import sys

from SimpleButton import SimpleButton
from SimpleText import SimpleText
from Balloon import Balloon
from settings import WINDOW_WIDTH, WINDOW_HEIGHT, FRAMES_PER_SECOND, BLACK, N_BALLOONS, BALLOON_SIZES

# Initialize window, button object, text object and ball objects
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

simpleButton = SimpleButton(window = window, pos = (WINDOW_WIDTH//2, 7*(WINDOW_HEIGHT//8)))
simpleTextHeader = SimpleText(window = window, text = "", pos = (WINDOW_WIDTH//6, WINDOW_HEIGHT//8))
balloon_list = [Balloon(window, random.choice(BALLOON_SIZES)) for i in range(N_BALLOONS)]

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
        for balloon in balloon_list[:]: # loop over copy, so I can modify the list
                balloon.handle_events(event)
                # delete balloon from list if it was staged to be deleted (because it was hit before)
                if balloon.to_be_deleted:
                    balloon_list.remove(balloon)

    # when button object is released, start or stop balloon action
    if simpleButton.ball_action_started:
        for balloon in balloon_list:
            balloon.update()
            balloon.showing = True

    # change text for every ballon popped
    simpleTextHeader.change_text(f"Hurray! Only {Balloon.balloons_remaining} Balloons remaining!")

    # draw updated window
    window.fill(BLACK)
    simpleButton.draw()
    if simpleButton.ball_action_started:
        for balloon in balloon_list:
            balloon.draw()
    simpleTextHeader.draw()
    pygame.display.update()

    # Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)  # make pygame wait
