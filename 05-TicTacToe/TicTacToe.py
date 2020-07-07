import pygame
import sys


# --------------------------- Conversion helper functions ---------------------------


def get_row_col(mouse_x, mouse_y):
    """ Converts an x, y screen position into a row, col value. """
    # Note: the top row is row=0 (bottom row=2), left col is col=0 (right col=2)
    spacing_x = 86 + 8
    spacing_y = 98 + 5
    top_y = 50
    left_x = 50
    return (mouse_y - top_y) // spacing_y, (mouse_x - left_x) // spacing_x


def get_xy_position(row, col):
    """ Converts a row, col value into an x, y screen position (upper left corner of that location). """
    spacing_x = 86 + 11
    spacing_y = 98 + 8
    top_y = 50
    left_x = 50
    return left_x + col * spacing_x, top_y + row * spacing_y


# --------------------------- Model Object ---------------------------


class Game:
    def __init__(self):
        # TODO: Create an empty board, called board
        #         A list that contains 3 lists, each of those lists has 3 "." values.
        # TODO: Create a game_state_string set to X's turn
        # TODO: Create a turn_counter variable set to 0
        # TODO: Create a game_is_over variable set to False
        pass

    def take_turn(self, row, col):
        """Handle the current turn of the player and update board array"""
        # TODO: Check if game_is_over and return from this method (doing nothing) if True
        # TODO: Check if the value for row and col are valid.  Return (doing nothing) if invalid.
        # TODO: Check if the mark at the requested row col is ".".  Return (doing nothing) if it is not "."

        # TODO: Determine if it is X's turn or O's turn (even turn_counter means X's turn, odd for O's turn)
        # TODO: Modify the board by setting the current row col to an "X" or an "O" as appropriate
        # TODO: Update the game_state_string as appropriate "O's Turn" or "X's Turn"

        # TODO: Increment the turn_counter

        self.check_for_game_over()

    def check_for_game_over(self):
        # TODO: If the turn_counter is 9 then the game is over
        # TODO:    If >=9 update the game_is_over value and set the game_state_string to "Tie Game"
        lines = []
        lines.append(self.board[0][0] + self.board[0][1] + self.board[0][2])
        lines.append(self.board[1][0] + self.board[1][1] + self.board[1][2])
        lines.append(self.board[2][0] + self.board[2][1] + self.board[2][2])
        lines.append(self.board[0][0] + self.board[1][0] + self.board[2][0])
        lines.append(self.board[0][1] + self.board[1][1] + self.board[2][1])
        lines.append(self.board[0][2] + self.board[1][2] + self.board[2][2])
        lines.append(self.board[0][0] + self.board[1][1] + self.board[2][2])
        lines.append(self.board[0][2] + self.board[1][1] + self.board[2][0])

        # TODO: Use the lines list to determine if there is a winner.
        # TODO: If there is a winner, update the game_state_string, play a sound, and set game_is_over to True.


# --------------------------- View Controller ---------------------------

class ViewController(object):

    def __init__(self, screen):
        """ Creates the view controller (the Tic-Tac-Toe game you see) """
        # TODO: Initialize the ViewController, as follows:
        # TODO    - Store the screen.
        # TODO    - Create the game model object.
        # TODO    - Create images for the board, X, and O images filenames.
        # TODO  Use instance variables:   screen game board_image x_image o_image
        pass

    def check_event(self, event):
        """ Takes actions as necessary based on the current event. """
        # TODO: If the event is pygame.MOUSEBUTTONUP
        #     Get the mouse click position as x and y variables
        #     Convert the x and y variables into row and col using get_row_col
        #     Inform the model object about this event
        # TODO: If the event is pygame.KEYDOWN
        #     Get the pressed_keys
        #     If the key is pygame.K_SPACE, then reset the game.
        pass

    def draw(self):
        """ Draw the board based on the marked store in the board configuration array """
        # TODO: Blit the board_image onto the screen at the x y position of row=0 col=0
        # TODO: Use a nested loop (via range) to go over all marks of the game.board
        #    If the mark is "X", blit an X image at the x y position of row col
        #    If the mark is "O", blit an O image at the x y position of row col
        # TODO: Update the display caption to be the game.game_state_string
        pass

# --------------------------- Controller ---------------------------


def main():
    pygame.init()
    pygame.mixer.music.load("win.mp3")
    screen = pygame.display.set_mode((380, 400))
    # TODO 1: Create an instance of the ViewController class called view_controller

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            # TODO : Pass the event to the view_controller

        screen.fill(pygame.Color("white"))
        # TODO: Draw the view_controller
        pygame.display.update()


main()
