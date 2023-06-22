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
import statistics

class Game:

    def __init__(self, display: Display, input: Input):
        self.display = display
        self.input = input
        self.__board = Board.build_board()

    def get_board_copy(self) -> ndarray:
        return Board.get_copy(self.__board)

    def play_game(self):

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
        # for i in range(len(times)):
            # print("turn "+str(i+1)+" - "+str(times[i]))

    def report_statistics(self, num_games: int = 20):
        scores = []
        old_disp = self.display
        self.display = ProgressDisplay(num_games)
        print(f'--------------------------Playing Games--------------------------')
        for i in range(num_games):
            self.play_game()
            scores.append(Board.get_score(self.__board))
            self.__board = Board.build_board()
            self.display.current_game += 1
            self.display.turn = 0
        print(f'{scores}', end='                                                                   \n')
        print(f'Mean: {statistics.mean(scores)}\n')
        print(f'stdev: {statistics.stdev(scores)}\n')
        print(f'Max: {max(scores)}\n')
        print(f'Min: {min(scores)}\n')



