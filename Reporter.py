import multiprocessing
from abc import ABC, abstractmethod
from Game import *
import statistics
import time
from Input import *
from typing import List

class Reporter(ABC):

    @abstractmethod
    def __init__(self, input: Input, num_games: int = 20, multithreaded: bool = False):
        pass

    @abstractmethod
    def report_statistics(self):
        pass


class TextReporter(Reporter):

    def __init__(self, input: Input, num_games: int = 20, multithreaded: bool = False):
        self.input = input
        self.num_games = num_games
        self.multithreaded = multithreaded

    def report_statistics(self):
        scores = []
        display = ProgressDisplay(self.num_games)
        t = time.time()
        print(f'--------------------------Playing Games--------------------------')
        if self.multithreaded:
            with multiprocessing.Pool(min(self.num_games, 100)) as pool:
                args = [(display, self.input, i, scores) for i in range(self.num_games)]
                for result in pool.starmap(TextReporter.play_concurrent_game, args):
                    scores.append(result)

        else:
            for i in range(self.num_games):
                g = Game(display, self.input)
                scores.append(g.play_game())
                display.current_game += 1
                display.turn = 0
        t = time.time() - t
        print(f'{t} seconds')
        print(f'{scores}', end='                                                                   \n')
        print(f'Mean: {statistics.mean(scores)}\n')
        print(f'stdev: {statistics.stdev(scores)}\n')
        print(f'Max: {max(scores)}\n')
        print(f'Min: {min(scores)}\n')
    @staticmethod
    def play_concurrent_game(display:Display, input: Input, game_num:int, scores: List[int]):
        g = Game(display, input)
        return g.play_game()


