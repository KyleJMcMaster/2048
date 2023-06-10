# Board will have protections to allow only legal moves
# will also allow users to make quick copies (of internal array) to make testing new game states easier
# board will calculate score as well
# board representation is a 16 int array from top left to bot right

import random
from typing import List





class Board:

    def __init__(self, init: bool=True):
        # initialize empty board
        self.values = [0 for i in range(0, 16)]
        self.score = 0
        if init:
            pos = random.sample(range(0, 15), 2)  # sample w/o replacement
            val = random.choices([2, 4], weights=[0.9,0.1], k=2)
            self.set_tile_value(pos, val)

    def set_tile_value(self, pos: List[int], val: List[int]):
        # length of pos and val should agree
        # sets corresponding positions on board to specified values
        # TODO: restrict values in pos and val
        for i in range(len(pos)):
            p = pos[i]
            self.values[p] = val[i]

    def check_legal_move(self, move: int) -> bool:
        # checks if move is legal, returns true if legal
        # 0:r,1:l,2:u,3:d
        if move == 0:
            for i in range(16):
                if i % 4 == 3: continue
                if self.values[i] != 0 and (self.values[i+1] == 0 or self.values[i+1] == self.values[i]):
                    return True
        if move == 1:
            for i in range(16):
                if i % 4 == 0: continue
                if self.values[i] != 0 and (self.values[i-1] == 0 or self.values[i-1] == self.values[i]):
                    return True
        if move == 2:
            for i in range(16):
                if i < 4: continue
                if self.values[i] != 0 and (self.values[i-4] == 0 or self.values[i-4] == self.values[i]):
                    return True
        if move == 3:
            for i in range(16):
                if i > 11: continue
                if self.values[i] != 0 and (self.values[i+4] == 0 or self.values[i+4] == self.values[i]):
                    return True
        return False

    def find_empty_squares(self) -> List[int]:
        empty_squares = []
        for i in range(16):
            if self.values[i] == 0:
                empty_squares.append(i)
        return empty_squares

    def get_score(self) -> int:
        return self.score

    def get_copy(self):
        # returns a board object with the same board configuration
        b = Board(init=False)
        b.values = self.values.copy()
        b.score = self.score
        return b

    def move(self,move: int) -> bool:
        # plays move, returns true if any tile moves
        # 0:r,1:l,2:u,3:d
        tile_moved = False
        if move == 0:
            for k in range(0,3):
                for i in range(3-k,16-k,4):
                    for j in range(1,4-k):
                        if self.values[i] == 0 and self.values[i-j] != 0:
                            self.values[i] = self.values[i-j]
                            self.values[i-j] = 0
                            tile_moved = True
                        if self.values[i] != 0 and self.values[i-j] == self.values[i]:
                            self.values[i] *= 2
                            self.values[i-j] = 0
                            self.score += self.values[i]
                            tile_moved = True
                            break
                        if self.values[i] != 0 and self.values[i-j] != 0 and self.values[i-j] != self.values[i]:
                            break
        if move == 1:
            for k in range(0,3):
                for i in range(0+k,13+k,4):
                    for j in range(1,4-k):
                        if self.values[i] == 0 and self.values[i+j] != 0:
                            self.values[i] = self.values[i+j]
                            self.values[i+j] = 0
                            tile_moved = True
                        if self.values[i] != 0 and self.values[i+j] == self.values[i]:
                            self.values[i] *= 2
                            self.values[i+j] = 0
                            self.score += self.values[i]
                            tile_moved = True
                            break
                        if self.values[i] != 0 and self.values[i+j] != 0 and self.values[i+j] != self.values[i]:
                            break
        if move == 2:
            for k in range(0,3):
                for i in range(0+4*k,4+4*k):
                    for j in range(1,4-k):
                        if self.values[i] == 0 and self.values[i+j*4] != 0:
                            self.values[i] = self.values[i+j*4]
                            self.values[i+j*4] = 0
                            tile_moved = True
                        if self.values[i] != 0 and self.values[i+j*4] == self.values[i]:
                            self.values[i] *= 2
                            self.values[i+j*4] = 0
                            self.score += self.values[i]
                            tile_moved = True
                            break
                        if self.values[i] != 0 and self.values[i+j*4] != 0 and self.values[i+j*4] != self.values[i]:
                            break
        if move == 3:
            for k in range(0,3):
                for i in range(12-4*k,16-4*k):
                    for j in range(1,4-k):
                        if self.values[i] == 0 and self.values[i-j*4] != 0:
                            self.values[i] = self.values[i-j*4]
                            self.values[i-j*4] = 0
                            tile_moved = True
                        if self.values[i] != 0 and self.values[i-j*4] == self.values[i]:
                            self.values[i] *= 2
                            self.values[i-j*4] = 0
                            self.score += self.values[i]
                            tile_moved = True
                            break
                        if self.values[i] != 0 and self.values[i-j*4] != 0 and self.values[i-j*4] != self.values[i]:
                            break
        return tile_moved

    def display(self):
        print(self.values[0:4])
        print(self.values[4:8])
        print(self.values[8:12])
        print(self.values[12:16])

    def add_random_square(self):
        # add random tile in empty square
        pos = random.sample(self.find_empty_squares(),1)
        val = random.choices([2,4],weights=[0.9,0.1],k=1)
        self.set_tile_value(pos, val)

    def get_legal_moves(self) -> List[int]:
        # returns a list of legal moves to play
        legal_moves = []
        for i in range(4):
            if self.check_legal_move(i):
                legal_moves.append(i)

        return legal_moves

