# Input is an abstract class which provides inputs to the game
from abc import ABC, abstractmethod
from Board import Board
from numpy import ndarray
import random


class Input(ABC):

    @abstractmethod
    def getInput(self, board: ndarray) -> int:
        pass



class TextInput(Input):

    def getInput(self, board: ndarray) -> int:
        valid_inputs = {
            'd': 0,
            'a': 1,
            'w': 2,
            's': 3,
            'exit': -1
        }
        user_input = ''
        while user_input not in valid_inputs:
            user_input = input('--> ')

        if user_input == 'exit':
            exit(valid_inputs['exit'])

        return valid_inputs[user_input]


class RandomAI(Input):

    def getInput(self, board: ndarray) -> int:
        return random.randint(0, 3)



class AI(Input):

    def getInput(self, board:ndarray) -> int:
        pass





