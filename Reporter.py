import pickle
import multiprocessing
import statistics
import time
from abc import ABC
from typing import List

from datetime import datetime
from Encoder import Encoder, PickleEncoder
from AI import *
from Game import Game
from Input import Input, TextInput
from Display import NoneDisplay


class Reporter(ABC):

    @abstractmethod
    def __init__(self, AI_: AI):
        pass

    @abstractmethod
    def generate_report(self, num_games: int):
        pass


class FileReporter(Reporter):
    # Plays n games and saves gameinfo objects as a binary file for efficient storage

    def __init__(self, AI_: AI, encoder: Encoder, filename: str = None):
        self.AI_ = AI_
        self.display = NoneDisplay()
        self.encoder = encoder
        if filename is None:
            self.filename = str(datetime.now()) + ".txt"
        else:
            self.filename = filename

    def generate_report(self, num_games: int = 5):
        t = time.perf_counter()
        print(f"Saving to {self.filename}")
        for i in range(num_games):
            g = Game(display=self.display, input=self.AI_ )
            info = g.play_game()
            self.encoder.encode(gameinfo=info, filename=self.filename)
            print(f"Game number {i+1} completed", end='\r')
        t = time.perf_counter() - t
        print(f"All games completed in {t} seconds")




