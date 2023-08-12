import pickle
from abc import ABC, abstractmethod
from Game import GameInformation


class Encoder(ABC):

    @staticmethod
    def encode(gameinfo: GameInformation, filename: str) -> None:
        pass


class PickleEncoder(Encoder):

    @staticmethod
    def encode(gameinfo: GameInformation, filename: str) -> None:
        with open(filename, 'ab') as file:
            pickle.dump(gameinfo, file)

