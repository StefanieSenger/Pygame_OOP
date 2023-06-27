import pygame
from pygame.locals import *
import sys

from Circle import Circle
from Square import Square
from Triangle import Triangle
from settings import WINDOW_WIDTH, WINDOW_HEIGHT, FRAMES_PER_SECOND, BLACK


# Initialize window and shape objects
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()
square_list = [Square(window) for i in range(3)]
circle_list = [Circle(window) for i in range(3)]
triangle_list = [Triangle(window) for i in range(3)]

while True:

    # Check for and handle events
    for event in pygame.event.get():
        # Clicked the close button? Quit pygame and end the program
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Clear the window before drawing it again
    window.fill(BLACK)

    # Draw shapes
    for square in square_list:
        square.draw()
    for circle in circle_list:
        circle.draw()
    for triangle in triangle_list:
        triangle.draw()

    # Update the window
    pygame.display.update()

    # Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)
