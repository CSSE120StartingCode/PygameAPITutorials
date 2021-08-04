import pygame
import sys


def main():
    # pre-define RGB colors for Pygame
    BLACK = pygame.Color("Black")
    WHITE = pygame.Color("White")
    IMAGE_SIZE = 470
    TEXT_HEIGHT = 30

    # initialize the pygame module
    pygame.init()

    # prepare the window (screen)
    screen = pygame.display.set_mode((IMAGE_SIZE, IMAGE_SIZE + TEXT_HEIGHT))
    pygame.display.set_caption("Text, Sound, and an Image")

    # Load the image that will be used in the game loop below.
    # TODO 1: Create an image with the 2dogs.JPG image

    # Load a font to use in the game loop below.
    # TODO 4: Create a font object with a size 28 font.
    #    Also, as you do _TODO_ 5, 6 and 7 (follow-ups to this _TODO_ 4),
    #    play around with your own fonts by uncommenting the commented-out
    #    lines below to print the names of the fonts on your own computer
    #    and using a line like the last one to use one of them (but use a name
    #    that gets printed, since "comicsansms" may not be on your computer).
    # fonts_on_my_computer = pygame.font.get_fonts()
    # for font_name in fonts_on_my_computer:
    #     print(font_name)
    # font1 = pygame.font.SysFont("comicsansms", 28)

    # Load the music to play in the game loop below.
    # TODO 8: Create a Sound object from the "bark.wav" file.
    # TODO 10: Try using the pygame.mixer.music API instead.
    # TODO 11: Try playing the music forever while the mouse is held down then stopped on Mouse up

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            # TODO 9: Play the music (bark) if there's a mouse click.

        # Clear the screen and set the screen background
        screen.fill(WHITE)

        # Draw the image onto the screen
        # TODO 3: Scale the image to be the size (IMAGE_SIZE, IMAGE_SIZE)
        # TODO 2: Draw (blit) the image onto the screen at position (0, 0)

        # Draw the text onto the screen
        # TODO 5: Render the text "Two Dogs" using the font object (it's like MAKING an image).
        # TODO 6: Draw (blit) the text image onto the screen in the middle bottom.
        # Hint: Commands like these might be useful..
        #          screen.get_width(), caption1.get_width(), image1.get_height()

        # TODO 7: On your own, create a new bigger font and in white text place a 'funny' message on top of the image.

        # Update the screen
        pygame.display.update()


main()
