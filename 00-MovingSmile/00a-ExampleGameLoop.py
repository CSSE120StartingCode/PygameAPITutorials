import pygame
import sys

# Initialize the game, caption and screen:
pygame.init()
pygame.display.set_caption("Hello World")
screen = pygame.display.set_mode((640, 480))

# The game loop:
while True:
    screen.fill((255, 255, 255))  # white (RGB: red, green, blue. Each 0 to 255.)

    # Check for events (and respond to them as desired):
    for event in pygame.event.get():
        print(event)  # Used for an example here
        if event.type == pygame.QUIT:
            sys.exit()
        # Additional interactions

    # Draw things on the screen (nothing in this example):

    # Update the screen each time through the game loop:
    pygame.display.update()
