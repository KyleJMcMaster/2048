# Board will have protections to allow only legal moves
# will also allow users to make quick copies (of internal array) to make testing new game states easier
# board will calculate score as well
# board representation is a 16 int array from top left to bot right



import random
import time
from typing import List
from numpy import zeros, ndarray


class Board:

    @staticmethod
    def build_board() -> ndarray:
        arr = zeros(17, dtype=int)
        pos = random.sample(range(0, 15), 2)
        val = random.choices([2, 4], weights=[0.9, 0.1], k=2)
        return Board.set_tile_value(arr, pos, val)

    @staticmethod
    def set_tile_value(arr: ndarray, pos: List[int], val: List[int]) -> ndarray:
        # length of pos and val should agree
        # sets corresponding positions on board to specified values
        # TODO: restrict values in pos and val
        for i in range(len(pos)):
            p = pos[i]
            arr[p] = val[i]
        return arr

    @staticmethod
    def check_legal_move(arr: ndarray, move: int) -> bool:
        # checks if move is legal, returns true if legal
        # 0:r,1:l,2:u,3:d
        if move == 0:
            for i in range(16):
                if i % 4 == 3: continue
                if arr[i] != 0 and (arr[i + 1] == 0 or arr[i + 1] == arr[i]):
                    return True
        if move == 1:
            for i in range(16):
                if i % 4 == 0: continue
                if arr[i] != 0 and (arr[i - 1] == 0 or arr[i - 1] == arr[i]):
                    return True
        if move == 2:
            for i in range(16):
                if i < 4: continue
                if arr[i] != 0 and (arr[i - 4] == 0 or arr[i - 4] == arr[i]):
                    return True
        if move == 3:
            for i in range(16):
                if i > 11: continue
                if arr[i] != 0 and (arr[i + 4] == 0 or arr[i + 4] == arr[i]):
                    return True
        return False

    @staticmethod
    def find_empty_squares(arr: ndarray) -> List[int]:
        empty_squares = []
        for i in range(16):
            if arr[i] == 0:
                empty_squares.append(i)
        return empty_squares

    @staticmethod
    def get_score(arr: ndarray) -> int:
        return arr[16]

    @staticmethod
    def get_copy(arr: ndarray) -> ndarray:
        # returns a board object with the same board configuration
        return arr.copy()

    @staticmethod
    def move(arr: ndarray, move: int) -> ndarray:
        # plays move, returns moved array
        # 0:r,1:l,2:u,3:d
        if move == 0:
            for k in range(0, 3):
                for i in range(3 - k, 16 - k, 4):
                    for j in range(1, 4 - k):
                        if arr[i] == 0 and arr[i - j] != 0:
                            arr[i] = arr[i - j]
                            arr[i - j] = 0
                        if arr[i] != 0 and arr[i - j] == arr[i]:
                            arr[i] *= 2
                            arr[i - j] = 0
                            arr[16] += arr[i]
                            break
                        if arr[i] != 0 and arr[i - j] != 0 and arr[i - j] != arr[i]:
                            break
        if move == 1:
            for k in range(0, 3):
                for i in range(0 + k, 13 + k, 4):
                    for j in range(1, 4 - k):
                        if arr[i] == 0 and arr[i + j] != 0:
                            arr[i] = arr[i + j]
                            arr[i + j] = 0
                        if arr[i] != 0 and arr[i + j] == arr[i]:
                            arr[i] *= 2
                            arr[i + j] = 0
                            arr[16] += arr[i]
                            break
                        if arr[i] != 0 and arr[i + j] != 0 and arr[i + j] != arr[i]:
                            break
        if move == 2:
            for k in range(0, 3):
                for i in range(0 + 4 * k, 4 + 4 * k):
                    for j in range(1, 4 - k):
                        if arr[i] == 0 and arr[i + j * 4] != 0:
                            arr[i] = arr[i + j * 4]
                            arr[i + j * 4] = 0
                        if arr[i] != 0 and arr[i + j * 4] == arr[i]:
                            arr[i] *= 2
                            arr[i + j * 4] = 0
                            arr[16] += arr[i]
                            break
                        if arr[i] != 0 and arr[i + j * 4] != 0 and arr[i + j * 4] != arr[i]:
                            break
        if move == 3:
            for k in range(0, 3):
                for i in range(12 - 4 * k, 16 - 4 * k):
                    for j in range(1, 4 - k):
                        if arr[i] == 0 and arr[i - j * 4] != 0:
                            arr[i] = arr[i - j * 4]
                            arr[i - j * 4] = 0
                        if arr[i] != 0 and arr[i - j * 4] == arr[i]:
                            arr[i] *= 2
                            arr[i - j * 4] = 0
                            arr[16] += arr[i]
                            break
                        if arr[i] != 0 and arr[i - j * 4] != 0 and arr[i - j * 4] != arr[i]:
                            break
        return arr.copy()

    @staticmethod
    def display(arr: ndarray):
        print(arr[0:4])
        print(arr[4:8])
        print(arr[8:12])
        print(arr[12:16])

    @staticmethod
    def add_random_square(arr: ndarray) -> ndarray:
        # add random tile in empty square
        pos = random.sample(Board.find_empty_squares(arr), 1)
        val = random.choices([2, 4], weights=[0.9, 0.1], k=1)
        Board.set_tile_value(arr, pos, val)
        return arr

    @staticmethod
    def get_legal_moves(arr: ndarray) -> List[int]:
        # returns a list of legal moves to play
        legal_moves = []
        for i in range(4):
            if Board.check_legal_move(arr, i):
                legal_moves.append(i)

        return legal_moves
