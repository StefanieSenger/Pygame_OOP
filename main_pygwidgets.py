import pygwidgets
import pygame
import sys

from settings import WINDOW_WIDTH, WINDOW_HEIGHT, FRAMES_PER_SECOND, BLACK

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

image_object = pygwidgets.Image(window, (100, 200), 'images/ball.png')
text_button =pygwidgets.TextButton(window, (50, 50), 'Text Button')

while True:
    for event in pygame.event.get():

        # if close button clicked: quit pygame and end the program
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # class method returns true if this is an event the oWidget needs to
        # respond to
        if image_object.handleEvent(event):
            pass

        # updating window
        window.fill(BLACK)
        image_object.draw()
        text_button.draw()
        pygame.display.update()

        clock.tick(FRAMES_PER_SECOND)
