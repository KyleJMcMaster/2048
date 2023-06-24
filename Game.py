# Game controls elements like displaying the board and when game ends
# there should only be one game object made at a time, and AIs can test by duplicating
# boards
# AIs can only interface with up,down,left,right movements, this will prevent possible
# cheating

import Board
from Display import *
from Input import *
from numpy import ndarray
import time


class Game:

    def __init__(self, display: Display, input: Input):
        self.display = display
        self.input = input
        self.__board = Board.build_board()

    def get_board_copy(self) -> ndarray:
        return Board.get_copy(self.__board)

    def play_game(self) -> int:

        self.display.displayBoard(self.__board)
        turn = 0
        times = []
        gameover = False

        while not gameover:
            turn += 1
            t = time.time()
            user_input = self.input.getInput(Board.get_copy(self.__board))
            t = time.time() - t
            times.append(t)
            # print(t)
            if Board.check_legal_move(self.__board, user_input):
                self.__board = Board.move(self.__board, user_input)
                self.__board = Board.add_random_square(self.__board)

            self.display.displayBoard(self.__board)
            if not Board.get_legal_moves(self.__board):
                gameover = True

        self.display.displayBoard(self.__board)
        return Board.get_score(self.__board)





