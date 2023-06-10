# Game controls elements like displaying the board and when game ends
# there should only be one game object made at a time, and AIs can test by duplicating
# boards
# AIs can only interface with up,down,left,right movements, this will prevent possible
# cheating

from Board import Board
from Display import *
from Input import *
import time


class Game:

    def __init__(self, display: Display, input: Input):
        self.display = display
        self.input = input
        self.__board = Board()

    def get_board_copy(self) -> Board:
        return self.__board.get_copy()

    def play_game(self):

        self.display.displayBoard(self.__board)
        gameover = False

        while not gameover:
            user_input = self.input.getInput(self.get_board_copy())

            t = time.time()
            if self.__board.move(user_input):
                self.__board.add_random_square()
            print(time.time()-t)
            self.display.displayBoard(self.__board)
            if not self.__board.get_legal_moves():
                gameover = True





