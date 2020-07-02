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
        #         A list that contains 3 lists, each of those lists has 3 '.' values.
        # TODO: Create a turn_counter set to 0 and a game_is_over set to False
        pass

    def take_turn(self, row, col):
        """Handle the current turn of the player and update board array"""
        # TODO: Check if game_is_over and return from this method (doing nothing) if True
        # TODO: Check if the value for row and col are valid.  Return (doing nothing) if invalid.
        # TODO: Check if the mark at the requested row col is '.'.  Return (doing nothing) if it is not '.'

        # TODO: Determine if it is X's turn or O's turn (even turn_counter means X's turn, odd for O's turn)
        # TODO: Modify the board by setting the current row col to an 'X' or an 'O' as appropriate
        # TODO: Update the display caption (top title) text as appropriate "O's Turn" or "X's Turn"

        # TODO: Increment the turn_counter
        # TODO: If the turn_counter is 9 then the game is over
        # TODO:        Update the game_is_over value and set the display caption to "Tie Game"

        self.check_for_game_over()

    def check_for_game_over(self):
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
        # TODO: If there is a winner, update the title text, play a sound, and set game_is_over to True.


# --------------------------- Update the view ---------------------------


def draw_board(screen, game):
    """ Draw the board based on the marked store in the board configuration array """
    # TODO 3: Loop over the game.board to place X and O images on the screen as appropriate.


# --------------------------- Controller ---------------------------


def main():
    pygame.init()
    pygame.mixer.music.load("win.mp3")
    screen = pygame.display.set_mode((380, 400))
    pygame.display.set_caption("X's Turn")
    board_surface = pygame.image.load("board.png")
    # TODO 1: Create an instance of the Game class

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            # TODO 6: When a MOUSEBUTTONUP event occurs take a game turn:
            # TODO 7:   Get the X and Y mouse position
            # TODO 8:   Use the get_row_col function to convert the XY mouse position into a row and column.
            # TODO 9:   Call the take_turn method with the row and column values
            # TODO 10: When the pygame.K_SPACE key is pressed create a new game instance and update the text.

        screen.fill(pygame.Color("white"))
        screen.blit(board_surface, get_xy_position(0, 0))

        # TODO 2: Call draw_board
        # TODO 4: As a temporary test hardcode a few 'X' or 'O' values in game.board
        # TODO 5: Remove your temporary hardcoded tests

        pygame.display.update()


main()
