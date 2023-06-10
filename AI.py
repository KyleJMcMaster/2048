from Board import Board
from Input import Input
from typing import List
from itertools import chain



class MinMaxAI(Input):

    def __init__(self, depth: int = 100):
        self.depth = depth
        self.selected_move_tree = []


    def getInput(self, board: Board) -> int:
        # method returns move to play based on a given board state
        # TODO: optimizations to improve pruning, save already calculated values
        root_state = GameState(board)
        current_depth = 0

        root_state.generate_tree()
        current_children = root_state.children
        while current_depth < self.depth:
            new_children = []
            print(len(current_children))
            for child in current_children:
                new_children.append(child.generate_tree())
            current_children = list(chain.from_iterable(new_children))
            current_depth += 1

        mins = [4000000] * 4
        for child in current_children:
            score = child.get_score()
            if score < mins[child.move_made]:
                mins[child.move_made] = score
        print(mins)
        max_move_score = -1
        max_move = -1
        for i in range(4):
            if mins[i] != 4000000 and mins[i] > max_move_score and max_move_score:
                max_move_score = mins[i]
                max_move = i
        print(max_move_score)
        print(max_move)
        return max_move
        # TODO: always getting assinged 0, what's going on

class GameState:

    def __init__(self, board:Board, move_made: int=-1, parent_state=None,first_child:bool=False):
        self.board = board.get_copy()
        self.parent = parent_state
        if first_child or parent_state is None:
            self.move_made = move_made
        else:
            self.move_made = self.parent.move_made

        self.children = []

    def generate_tree(self) -> List:
        # expands game tree by generating all possible game states from this position
        states = []
        legal_moves = self.board.get_legal_moves()
        for move in legal_moves:
            board = self.board.get_copy()
            board.move(move)
            empty_squares = board.find_empty_squares()
            for empty_square in empty_squares:
                b = board.get_copy()
                b.set_tile_value([empty_square], [2])
                states.append(GameState(b, move,  self, self.parent is None))
                b.set_tile_value([empty_square], [4])
                states.append(GameState(b, move, self, self.parent is None))
        self.children = states.copy()
        return states

    def print_tree(self):
        self.board.display()
        for child in self.children:
            print(child.move_made)
            child.board.display()

    def get_score(self) -> int:
        return self.board.get_score()

'''
b = Board(init=False)
b.set_tile_value([2,3,4,5,6,7,8,9,10,11,12,13,14,15],[4,8,16,32,4,4,4,8,8,8,2,2,4,4,4])
g = GameState(b)

g.generate_tree()
g.print_tree()
'''