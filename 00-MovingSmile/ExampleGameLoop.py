import pygame
import sys

pygame.init()
pygame.display.set_caption("Hello World")
screen = pygame.display.set_mode((640, 480))

while True:
    for event in pygame.event.get():
        print(event)  # Used for an example here
        if event.type == pygame.QUIT:
            sys.exit()
        # Additional interactions

    # Draw things on the screen

    pygame.display.update()
